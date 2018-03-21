
class Singleton:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance 

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
    a = 5
# A little testing

#s = Singleton() # Ok
#Singleton() # will raise exception
#print (s)

#s = Singleton.getInstance()
#print (s)

#s = Singleton.getInstance()
#rint (s) # will print the same instance as before