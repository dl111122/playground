Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> datetime.datetime.fromtimestamp(1437514227)
datetime.datetime(2015, 7, 21, 14, 30, 27)
>>> 
>>> from datetime import datetime
>>> 
>>> from time import gmtime, strftime
>>> strftime ("%a, %d %b %Y %H:%M:%S", gmtime (1437514227))
'Tue, 21 Jul 2015 21:30:27'
>>> 
>>> import time
>>> 
>>> from time import gmtime, strftime
>>> strftime ("%b %d, %Y %H:%M:%S %P", gmtime (1437514227))

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    strftime ("%b %d, %Y %H:%M:%S %P", gmtime (1437514227))
ValueError: Invalid format string
>>> 
>>> from time import gmtime, strftime
>>> strftime ("%b %d, %Y %H:%M:%S", gmtime (1437514227))
'Jul 21, 2015 21:30:27'
>>> 
>>> from time import gmtime, strftime
>>> strftime ("b %d, %Y %H:%M:%S %p", gmtime (1437514227))
'b 21, 2015 21:30:27 PM'
>>> 
>>> 
>>> from time import gmtime, strftime
>>> strftime ("%b %d, %Y %H:%M:%S %p", gmtime (1437514227))
'Jul 21, 2015 21:30:27 PM'
>>> 
