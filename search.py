import sys
import baseMethods, time, lcddriver

class Search:
    global display
    display = lcddriver.lcd()
    baseMethod = baseMethods.BaseMethods()

    def __init__(self):
        pass

    def main(self):
        
        temp = self.baseMethod.genImg()
        
        if temp == 2:
            return [404]
            pass 
        elif (temp == 0):
            if self.baseMethod.img2Tz(1):
                display.lcd_clear()
                display.lcd_display_string('Conversion Error',1)
                time.sleep(2)
                display.lcd_clear()
                sys.exit(0)
            r = self.baseMethod.search()  # template conversion done. Now check whether the finger
            if r[0] == 0:
                return [r[0], r[1], r[2]]
            else:
                return [304]
        else:
            sys.exit(0)