# Python implementation to
# read last N lines of a file
from time import time

# Function to read
# last N lines of the file
def LastNlines(fname, N):
    # opening file using with() method
    # so that file get closed
    # after completing work
    with open(fname) as file:
        
        # loop to read iterate
        # last n lines and print it
        for line in (file.readlines() [-N:]):
            print(line, end ='')

# importing os module
import os

# Function to read
# last N lines of the file
def LastNlines2(fname, N):
    # taking buffer size of 8192 bytes
    bufsize = 8192
    print("b")
    # calculating size of
    # file in bytes
    fsize = os.stat(fname).st_size
    
    iter = 0
    
    # opening file using with() method
    # so that file get closed
    # after completing work
    with open(fname) as f:
        print(bufsize)
        print(fsize)
        if bufsize > fsize:
            
            # adjusting buffer size
            # according to size
            # of file
            bufsize = fsize-1
            print("c")
            # list to store
            # last N lines
            fetched_lines = []
            
            # while loop to
            # fetch last N lines
            while True:
                iter += 1
                
                # moving cursor to
                # the last Nth line
                # of file
                f.seek(fsize-bufsize * iter)
                
                # storing each line
                # in list upto
                # end of file
                fetched_lines.extend(f.readlines())
                print("a")
                # halting the program
                # when size of list
                # is equal or greater to
                # the number of lines requested or
                # when we reach end of file
                if len(fetched_lines) >= N or f.tell() == 0:
                        print(''.join(fetched_lines[-N:]))
                        break

# Function to read
# last N lines of the file
def LastNlines3(fname, N):
    # taking buffer size of 8192 bytes
    bufsize = 8192
     
    # calculating size of
    # file in bytes
    fsize = os.stat(fname).st_size
     
    iter = 0
     
    # opening file using with() method
    # so that file get closed
    # after completing work
    with open(fname) as f:
        if bufsize > fsize:
            # adjusting buffer size
            # according to size
            # of file
            bufsize = fsize-1
             
            # list to store
            # last N lines
            fetched_lines = []
             
            # while loop to
            # fetch last N lines
            while True:
                iter += 1
                 
                # moving cursor to
                # the last Nth line
                # of file
                f.seek(fsize-bufsize * iter)
                 
                # storing each line
                # in list upto
                # end of file
                fetched_lines.extend(f.readlines())
                 
                # halting the program
                # when size of list
                # is equal or greater to
                # the number of lines requested or
                # when we reach end of file
                if len(fetched_lines) >= N or f.tell() == 0:
                        print(''.join(fetched_lines[-N:]))
                        break

# Driver Code:
if __name__ == '__main__':
    fname = 'filefull.txt'
    N = 3
    try:
        t=time()
        LastNlines(fname, N)
        print(f"\nTime taken: {time()-t}")
    except:
        print('File not found')
print("début")
t=time()
import os
with open("filefull.txt", "rb") as file:
    file.seek(-2, 2)
    for i in range(3):
        while file.read(1) != b'\n':
            file.seek(-2, 1) 
        print(file.readline().decode())
print("fin")
print(f"\nTime taken: {time()-t}")
