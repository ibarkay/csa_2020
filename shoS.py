
from pwn import *
import sys
import os
import zlib

flag = open('fl4g.jpg','wb')
key = "CSA"
host = '52.28.255.56'
port =  1080
s = remote(host,port)

while True:
    try:

        s.send("\x5a\x01\xfe\xdd\x74\x9c\x2e") #greeting packet
        r = s.recv()  #server respone
        re = r.encode('hex')
        chary = r[2]
        toXor = r[3:6] #the bytes that we need to xor and send to server

        o = ''
        index = 0
        for item in toXor: # Xoring...
            o += chr(ord(item) ^ ord(key[index]))
            index = (index + 1) % len(key)
        print "server respone : " + re
        print "Toxor : "+ toXor.encode('hex')
        print "Xored with CSA : "+ o.encode('hex')
        print "magic byte : " + chary.encode('hex')

        toCheck =b"\x5a"+chary+o
        checksum =  hex(zlib.crc32(toCheck) & 0xffffffff) #CRC32 checksum
        def checksumy(): 
            s = checksum[2:]
            o = []
            while s:
                o.append(s[:2])
                s = s[2:]
            cheky = ''
            for i in o:
                cheky += chr(int("0x{}".format(i), 16))
            #print cheky
            return cheky

        s.send("\x5a" + chary + o +checksumy())
        s.send("\x5a\x01\x00\x01\xc0\xa8\xad\x14\x00\x50\x62\x4A\x30\x63") #addres to conect - with 4bytes checksum

        print s.recv()
        s.send('474554202f466c61672e6a706720485454502f312e310d0a557365722d4167656e743a204d6f7a696c6c612f352e30202857696e646f7773204e542031302e303b2057696e36343b2078363429204170706c655765624b69742f3533372e333620284b48544d4c2c206c696b65204765636b6f29204368726f6d652f37342e302e333732392e313639205361666172692f3533372e33360d0a486f73743a207777772e7475746f7269616c73706f696e742e636f6d0d0a4163636570742d4c616e67756167653a20656e2d75730d0a436f6e6e656374696f6e3a204b6565702d416c6976650d0a0d0a'.decode('hex'))
        #above is GET HTTP req in hex (for Flag.jpg on the server)
	data = ''
        while True:
            #flag.write(s.recv())
            data += s.recv(1024)

    except EOFError as error:
        print(error)
        flag.write(data)
        exit()
