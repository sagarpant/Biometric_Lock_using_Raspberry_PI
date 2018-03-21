import search, buttons, time, registerUser, registerAuthorizer, lockOutput, irsensor
import baseMethods, sys, lcddriver
import RPi.GPIO as GPIO

display = lcddriver.lcd()
search = search.Search()
but = buttons.Buttons()
lockOutput = lockOutput.LockOutput()
irsens=irsensor.Irsens()
baseMethod = baseMethods.BaseMethods()

count = 0


def sButPressed(title):
    if title == "Register User":
        regUser = registerUser.RegisterUser()
        regUser.main()
    
    elif title == "Register Authorizer":
        regAutho = registerAuthorizer.RegisterAuthorizer()
        regAutho.main()
        

def mButPressed():
    global count
    count += 1

    if count == 1:
        display.lcd_clear()
        display.lcd_display_string("Register User",1)
        while but.button_1() or but.button_2():
            pass
        time.sleep(0.5)
        timestamp1 = time.time()
        while (time.time() - timestamp1) <= 120:
            if but.button_2():
                sButPressed("Register User") #registration process initiated
                break
            elif but.button_1():
                count += 1
                break

    if count == 2:
        while but.button_1() or but.button_2():
            pass
        display.lcd_clear()
        display.lcd_display_string("Register", 1)
        display.lcd_display_string("Authorizer", 2)
        time.sleep(0.5)
        timestamp1 = time.time()
        while (time.time() - timestamp1) <= 120:
            if but.button_2():
                sButPressed("Register Authorizer")
                break
            elif but.button_1():
                count += 1
                break

    else:
        count = 0


if baseMethod.verifyFinger():
    display.lcd_clear() 
    display.lcd_display_string('Verification Error', 1)
    time.sleep(1.4)
    sys.exit(0)

GPIO.setmode(GPIO.BCM)

while but.button_1() or but.button_2():
    pass
while True:
    if irsens.ir():  # buzzer high
        pass
        
    if but.button_1():
        mButPressed()
        time.sleep(0.5)
    else:
        time.sleep(0.05)
        display.lcd_display_string("Put Finger", 1)
        finalOutput = search.main()
        if finalOutput[0] == 0:
            display.lcd_clear()
            display.lcd_display_string("Access Granted", 1)
            lockOutput.main()
            time.sleep(1)
            display.lcd_clear()
            
            # GPIO.setup(n, GPIO.IN) #n is the relay pin output
        if finalOutput == [304]:
            display.lcd_clear()
            display.lcd_display_string("Access Denied", 1)
            time.sleep(1)
            display.lcd_clear()
