'''
python socket chat example
original author: Ankur Shrivastava
licence: GPL v3 

modified by Mike Capozzoli for Engineering 325 lab, the failed version is commented out and below this code
    -added more comments
    -included flag handling
    -incorporated user name and password
    -added auto setup IP address 
'''
#server
import socket
import threading
import time
SIZE = 4


#creating an instance of socket.  SOCK_STREAM designates a TCP/IP connection
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#getting the IP address of the raspberry pie

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
IPaddr = s.getsockname()[0]
s.close()

# binding to ip address 
soc.bind(( IPaddr  ,5432)) 
soc.listen(5)

class CThread(threading.Thread):
    def __init__(self,c):
        threading.Thread.__init__(self)
        self.conn = c
        self.stopIt=False

    def mrecv(self):
        data = self.conn.recv(SIZE)
        self.conn.send('OK')
        msg = self.conn.recv(int(data))
        return msg

    def run(self):
        while not self.stopIt:
            msg = self.mrecv()
            print 'recieved->  ',msg

def setConn(con1,con2):
    dict={}
    state = con1.recv(9)
    con2.recv(9)
    if state =='WILL RECV':
        dict['send'] = con1 # server will send data to reciever
        dict['recv'] = con2
    else:
        dict['recv'] = con1 # server will recieve data from sender
        dict['send'] = con2
    return dict

def msend(conn,msg):
    if len(msg)<=999 and len(msg)>0:
        conn.send(str(len(msg)))
        if conn.recv(2) == 'OK':
            conn.send(msg)
    else:
        conn.send(str(999))
        if conn.recv(2) == 'OK':
            conn.send(msg[:999])
            msend(conn,msg[1000:]) # calling recursive


(c1,a1) = soc.accept()
(c2,a2) = soc.accept()
dict = setConn(c1,c2)
thr = CThread(dict['recv'])
thr.start()
try:
    while 1:
        msend(dict['send'],raw_input())
except:
    print 'closing'
thr.stopIt=True
msend(dict['send'],'bye!!!')# for stoping the thread
thr.conn.close()
soc.close()






#'''
#Created on Nov 29, 2012
#
#@author: Mike
#'''
#import SocketServer
#import socket
#class MyTCPHandler(SocketServer.BaseRequestHandler):
#    """
#    The RequestHandler class for our server.
#
#    It is instantiated once per connection to the server, and must
#    override the handle() method to implement communication to the
#    client.
#    """
#    
#    
#    def handle(self):
#        print 'handle'
#        # self.request is the TCP socket connected to the client
#        self.data = self.request.recv(1024).strip()
#        print "{} wrote:".format(self.client_address[0])
#        print self.data
#        # just send back the same data, but upper-cased
#        self.request.sendall(self.data.upper())
#    def finish(self):
#        print 'finish'
#    
#    def setup(self):
#        print 'setup'
#        
#class ChatServer(MyTCPHandler) :
#    '''
#    classdocs
#    '''
#
#
#    def __init__(self):
#        '''
#        Constructor
#        '''
#        self.IP = socket.gethostbyname(socket.gethostname())
#        self.PORT = 9999
#        self.theServer = SocketServer.TCPServer((self.IP, self.PORT), MyTCPHandler)
#        self.CLIENTLIST = self.client_address
#    
#    def dothings(self):
#        while True:
#            self.theServer.serve_forever()
#
#    
#    def welcome(self):
#        for user in self.CLIENTLIST:
#            for client in self.theServer.RequestHandlerClass.client_address:
#                if user == client:
#                    
                    
                    
                
            
        
