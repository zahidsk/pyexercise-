print ("While List")
import timeit
start = timeit.default_timer()
print (start)
# for k in ('policy', 'site', 'rpo'):
for k in ['policy', 'site', 'rpo']:
    print (k)
stop = timeit.default_timer()
print (stop)
print (stop-start)
# print ("While list")
# for k in ['policy', 'site', 'rpo']:
#     print