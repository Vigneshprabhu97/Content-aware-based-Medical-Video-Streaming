# -*- coding: utf-8 -*-
"""
Created on Mon May 20 13:34:13 2019

@author: tvign
"""

import socket                   # Import socket module
import time
import os
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port=8080
t1 = time.time()
s.connect((host,port))
print("Decoding of Encoded Data")
print("Connected....")
t2 = time.time()
file=open("trans.png",'wb')
file_data=s.recv(16777216)
file.write(file_data)
t3 = time.time()
file.close()
print (file_data)
print ('Total:', t3 - t1)
print ('Throughput:', round((1024.0 * 0.001) / (t3 - t1), 3),'K/sec.')
print("File received")
