import enroll, search, time, lcddriver


class RegisterAuthorizer:
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
            display.lcd_display_string("Put Authorizer's", 1)
            display.lcd_display_string("Finger", 2)
            a = self.srh.main()  # to check whether the finger is registered. Returns page and id.
            if a[0] != 404 and a[0] != 304:
                try:
                    fp = open('records.txt', 'r')
                    for line in fp:
                        arg1, arg2 = line.split(',')
                        # Check if the authorizer is there in the records
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
                display.lcd_display_string("Put New Finger", 1)
                
                c = self.srh.main()
                if c[0] == 404:
                    pass
                elif c[0] == 304:
                    self.enr.main(1)
                    break
                elif c[0] == 0:
                    h = False;
                    try:
                        fp = open('records.txt', 'r')
                        for line in fp:
                            arg1, arg2 = line.split(',')
                            # Check if the authorizer is there in the records
                            if arg1 == str(a[1]) and arg2 == (str(a[2]) + "\n"):
                                h = True
                                break
                            else:
                                h = False
                    finally:
                        fp.close()

                    if h:
                        display.lcd_clear()
                        display.lcd_display_string("Autho. Already", 1)
                        display.lcd_display_string("Registered", 2)
                        time.sleep(2)
                        display.lcd_clear()
                        break
                    else:
                        try:
                            fp = open('records.txt', 'a')
                            fp.write(str(c[1]) + "," + str(c[2]) + "\n")
                        finally:
                            fp.close()
                        break

        else:
            display.lcd_clear()
            display.lcd_display_string("Finger Isn't", 1)
            display.lcd_display_string("Authorized", 2)
            time.sleep(2)
            display.lcd_clear()

