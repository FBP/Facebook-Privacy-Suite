# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 15:52:38 2012

@author: Chris Paulson
"""

## This is a simple server for encryption protocol testing, it's built on twisted. Currently, it'll echo any tcp data recieved on port 1234

from twisted.internet import protocol, reactor
from Crypto.Cipher import Blowfish
from multiprocessing import Process
import binascii

class EncryptEcho(protocol.Protocol):
    def dataReceived(self,data):
            encdec = encrypt_decrypt('This is a key gsdgsgdfggd')
            print 'Recieved: ',data
            sent_data = encdec.text_encrypt(data)
            print 'Returned: ', sent_data 
            self.transport.write(sent_data)
 
class EncryptFactory(protocol.Factory):
    def buildProtocol(self,addr):
            return EncryptEcho()
            
            
class DecryptEcho(protocol.Protocol):
    def dataReceived(self,data):
            encdec = encrypt_decrypt('This is a key gsdgsgdfggd')
            print 'Recieved: ',data
            sent_data = encdec.text_decrypt(data)
            print 'Returned: ', sent_data 
            self.transport.write(sent_data)
 
class DecryptFactory(protocol.Factory):
    def buildProtocol(self,addr):
            return DecryptEcho()
            
class encrypt_decrypt():
    def __init__(self, key):
        self.obj = Blowfish.new(key, Blowfish.MODE_ECB)
        
    def text_encrypt(self,message):
        while len(message)%8!=0:
            message += ' '
        return binascii.b2a_base64(self.obj.encrypt(message))
    
    def text_decrypt(self,encmsg):
        return self.obj.decrypt(binascii.a2b_base64(encmsg))
    
    
    
if __name__ == '__main__': 
    reactor.listenTCP(1234,EncryptFactory())
    reactor.listenTCP(1235,DecryptFactory())
    reactor.run()