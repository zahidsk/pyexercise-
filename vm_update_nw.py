'''
Copyright 2013-2014 Reubenur Rahman
All Rights Reserved
@author: reuben.13@gmail.com
'''

import atexit
import argparse
import sys
import time

from pyVmomi import vim, vmodl
from pyVim import connect
from pyVim.connect import Disconnect, SmartConnect

inputs = {'vcenter_ip': '10.180.1.8',
          'vcenter_password': 'PanBar168',
          'vcenter_user': 'pixel8networks\\pandas',
          'vm_name': 'CC_SZ_HABC1_192',
          'isDHCP': False,
          'vm_ip': '10.201.15.144',
          'subnet': '255.255.255.0',
          'gateway': '10.201.15.1',
          'dns': ['10.199.0.1', '10.199.6.1'],
          'domain': 'demosp.com'
          }


def get_obj(content, vimtype, name):
    """
     Get the vsphere object associated with a given text name
    """
    obj = None
    container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
    for c in container.view:
        if c.name == name:
            obj = c
            break
    return obj


def wait_for_task(task, actionName='job', hideResult=False):
    """
    Waits and provides updates on a vSphere task
    """

    while task.info.state == vim.TaskInfo.State.running:
        time.sleep(2)

    if task.info.state == vim.TaskInfo.State.success:
        if task.info.result is not None and not hideResult:
            out = '%s completed successfully, result: %s' % (actionName, task.info.result)
            print out
        else:
            out = '%s completed successfully.' % actionName
            print out
    else:
        out = '%s did not complete successfully: %s' % (actionName, task.info.error)
        raise task.info.error
        print out

    return task.info.result


def main():
    # args = GetArgs()
    try:
        si = None
        # try:
        #     print "Trying to connect to VCENTER SERVER . . ."
        #     # si = connect.Connect(inputs['vcenter_ip'], 443, inputs['vcenter_user'], inputs['vcenter_password'])
        #     si = SmartConnect(host=inputs['vcenter_ip'], user=inputs['vcenter_user'], pwd=inputs['vcenter_password'])
        #
        # except IOError, e:
        #     pass
        #     atexit.register(Disconnect, si)
        print "Trying to connect to VCENTER SERVER . . ."
        try:
            si = SmartConnect(
                host=inputs['vcenter_ip'],
                user=inputs['vcenter_user'],
                pwd=inputs['vcenter_password'],
            )
        except Exception as exc:
            print "Exception catch ",exc.args
            if isinstance(exc, vim.fault.HostConnectFault) or '[SSL: CERTIFICATE_VERIFY_FAILED]' in exc.args[1]:
                try:
                    import ssl
                    print "in smart hadling"
                    default_context = ssl._create_default_https_context
                    ssl._create_default_https_context = ssl._create_unverified_context
                    si = SmartConnect(
                        host=inputs['vcenter_ip'],
                        user=inputs['vcenter_user'],
                        pwd=inputs['vcenter_password'],
                    )
                    ssl._create_default_https_context = default_context
                except Exception as exc1:
                    raise Exception(exc1)
            else:
                raise Exception(exc)

        print "Connected to VCENTER SERVER !"
        # if isinstance(si, connect):
        #     print "Yes"
        # else:
        #     print "No.."*3
        content = si.RetrieveContent()

        # vm_name = args.vm
        vm_name = inputs['vm_name']
        vm = get_obj(content, [vim.VirtualMachine], vm_name)

        if vm.runtime.powerState != 'poweredOff':
            print "WARNING:: Power off your VM before reconfigure"
            sys.exit()

        adaptermap = vim.vm.customization.AdapterMapping()
        globalip = vim.vm.customization.GlobalIPSettings()
        adaptermap.adapter = vim.vm.customization.IPSettings()

        isDHDCP = inputs['isDHCP']
        if not isDHDCP:
            """Static IP Configuration"""
            adaptermap.adapter.ip = vim.vm.customization.FixedIp()
            adaptermap.adapter.ip.ipAddress = inputs['vm_ip']
            adaptermap.adapter.subnetMask = inputs['subnet']
            adaptermap.adapter.gateway = inputs['gateway']
            globalip.dnsServerList = inputs['dns']

        else:
            """DHCP Configuration"""
            adaptermap.adapter.ip = vim.vm.customization.DhcpIpGenerator()

        adaptermap.adapter.dnsDomain = inputs['domain']

        globalip = vim.vm.customization.GlobalIPSettings()

        # For Linux . For windows follow sysprep
        ident = vim.vm.customization.LinuxPrep(domain=inputs['domain'],
                                               hostName=vim.vm.customization.FixedName(name=vm_name))

        customspec = vim.vm.customization.Specification()
        # For only one adapter
        customspec.identity = ident
        customspec.nicSettingMap = [adaptermap]
        customspec.globalIPSettings = globalip

        # Configuring network for a single NIC
        # For multipple NIC configuration contact me.

        print "Reconfiguring VM Networks . . ."

        task = vm.Customize(spec=customspec)

        # Wait for Network Reconfigure to complete
        wait_for_task(task, si)

    except vmodl.MethodFault, e:
        print "Caught vmodl fault: %s" % e.msg
        return 1
    except Exception, e:
        print "Caught exception: %s" % str(e)
        return 1


# Start program
if __name__ == "__main__":
    main()