import serial, time, datetime, struct
import sys 

ser = serial.Serial('/dev/ttyUSB0',57600)
pack = [0xef01, 0xffffffff, 0x1]

def printx(l):
	for i in l:
		print hex(i),
	print ''

def readPacket():
	time.sleep(1)
	w = ser.inWaiting()
	ret = []
	if w >= 9:
		s = ser.read(9) #partial read to get length
		ret.extend(struct.unpack('!HIBH', s))
		ln = ret[-1]
		
		time.sleep(1)
		w = ser.inWaiting()
		if w >= ln:
			s = ser.read(ln)
			form = '!' + 'B' * (ln - 2) + 'H'
			ret.extend(struct.unpack(form, s))
	return ret


def writePacket(data):
	pack2 = pack + [(len(data) + 2)]
	a = sum(pack2[-2:] + data)
	pack_str = '!HIBH' + 'B' * len(data) + 'H'
	l = pack2 + data + [a]
	s = struct.pack(pack_str, *l)
	ser.write(s)


def verifyFinger():
	data = [0x13, 0x0, 0, 0, 0]
	writePacket(data)
	s = readPacket()
	return s[4]
	
def genImg():
	data = [0x1]
	writePacket(data)
	s = readPacket()
	return s[4]	

def img2Tz(buf):
	data = [0x2, buf]
	writePacket(data)
	s = readPacket()
	return s[4]

def regModel():
	data = [0x5]
	writePacket(data)
	s = readPacket()
	return s[4]

def store(id):
	data = [0x6, 0x1, 0x0, id]
	writePacket(data)
	s = readPacket()
	return s[4]
def empty():
        data = [0xd]
	writePacket(data)
	s = readPacket()
	print s[4]
	return s[4]

def valid_temp_num():
        data = [0x1d]
        writePacket(data)
        s = readPacket()
        print [s[4], s[5], s[6]]
        return [s[4], s[5], s[6]]
    
if verifyFinger():
	print 'Verification Error'
	sys.exit(0)
print 'Put finger',
sys.stdout.flush()


time.sleep(1)	
while genImg():
	time.sleep(0.1)

	print '.',
	sys.stdout.flush()

print ''
sys.stdout.flush()

if img2Tz(1):
	print 'Conversion Error'
	sys.exit(0)

print 'Put finger again',
sys.stdout.flush()
time.sleep(1)	
while genImg():
	time.sleep(0.1)
	print '.',
	sys.stdout.flush()

print ''
sys.stdout.flush()

if img2Tz(2):
	print 'Conversion Error'
	sys.exit(0)

if regModel():
	print 'Template Error'
	sys.exit(0)
id=0
if store(id):
	print 'Store Error'
	sys.exit(0)	

sys.stdout.flush()
print "Enrolled successfully at id %d"%id
valid_temp_num()
