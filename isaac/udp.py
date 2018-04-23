# Contains the logic for my udp server

def run_server():
    import socket

    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    sock.setblocking(0)

    return sock

def receive(sock):
    try:
        data,address = sock.recvfrom(11)
    except:
        pass
    else: 
        return data
