s= """GET
/pzapi/config/persistentReadCacheSwitch
Get persistentReadCacheSwitch
PUT
/pzapi/config/persistentReadCacheSwitch
Update persistentReadCacheSwitch
GET
/pzapi/config/persistentReadCacheSize
Get persistentReadCacheSize
PUT
/pzapi/config/persistentReadCacheSize
Update persistentReadCacheSize
GET
/pzapi/config/persistentReadCacheSizeMaximum
Get persistentReadCacheSizeMaximum
PUT
/pzapi/config/persistentReadCacheSizeMaximum
Update persistentReadCacheSizeMaximum
GET
/pzapi/config/cacheAll
Get cacheAll
PUT
/pzapi/config/cacheAll
Update cacheAll
GET
/pzapi/config/autoPrepop
Get autoPrepop
PUT
/pzapi/config/autoPrepop
Update autoPrepop
GET
/pzapi/config/sysLogging
Get sysLogging
PATCH
/pzapi/config/sysLogging
Update sysLogging (object)
GET
/pzapi/config/smtpServer
Get smtpServer
PUT
/pzapi/config/smtpServer
Update smtpServer
GET
/pzapi/config/smtpPort
Get smtpPort
PUT
/pzapi/config/smtpPort
Update smtpPort
GET
/pzapi/config/smtpSender
Get smtpSender
PUT
/pzapi/config/smtpSender
Update smtpSender
GET
/pzapi/config/smtpUseEncrypt
Get smtpUseEncrypt
PUT
/pzapi/config/smtpUseEncrypt
Update smtpUseEncrypt
GET
/pzapi/config/smtpUseAuth
Get smtpUseAuth
PUT
/pzapi/config/smtpUseAuth
Update smtpUseAuth
GET
/pzapi/config/smtpUsername
Get smtpUsername
PUT
/pzapi/config/smtpUsername
Update smtpUsername
GET
/pzapi/config/smtpPassword
Get smtpPassword
PUT
/pzapi/config/smtpPassword
Update smtpPassword
GET
/pzapi/config/staticRoute
Get all staticRoute(s)
GET
/pzapi/config/staticRoute/{ipaddr}
Get staticRoute row
DELETE
/pzapi/config/staticRoute/{ipaddr}
Delete staticRoute row
PATCH
/pzapi/config/staticRoute/{ipaddr}
Add/update staticRoute row
GET
/pzapi/config/enableJumboFrame
Get enableJumboFrame
PUT
/pzapi/config/enableJumboFrame
Update enableJumboFrame
GET
/pzapi/config/name
Get name
PUT
/pzapi/config/name
Update name
GET
/pzapi/config/email
Get email
PUT
/pzapi/config/email
Update email
GET
/pzapi/config/title
Get title
PUT
/pzapi/config/title
Update title
GET
/pzapi/config/configurationMode
Get configurationMode
PUT
/pzapi/config/configurationMode
Update configurationMode"""
ra = s.split("\n")
arrang_apis = []
for i in range(0,len(ra),3):
    arrang_apis.append(" ".join(ra[i:i+3]))

print 'total APIs : ',len(arrang_apis)
for i in arrang_apis: print i


# s2 = "\n".join(arrang_apis)
s2 = """GET /pzapi/config/cloud_provider Get cloud_provider
PUT /pzapi/config/cloud_provider Update cloud_provider
"""
# arrang_apis = s2.split("\n")

# for sn, i in enumerate(arrang_apis):
#     print i.split(" ")[1]
# urls_only = set([i.split(" ")[1] for i in arrang_apis])
urls_only = []
for ur in [i.split(" ")[1] for i in arrang_apis]:
    if ur in urls_only:
        continue
    urls_only.append(ur)
print "Urls Only : "
for i in urls_only: print i
# Docs : To create url variable and url for urls.robot file use following code
s = """/pzapi/config/cloud_provider
/pzapi/config/cloud_provider
/pzapi/config/csp_hostname
/pzapi/config/csp_hostname
/pzapi/config/csp_username
/pzapi/config/csp_username
/pzapi/config/csp_bucket
/pzapi/config/csp_bucket
/pzapi/config/csp_fs_path
/pzapi/config/csp_fs_path
/pzapi/config/csp_size
/pzapi/config/csp_size
/pzapi/config/csp_caliber
/pzapi/config/csp_caliber
/pzapi/config/companyName
/pzapi/config/companyName"""

import re
# url_var_name =  ['_'.join([spapi.upper() for spapi in re.sub('(?!^)([A-Z][a-z]+)', r' \1', api).split()])+'_URL' for api in [i.split("/")[-1] for i in s.split("\n")]]
url_var_name = ['_'.join([spapi.upper() for spapi in re.sub('(?!^)([A-Z][a-z]+)', r' \1', api).split()])+'_URL' for api in [i.split("/")[-1] for i in urls_only]]
print "API type Count : ",len(url_var_name)
print "="*20+"\n Append below code to urls.robot file "
for vname, url in zip(url_var_name, urls_only):
    print "${%s}    %s"%(vname,url)

# Docs : To generate api for rest automation use following code

# s = """${DEFAULT_BANDWIDTH_URL}    /pzapi/config/defaultBandwidth
# ${BANDWIDTH_LIMIT_URL}    /pzapi/config/bandwidthLimit
# ${HA_LOCAL_URL}    /pzapi/config/haLocal
# ${TRACE_LOGGING_URL}    /pzapi/config/traceLogging"""
# #
url = [i.split('  ')[0] for i in s.split('\n')]
get_key = ['get_'+i.split('/')[-1] for i in urls_only]
set_key = ['set_'+i.split('/')[-1] for i in urls_only]
delete_key = ['delete_'+i.split('/')[-1] for i in urls_only]
patch_key = ['patch_'+i.split('/')[-1] for i in urls_only]

print url
print get_key
print set_key
# for i,j in zip(set_key,get_key):
#     print j
#     print i
url_var_robot = ['${%s}'%var for var in url_var_name]

print "="*20+"\n Append below code to resource file "
for i in range(len(url_var_robot)):
    print "%s\n\tRun Keyword And Return   Get   %s\n"%(get_key[i], url_var_robot[i])
    print "%s\n\t[Arguments]   ${val}\n\tRun Keyword And Return    Put    ${val}   %s\n"%(set_key[i], url_var_robot[i])
#     print "%s\n\t[Arguments]   ${val}\n\tRun Keyword And Return    Delete    ${val}   %s\n"%(delete_key[i], url_var_robot[i])
#     print "%s\n\t[Arguments]   ${val}\n\tRun Keyword And Return    Patch    ${val}   %s\n"%(patch_key[i], url_var_robot[i])

# s = "${time_SCHED_SNAP_LIMIT}   /pzapi/config/stimScheduledSnapshotLimit"
#
# for sched in ['montly','weekly','nightly', 'hourly']:
#     print s.replace('time', sched.upper()).replace('stim', sched)

"""QTCT-10579, QTCT-10580, QTCT-10581, QTCT-10582, QTCT-10583, QTCT-10584, QTCT-10585, QTCT-10586, QTCT-10587, QTCT-10588,
 QTCT-10589, QTCT-10590, QTCT-10591, QTCT-10592, QTCT-10593, QTCT-10594, QTCT-10595, QTCT-10596, QTCT-10597, QTCT-10598,
 QTCT-10599, QTCT-10600, QTCT-10601, QTCT-10602, QTCT-10603, QTCT-10604,QTCT-10605, QTCT-10606, QTCT-10607, QTCT-10608,
 QTCT-10609, QTCT-10610, QTCT-10611, QTCT-10612"""