import serial
import time
#import _thread
#from XOR_CheckSum import XOR_CheckSum_string


def XOR_CheckSum_string(m_str, encoding="utf-8"):
    if str == type(m_str):
        try:
            m_str = bytes(m_str,encoding=encoding)
        except:
            #m_str = bytes(m_str)
            m_str=m_str.encode(encoding=encoding)
    sum = 0x0
    #print(m_str)
    #print(type(m_str))
    for c in m_str:
        try:
            sum = sum ^ c
        except:
            #print(c)
            sum = sum ^ int(c,16)
    sum = sum ^ 0x0
    return sum


def read_serial(ser):
    while True:
        line = ser.readline()
        print(line)


class TXA:
    def __init__(self, user_address, serial, sender_identifier='CC', communication_category='1', transfer_method='0'):
        self.sender_identifier = sender_identifier
        self.user_address = user_address
        self.communication_category = communication_category
        self.transfer_method = transfer_method
        self.serial = serial

    def message(self, content, address=''):
        if address == '':
            address = self.user_address
        message = self.sender_identifier + 'TXA' + ',' + \
                  address + ',' + \
                  self.communication_category + ',' + \
                  self.transfer_method + ',' + \
                  content
        #print(XOR_CheckSum_string(message, encoding="utf-8"))
        self.xor_checkSum = hex(XOR_CheckSum_string(message, encoding="utf-8"))[2:4]
        '''try:
            self.xor_checkSum = hex(XOR_CheckSum_string(message, encoding="utf-8"))[2:4]
        except:
            self.xor_checkSum = hex(XOR_CheckSum_string(message))[2:4]'''
        message = '$' + message + '*' + self.xor_checkSum + '\r\n'
        return bytes(message, encoding="utf-8")

    def send(self, message):
        self.serial.write(message)

    def read(self):
        try:
            import _thread
            _thread.start_new_thread(read_serial, (self.serial,))
        except:
            import thread
            thread.start_new_thread(read_serial, (self.serial,))


def test():
    ser = serial.Serial('/dev/ttyUSB1', 115200)
    print(ser)
    _thread.start_new_thread(read_serial, (ser,))
    for i in range(5):
        # ser.write(b'$CCICA,0,00*7B\r\n')
        ser.write(b'$CCICI,0,00*73\r\n')
        # line = ser.readline()
        # print(line)
        time.sleep(1)

    for i in range(100):
        ser.write(b'$CCTXA,0247718,1,1,3132333435*70\r\n')
        time.sleep(80)

    ser.close()


if __name__ == "__main__":
    '''print(hex(XOR_CheckSum_string('CCICA,0,00')))
    print(hex(XOR_CheckSum_string('CCICI,0,00')))
    print(hex(XOR_CheckSum_string('CCTXA,0247718,1,1,3132333435')))

    print(hex(XOR_CheckSum_string(b'CCICA,0,00')))
    print(hex(XOR_CheckSum_string(b'CCICI,0,00')))
    print(hex(XOR_CheckSum_string(b'CCTXA,0247718,1,1,3132333435')))

    print(hex(XOR_CheckSum_string(bytes('CCICA,0,00', encoding="utf-8"))))
    print(hex(XOR_CheckSum_string(bytes('CCICI,0,00', encoding="utf-8"))))
    print(hex(XOR_CheckSum_string(bytes('CCTXA,0247718,1,1,3132333435', encoding="utf-8"))))'''

    ser = serial.Serial('/dev/ttyUSB1', 115200)
    txa = TXA(user_address='0247718', serial=ser, transfer_method='1')
    txa.read()

    message = txa.message(content='3132333435')
    print(message)
    txa.send(message=message)

    time.sleep(60)

    # test()
8
