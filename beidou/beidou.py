import serial
import time


# import _thread
# from XOR_CheckSum import XOR_CheckSum_string


def XOR_CheckSum_string(m_str, encoding="utf-8"):
    if str == type(m_str):
        try:
            m_str = bytes(m_str, encoding=encoding)
        except:
            # m_str = bytes(m_str)
            m_str = m_str.encode(encoding=encoding)
    sum = 0x0
    # print(m_str)
    # print(type(m_str))
    for c in m_str:
        try:
            sum = sum ^ c
        except:
            # print(c)
            sum = sum ^ ord(c)
    sum = sum ^ 0x0
    return sum


def read_serial(serial, transfer_method=2, encoding="gb2312"):
    while True:
        line = serial.readline()
        print(line)

        if line[3:6] == b'TXR':
            tmp = line.split(b',')[-1]
            msg = tmp.split(b'*')[0]
            if transfer_method == '2' and msg[0:2] == b'A4':
                msg = msg[1:]
            try:
                # print("Receive message:",str(msg,encoding='utf-8'))
                print("Receive message:", msg.decode(encoding))
            except:
                print("Receive message:", str(msg))


class TXA:
    def __init__(self, user_address, serial, sender_identifier='CC', communication_category='1', transfer_method='2',
                 encoding="gb2312"):
        self.sender_identifier = sender_identifier
        self.user_address = user_address
        self.communication_category = communication_category
        self.transfer_method = transfer_method
        self.serial = serial
        self.encoding = encoding

    def message(self, content, address='', encoding=''):
        if address == '':
            address = self.user_address
        if encoding == '':
            encoding = self.encoding

        message_temp = self.sender_identifier + 'TXA' + ',' + \
                  address + ',' + \
                  self.communication_category + ',' + \
                  self.transfer_method + ','
        message=bytes(message_temp,encoding)
        #if self.transfer_method=='2':
         #   message=message+b'\xA4'
        message=message+bytes(content,encoding)
        #if self.transfer_method == 2:
         #   message = 'A4' + message
        self.xor_checkSum = hex(XOR_CheckSum_string(message, encoding=encoding))[2:4]
        message = bytes('$',encoding) + message + bytes('*',encoding) + bytes(self.xor_checkSum,encoding) + bytes('\r\n',encoding)
        '''try:
            reslut = bytes(message, encoding=encoding)
        except:
            reslut = bytes(message)'''

        '''if self.transfer_method == 2:#'''
        #    '''reslut = b'\xA4' + reslut'''

        #return reslut
        return message

    def send(self, message):
        self.serial.write(message)

    def read(self):
        try:
            import _thread
            _thread.start_new_thread(read_serial, (self.serial, self.transfer_method, self.encoding,))
        except:
            import thread
            thread.start_new_thread(read_serial, (self.serial, self.transfer_method, self.encoding,))


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
    txa = TXA(user_address='0247718', serial=ser, transfer_method='2',encoding='gb2312')
    txa.read()

    '''test_msg=b'$CCTXA,0242407,1,2,A4B9E3D6DDBAA3C1C4BFC6BCBCD3D0CFDEB9ABCBBE*0F'
    print(test_msg)
    txa.send(message=test_msg)
    time.sleep(60)'''

    message = txa.message(content='3132333435')
    print(message)
    txa.send(message=message)
    time.sleep(60)

    message = txa.message(content='-3-132333435')
    print(message)
    txa.send(message=message)
    time.sleep(60)

    message = txa.message(content='-3--132333435')
    print(message)
    txa.send(message=message)
    time.sleep(60)

    message = txa.message(content='.3.132333435')
    print(message)
    txa.send(message=message)
    time.sleep(60)

    message = txa.message(content='.3..132333435')
    print(message)
    txa.send(message=message)
    time.sleep(60)

    message = txa.message(content='.-3.-13.2333435')
    print(message)
    txa.send(message=message)
    time.sleep(60)

    message = txa.message(content='.-3..--13.2333435')
    print(message)
    txa.send(message=message)
    time.sleep(60)

    message = txa.message(content='广州海聊科技..有限公--司12就3a给bc.-PM2.5-1.0CO-3.57')
    print(message)
    txa.send(message=message)
    time.sleep(60)

    # test()
8
