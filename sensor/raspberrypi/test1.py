# coding=utf-8

def XOR_CheckSum_string(m_str, encoding="ascii"):
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

msg = b'\xb3\xb1\xb3\xb2\xb3\xb3\xb3\xb4\xb3\xb5'
print(msg)
print(str(msg))
print(msg.decode('GB18030').encode('utf-8'))
print(msg.decode('GBK'))
print(msg.decode('GB2312'))
print(msg.decode('utf-16'))
# print(msg.decode('utf-8'))

msg = b'\xB9\xE3\xD6\xDD\xBA\xA3\xC1\xC4\xBF\xC6\xBC\xBC\xD3\xD0\xCF\xDE\xB9\xAB\xCB\xBE'
print(msg.decode('GB2312'))

print("广州海聊科技有限公司".encode(encoding="gb2312"))
print(bytes("广州海聊科技有限公司", 'gb2312'))
print(b'\xA4' + bytes("广州海聊科技..有限公--司12就3a给bc.-", 'gb2312'))
print((b'\xA4' + bytes("广州海聊科技..有限公--司12就3a给bc.-", 'gb2312'))[1:])

# msg=b'\xb9\xe3\xd6\xdd\xba\xa3\xc1\xc4\xbf\xc6\xbc\xbc..\xd3\xd0\xcf\xde\xb9\xab--\xcb\xbe12\xbe\xcd3a\xb8\xf8bc.-'
msg = (b'\xA4' + bytes("广州海聊科技..有限公--司12就3a给bc.-", 'gb2312'))[1:]
print(msg.decode('GB2312'))

print(bytes("\xA4广州海聊科技有限公司", 'gb2312'))

test_msg=bytes("CCTXA,0242407,1,2,",'gb2312')+b'\xA4'+bytes("广州海聊科技有限公司", 'gb2312')
#test_msg=b'$CCTXA,0242407,1,2,A4B9E3D6DDBAA3C1C4BFC6BCBCD3D0CFDEB9ABCBBE*0F'
print(test_msg)
print(hex(XOR_CheckSum_string(test_msg)))

print(hex(XOR_CheckSum_string(bytes("CCTXA,0242407,1,2,",'utf-8')+bytes("0123456789ABCDEF", 'utf-8'))))
