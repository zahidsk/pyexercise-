list1 = ['test', 'test', 'test', 'Machine_Gtjrmyxohcxsrgvtdrwugkryaxlqzh job for machine TestJobType failed.', 'Machine_Jhmajfsqjmqwyylguobhrbdsipnaij job for machine TestJobType failed.', 'Backup job for machine Magneson-scale-r5u25-centos73-tiny-003 failed.', 'Backup job for machine Dan_Tiny_Running - Recovery-nfs failed.', 'Backup job for machine Dan_Tiny_Running - Recovery-smb-rep -VB1.6.0 failed.']
vm = 'test'
cnt = len([1 for x in list1 if vm in x])
print(cnt)
# ################

s = "\\\\smoke-infra.mgmt.smoke\\root\\share\\smoke\\presub\\logs\\alreadyPlusWide.shaikhz.1554722497.67532_cmode_1of1\\010_test\\001_cit-cifs-ext\\cit-cifs-widelink\\cit-cifs-widelink1\\cit-cifs-link1\\cit-cifs-link1\\already_present_tcs\\Parallel_blk\\branchcache\\02_Branchcache_CIT"
print(len(s))

