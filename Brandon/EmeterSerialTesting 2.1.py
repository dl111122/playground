# connect to emeter directly

from __future__ import print_function
import serial
import sys
import time
voltage = 0
current = 0
ampHrs = 0
fiveMinuteAverage = 0
currentList = []
####################################################
def main():
    # to list serial ports: python -m serial.tools.list_ports
    # emeter uses 2400 baud, 8 bits, 1 stop bit, even parity, no hardware flow control
    # on hobbes    
    with serial.Serial(port="/dev/ttyUSB0",
                       baudrate=2400, bytesize=8, parity='E',
                       stopbits=1, xonxoff=0, rtscts=0, timeout=1) as ser:
        count = 0
        print ("Voltage Current AmpHours")
        while True:
            count = count + 1
            findStart(ser)
            # source address
            x = ord(ser.read())
            if x != 0x00:
                print('--- unexpected source address %x s.b. 0x00' % (x))
                continue
            #  device id
            x = ord(ser.read())
            if x != 0x22:
                print('--- unexpected device id %x s.b. 0x22' % (x))
                continue
            # message type
            readMessage(ser)
            currentlist.append (current)
            if count % 300 == 0:
                for currentValues in currentList:
                    fiveMinuteAverage += currentValue
                fiveMinuteAverage = fiveMinuteAverage/300
                while len (currentList) > 0: del currentList[0]
            if count % 8 == 0:
                n =  time.ctime() 
                print ("%s %f %f %f \n" %(n, voltage, current, ampHrs, fiveMinuteAverage), end = "")
            
                
    return 0


def findStart(ser):
    """keep on reading till you get the start byte - 0x80"""
    count = 0
    while True:
        count = count + 1
        x = ord(ser.read())
        if x == 0x80:
            #print('\n Found it!')
            if count > 1:
                print ('')
            break
        if count == 1:
            print('--- Looking for start byte ', end='')
        print('%x ' % (x), end='')
        if (count % 8) == 0:
            print('')       # newline


def readMessage(ser):
    global voltage, current, ampHrs
    """read the message"""
    x = ord(ser.read())              # message type
    if x == 0x60:
        (sign, value) = readData(ser)
        voltage = value * 0.01
    elif x == 0x61:
        (sign, value) = readData(ser)
        current = sign * value * 0.01
    elif x == 0x62:
        (sign, value) = readData(ser)
        ampHrs = sign * value * 0.1
    elif x == 0x64:
        (sign, value) = readData(ser)
        stateOfCharge = value * 0.1
        #print("stateOfCharge(percentage) = %f" % stateOfCharge)
    elif x == 0x65:
        (sign, value) = readData(ser)
        timeRemaining = sign * value
        #print("timeRemaining(minutes) = %f" % timeRemaining)
    elif x == 0x66:
        (sign, value) = readData(ser)
        battTemp = sign * value * 0.1
        #print("battTemp(Celsius) = %f" % battTemp)
    elif x == 0x67:
        (sign, value) = readData(ser)
        monitorStatus = value
        #print("monitorStatus(bitfield) = 0x%x" % monitorStatus)
    elif x == 0x68:
        (sign, value) = readData(ser)
        auxVoltage = value * 0.01
        #print("auxVoltage(volts) = %f" % auxVoltage)
    elif x == 0x3c:
        print('--- Right Arrow pressed')
        terminator = ord(ser.read())
        if terminator != 0xff:
            print('\nunexpected terminator %x s.b. 0xff - bytes read u1-u3 %x %x %x\n' % (terminator, u1, u2, u3))
    elif x == 0x3e:
        print('--- Left Arrow pressed')
        terminator = ord(ser.read())
        if terminator != 0xff:
            print('\nunexpected terminator %x s.b. 0xff - bytes read u1-u3 %x %x %x\n' % (terminator, u1, u2, u3))
    else:
        print('--- unexpected message type %x' % x)
        count = 0
        while True:
            count = count + 1
            x = ord(ser.read())
            if x == 0xff:
                if count > 1:
                    print('')
                break
            if count == 1:
                print('Looking for terminator byte ', end='')
            print('%x ' % (x), end='')
            if (count % 8) == 0:
                print('')       # newline


def readData(ser):
    """read 3 data bytes and final terminator"""
    u1 = ord(ser.read())
    u2 = ord(ser.read())
    u3 = ord(ser.read())
    terminator = ord(ser.read())
    signbit = (u1 >> 6) & 1
    if signbit:
        sign = -1
    else:
        sign = 1
    value = ((u1 & 0x3f) << 14) + ((u2 & 0x7f) << 7) + (u3 & 0x7f)
    if terminator != 0xff:
        print('\nunexpected terminator %x s.b. 0xff - bytes read u1-u3 %x %x %x\n' % (terminator, u1, u2, u3))
    return(sign, value)

####################################################
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    ret = main()
    sys.exit(ret)
