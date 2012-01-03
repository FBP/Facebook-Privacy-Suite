# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 16:37:54 2012

@author: - Chris Paulson
"""

import socket

host = 'localhost'
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.send('Hello World!')

print(s.recv(1024))