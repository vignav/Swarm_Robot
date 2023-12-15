# Echo server program
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8000             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)

def get_data():
    data = conn.recv(1024)
    if data:
        return( [ float(i) for i in data.decode('ascii').split() ] )
    else:
        return([])

def close():
    conn.close()


if __name__ == '__main__':
    try:
        while 1:
            numbers = get_data()
            print(str(numbers[0]))
    except KeyboardInterrupt:
        close()

