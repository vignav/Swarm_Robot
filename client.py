# Echo client program
import time
import socket
import math

HOST = '127.0.0.1'    # The remote host
PORT = 8000              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def send( a_id , x1 ,y1 ,x2 ,y2 ,a1 ,a2 ):
    s_string = str(a_id) +' '+ str(x1) +' '+ str(x2) +' '+ str(y1) +' '+  str(y2) +' '+ str(a1) +' '+ str(a2)
    s.sendall(s_string.encode('ascii'))

def close():
    s.close()

if __name__ == '__main__':
    try:
        a = 1
        angle = -math.pi
        add = 0.5
        while 1:
            send( a,a*2,a*3,a*4,a*5,angle,angle )
            a = a+1
            angle = angle + add
            if ( angle > math.pi or angle < -math.pi ):
                add = -1 * add
                angle = angle - add
            time.sleep(1)

    except KeyboardInterrupt:
        close()

