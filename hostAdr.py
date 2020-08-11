# Getting the host address program in python.
import socket
#gets host address By follwing Method
add1=socket.gethostbyaddr("216.58.203.132")
add2=socket.gethostbyaddr("106.10.250.10")
print("The Address is Of:",add1)
print("The Address is Of:",add2)
