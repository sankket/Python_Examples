# Getting IP address using socket library in python.
import socket
add1=socket.gethostbyname("www.google.com")
add2=socket.gethostbyname("www.yahoo.com")
print(add1,"\t", add2)
