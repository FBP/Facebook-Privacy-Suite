# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 16:37:54 2012

@author: - Chris Paulson
"""

import socket

host = 'fbp.servebeer.com'
port_encrypt = 1234
port_decrypt = 1235

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port_encrypt))
s.send('Vera is SUPER hot!!!')

recieved = s.recv(1024)
print 'Encrypted: ', recieved

##
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((host,port_decrypt))
s1.send(recieved)

print 'Decrypted: ', s1.recv(1024)