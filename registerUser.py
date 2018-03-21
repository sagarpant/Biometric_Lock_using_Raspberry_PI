import enroll, search, time, lcddriver

class RegisterUser:
    global display
    display = lcddriver.lcd()
    srh = search.Search()
    enr = enroll.Enroll()

    def __init__(self):
        pass

    def main(self):
        b = False
        timeStamp = time.time()
        while (time.time() - timeStamp) <= 120:
            display.lcd_clear()
            display.lcd_display_string("Put Authorizer's",1)
            display.lcd_display_string("Finger",2)
            a = self.srh.main()
            if a[0] != 404 and a[0] != 304:
                try:
                    fp = open('records.txt', 'r')
                    for line in fp:
                        arg1, arg2 = line.split(',')
                        if arg1 == str(a[1]) and arg2 == (str(a[2]) + "\n"):
                            b = True
                            break
                        else:
                            b = False
                finally:
                    fp.close()
                break
            else:
                pass

        if b:
            timeStamp = time.time()
            while (time.time() - timeStamp) <= 120:
                display.lcd_clear()
                display.lcd_display_string("Put New Finger",1)
                c = self.srh.main()
                if c[0] == 404:
                    pass
                elif c[0] == 304:
                    self.enr.main(1)
                    break
                else:
                    display.lcd_clear()
                    display.lcd_display_string("Already",1)
                    display.lcd_display_string("Registered",2)
                    time.sleep(2)
                    display.lcd_clear()
                    break
        else:
            display.lcd_clear()
            display.lcd_display_string("Finger Isn't",1)
            display.lcd_display_string("Authorized",2)
            time.sleep(2)
            display.lcd_clear()