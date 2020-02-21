
'''
Client side for Backup/restore program
'''

import socket


def backup(s, filename):

    '''
    Function to backup the file
    :param s: socket object
    :param filename: file to be backed up
    :return: None
    '''

    with open(filename, 'rb') as fp:
        chunks = fp.read(1024)
        while chunks:
            s.send(chunks)
            print("sent", repr(chunks))
            chunks = fp.read(1024)

    print("Done sending the file")


def restore(s):

    '''
    Function to restore the file from server
    :param s: socket object
    :return: None
    '''

    with open('received_file1', 'wb') as fp1:
        print("File opened")
        while True:
            print("Receiving data..")
            data = s.recv(1024)
            print("Data:", data)
            if not data:
                break
            fp1.write(data)

    print("Done receiving the file")

if __name__ == "__main__":

    try:
        s = socket.socket()
        print("Socket created successfully")
    except socket.error as err:
        print("Socket creation failed with error ", err)

    port = 1443
    # host_ip = '172.16.37.70'
    host_ip = socket.gethostname()
    print(host_ip)
    s.connect((host_ip, port))
    s.send(b"Hello from Client!")

    print("Choose any option:\n1. Backup\n2. Restore\n")
    option = int(input())
    if option == 1:
        s.send(b"Backup")
        backup(s, 'a.txt')
    elif option == 2:
        s.send(b"Restore")
        restore(s)
    else:
        print("Invalid option")

    s.close()
