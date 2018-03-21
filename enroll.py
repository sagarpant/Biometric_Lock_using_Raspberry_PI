import time, sys, baseMethods,lcddriver


class Enroll:
    baseMethod = baseMethods.BaseMethods()
    global display
    display = lcddriver.lcd()

    def __init__(self):
        pass

    def main(self, mode):
        # mode = 1 for normal user
        # mode = 2 for authorizer

        self.body2()

        while True:
            resultRegModel = self.baseMethod.regModel()
            if resultRegModel == 10:
                display.lcd_clear()
                display.lcd_display_string("Fingerprints are", 1)
                display.lcd_display_string("not the same", 2)
                time.sleep(2)
                display.lcd_clear()
                self.body2()
            elif resultRegModel == 1:
                display.lcd_clear()
                display.lcd_display_string('Internal Error', 1)
                time.sleep(2)
                display.lcd_clear()
                sys.exit(0)
            else:
                break

        
        vtnOutput = self.baseMethod.valid_temp_num()
        if vtnOutput[0] == 0:  # if the function was executed successfuly
            pg = 0  # vtnOutput[1]
            id = vtnOutput[2]
            if id == 255:  # one extra condition of pg==0 removed
                display.lcd_clear()
                display.lcd_display_string("Memory full",1)
                time.sleep(2)
                display.lcd_clear()
                system.exit(0)
        else:
            display.lcd_clear()
            display.lcd_display_string("Internal Error!",1)
            time.sleep(2)
            display.lcd_clear()
            sys.exit(0)
            
        if self.baseMethod.store(pg, id):
            display.lcd_clear()
            display.lcd_display_string('Store Error!',1)
            time.sleep(2)
            display.lcd_clear()
            sys.exit(0)
        # Proceed from here as no errors found.
        
        if mode == 1:
            display.lcd_clear()
            display.lcd_display_string("Registration",1)
            display.lcd_display_string("Success",2)
            time.sleep(2)
            display.lcd_clear()
        elif mode == 2:
            try:
                fp = open('records.txt', 'a')
                fp.write(str(pg) + "," + str(id) + "\n")
            finally:
                fp.close()
            display.lcd_clear()
            display.lcd_display_string("Authorization",1)
            display.lcd_display_string("Success",2)
            time.sleep(2)
            display.lcd_clear()
        else:
            display.lcd_clear()
            display.lcd_display_string("Internal Error",1)
            time.sleep(2)
            display.lcd_clear()
    def body(self, comment1, comment2):
        display.lcd_clear()
        display.lcd_display_string(comment1,1)
        display.lcd_display_string(comment2,2)
        sys.stdout.flush()

        time.sleep(1)
        timeStamp = time.time()

        while self.baseMethod.genImg():
            if (time.time() - timeStamp) <= 120:
                time.sleep(0.1)
                sys.stdout.flush()
            else:
                break

        display.lcd_clear()
        display.lcd_display_string('Processing',1)
        sys.stdout.flush()

    def body2(self):
        self.body("Put New Finger", "Again 1")

        if self.baseMethod.img2Tz(1):
            display.lcd_clear()
            display.lcd_display_string('Conversion Error',1)
            time.sleep(2)
            display.lcd_clear()
            self.body("Put New Finger", "Again 1")

        self.body("Put New Finger", "Again 2")

        if self.baseMethod.img2Tz(2):
            display.lcd_clear()
            display.lcd_display_string('Conversion Error',1)
            time.sleep(2)
            display.lcd_clear()
            self.body("Put New Finger", "Again 2")