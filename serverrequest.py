import urllib2, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    if(not GPIO.input(17)):
        print("Loading")
        time.sleep(0.5)
        req = urllib2.Request('http://www.google.com')
        try:
            resp = urllib2.urlopen(req)
        except urllib2.HTTPError as e:
            if e.code == 404:
                print "abc"
                # do something...
            else:
                # ...
                print "def"
        except urllib2.URLError as e:
            # Not an HTTP-specific error (e.g. connection refused)
            # ...
            print "ofb"
        else:
            # 200
            body = resp.read()
            print body
    else:
        time.sleep(0.5)
        print "Button not Pressed"