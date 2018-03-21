import serial, time, struct


class BaseMethods:
    ser = serial.Serial('/dev/ttyUSB0', 57600)
    pack = [0xef01, 0xffffffff, 0x1]

    def __init__(self):
        pass

    def readPacket(self,bytes):
        w = 0
        while True:
            if w >= bytes:
                break
            w = self.ser.inWaiting()
        ret = []
        if w >= 9:
            s = self.ser.read(9)
            ret.extend(struct.unpack('!HIBH', s))
            ln = ret[-1]
        
        
            if w >= ln:
                s = self.ser.read(ln)
                form = '!' + 'B' * (ln - 2) + 'H'
                ret.extend(struct.unpack(form, s))
        return ret

    def writePacket(self, data):
        pack2 = self.pack + [(len(data) + 2)]
        a = sum(pack2[-2:] + data)
        pack_str = '!HIBH' + 'B' * len(data) + 'H'
        l = pack2 + data + [a]
        s = struct.pack(pack_str, *l)
        self.ser.write(s)

    def verifyFinger(self):
        data = [0x13, 0x0, 0, 0, 0]
        self.writePacket(data)
        s = self.readPacket(12)
        return s[4]

    def genImg(self):
        data = [0x1]
        self.writePacket(data)
        s = self.readPacket(12)
        return s[4]

    def img2Tz(self, buf):
        data = [0x2, buf]
        self.writePacket(data)
        s = self.readPacket(12)
        return s[4]

    def regModel(self):
        data = [0x5]
        self.writePacket(data)
        s = self.readPacket(12)
        return s[4]

    def store(self, pg, id):
        data = [0x6, 0x1, pg, id]
        self.writePacket(data)
        s = self.readPacket(12)
        return s[4]

    def valid_temp_num(self):
        data = [0x1d]
        self.writePacket(data)
        s = self.readPacket(14)
        return [s[4], s[5], s[6]]

    def search(self):
        data = [0x4, 0x1, 0x0, 0x0, 0x0, 255]
        self.writePacket(data)
        s = self.readPacket(16)
        return s[4:-1]

     
    #def delete(self) :
    #    data = [0xd ]
    #    self.writePacket(data)
    #    s = self.readPacket()
    #    return s
    
