'''
Problem Statement: Multithreaded program to read an input file in chunks of -1KB, calculate its checksum and store it
in the output file in proper sequence.
'''

import threading
import hashlib

def cal_cksum(fp, fp1, lock):
    '''
    Function which reads input.txt file in 1KB chunk size and
    stores its checksum in output.txt file
    :param fp: File pointer to input.txt
    :param fp1: File pointer to output.txt
    :param lock: for synchronization
    :return: None
    '''

    #print("Thread name:", threading.current_thread().name)
    chunk = fp.read(1024)
    while chunk:
        lock.acquire()
        md5_cksum = hashlib.md5(chunk.encode('UTF-8')).hexdigest()
        fp1.write(md5_cksum)
        fp1.write("\n")
        lock.release()
        chunk = fp.read(1024)


if __name__ == "__main__":

    # input.txt => Input file to read the content
    fp = open("input.txt", mode='r')

    # output.txt => Output file to store the checksum
    fp1 = open('output.txt', mode='w')

    thread_list = []
    lock = threading.Lock()

    # Thread creation
    for i in range(1, 7):
        t = threading.Thread(target=cal_cksum, args=(fp, fp1, lock,), name='thread_' + str(i))
        thread_list.append(t)
    #print(thread_list)

    # Start the threads
    for t in thread_list:
        t.start()

    # Wait till all the threads finish the execution
    for t in thread_list:
        t.join()

    # Read checksum of each 1KB from output.txt file
    fp1 = open('output.txt', mode='r')
    print(fp1.read())

    # Close the input.txt and output.txt
    fp1.close()
    fp.close()


