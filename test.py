#import singleton
#singleton = singleton.Singleton()
#singleton.a = 20


import search
search = search.Search()

while True:
    finalOutput=search.main()
    fp = open('readme.txt', 'w')
    if finalOutput==[404]:
        fp.write("[404]")
    elif finalOutput==[304]:
        fp.write("[304]")
    elif finalOutput[0]==0:
        fp.write("0")
