#! /usr/bin/python
# coding:utf-8
import SocketServer
import subprocess
import time

class MyTcpServer(SocketServer.BaseRequestHandler):
        def recvfile(self, filename):
                print "starting recieve file\n"
                f = open(filename,'wb')
                self.request.send("ready")
                while True:
                        data = self.request.recv(4096)
                        if data == 'EOF':
                                print "recv file success!"
                                break
                        f.write(data)
                f.close()
