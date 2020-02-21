'''
Server side for Backup/restore program
'''

import socket


def backup(conn):
    '''
    Backup function to backup the file sent by the client
    :param conn: connection object
    :return: None
    '''

    with open('received_file', 'wb') as fp1:
        print("File opened")
        while True:
            print("Receiving data..")
            data = conn.recv(1024)
            print("data", data)
            if not data:
                break
            fp1.write(data)

    print("Successfully backed up the file")

def restore(conn, filename):
    '''
    Function to restore file to client
    :param conn: connection object
    :param filename: file to be restored
    :return: None
    '''

    with open(filename, 'rb') as fp:
        chunks = fp.read(1024)
        while chunks:
            conn.send(chunks)
            print("sent", repr(chunks))
            chunks = fp.read(1024)

    print("Successfully restored the file")


if __name__ == "__main__":

    # Socket Creation and bind
    try:
        s = socket.socket()
        print("Socket created successfully")
    except socket.error as err:
        print("Socket creation failed with error ", err)

    port = 1443
    # host_ip = '172.16.37.70'
    host_ip = socket.gethostname()
    s.bind((host_ip, port))
    s.listen(5)

    print("Server is in listen mode..\n")

    conn, addr = s.accept()
    print("Connected to client", addr)
    data = conn.recv(1024)
    print("Server received the data", data)

    option = conn.recv(1024)
    if option == b"Backup":
        backup(conn)
    elif option == b"Restore":
        restore(conn, 'received_file')

    conn.close()
    print("Successfully closed the connection")


