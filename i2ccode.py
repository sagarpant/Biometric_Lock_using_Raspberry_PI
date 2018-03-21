#import modules
import smbus
import time

#setup SMBus
bus = smbus.SMBus(1)

bus.write_byte_data(0x20, 0x00, 0x00)
bus.write_byte_data(0x20, 0x01, 0x00)

#initialise counter
counter = 0

#main loop
try:
    while 1:
        for counter in range(0, 255):   #the counter variable increments by 1 through to 255, then loops back to 0
            bus.write_byte_data(0x20, 0x12, counter)    #write the value of counter IODIRA
            bus.write_byte_data(0x20, 0x13, counter)    #write the value of counter IODIRB
            time.sleep(0.5)    #wait for 500ms, alter this time to increase/decrease the speed of the counter

except KeyboardInterrupt:   #when Ctrl + C is pressed, write all the LEDs off
    bus.write_byte_data(0x20, 0x12, 0x00)
    bus.write_byte_data(0x20, 0x13, 0x00)
    print("Program Exited Cleanly")