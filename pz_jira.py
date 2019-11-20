from jira import JIRA
from pz_jira_fileds import jira_dict, step_dict

# import ipdb

fc = 0; lc = 4
# step_dict = {}
j = JIRA("http://jira.pixel8networks.com:8080",basic_auth=('szahid', 'Panew@0308'))
# j = JIRA("http://jira.pixel8networks.com:8080")
# issue = j.issue("QT-43971")
# jids = ['QT-44734', 'QT-44735', 'QT-44736', 'QT-44737', 'QT-44738', 'QT-44739', 'QT-44740', 'QT-44741', 'QT-44742', 'QT-44743', 'QT-44744', 'QT-44745', 'QT-44748']
jids = ['QT-49055',
 'QT-49056',
 'QT-49057',
 'QT-49058',
 'QT-49059',
 'QT-49060',
 'QT-49061',
 'QT-49062',
 'QT-49063',
 'QT-49064',
 'QT-49065']

for jid in jids:
    print "Jira Id : ", jid
    issue = j.issue(jid)
    step_dict = issue.raw['fields']['customfield_10107']
    for ro in step_dict['rows']:
        ro['columns'][lc]['value'] = 'Passed'
    issue.update(fields={'customfield_10107': step_dict})

# issue = j.issue("QT-44746")
#
# print issue.fields.description
# print issue.fields.project
# print issue.fields()
#
# fields = j.fields()
# # name = {field['name']: field['id'] for field in fields}
# name = jira_dict
# print name
#
# # for i, k in name.items():
# #     print i+':  '+ k
# # 'Test Plans',
# cfs = ['Steps Progress','TC Status',  'Status', 'TCT belong to', 'Current status', 'My TC Result',
#       'Labels', 'TC Template', 'Steps', 'Test Version', 'Progress', 'TC Group', ]
# # for cf in cfs:
# #     p = getattr(issue.fields, name[cf])
# #     print "%s  :\t %s"%(cf,p)
#
# # p2 = getattr(issue.fields, name['Steps'])
# # print p2.value
# # ipdb.set_trace()
# import json
# r = issue.raw['fields']
# print str(r['customfield_10107']).encode('ascii')
# # print json.dumps(r['customfield_10107'])
# step_dict = r['customfield_10107']
# col = step_dict['header']['columns']
# cold = {c['number']:c['name'] for c in col}
# print cold
# for ro in step_dict['rows']:
#     print "Row :",ro['number']
#     print "col : %s  value : %s"%(cold[ro['columns'][fc]['number']],ro['columns'][fc]['value'])
#     print "col : %s  value : %s\n"%(cold[ro['columns'][lc]['number']],ro['columns'][lc]['value'])
#     ro['columns'][lc]['value'] = 'Passed'
#
# for ro2 in step_dict['rows']:
#     print "col : %s  value : %s\n"%(cold[ro2['columns'][lc]['number']],ro2['columns'][lc]['value'])
#
# issue.update(fields={'customfield_10107':step_dict})
# for f in issue.raw['fields']:
#     print "%s  :\t %s"%(f, issue.raw['fields'][f])
# print issue.fields.customfield_10107.

smtp = "QT-51054, QT-51055, QT-51056, QT-51057, QT-51058, QT-51059, QT-51060, QT-51061, QT-51062, QT-51063, QT-51064, QT-51065, QT-51066, QT-51067"