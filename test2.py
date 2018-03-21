import singleton
import time

singleton = singleton.Singleton()
singleton.a = 10
while True:
    print (singleton.a)
    time.sleep(1)    
