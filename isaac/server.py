def run_server():
    """ The server that should be started when collecting data """
    # As of right now, a standalone tcp server, but will be intergrated with the agent.
    print("TCP Server Started...\nLooking for a connection...\nStart the Game (or Restart the mod it if it's running)")

    import socket
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 11

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    conn, addr = s.accept()
    print ('Connection address:', addr)

    return conn

def receive(conn):
    BUFFER_SIZE = 11
    data = conn.recv(BUFFER_SIZE)

    return data
