import time
import datetime
print "dsjglkgfdk: %s" %time.gmtime(1437514227)
my_variable = time.gmtime(1437514252)
print "Convert UTC to current: %s" %time.asctime(my_variable)
my_variable = time.gmtime(1437514253)
count = 1437514227
while count < 1437516095:
    print count
    count += 1
