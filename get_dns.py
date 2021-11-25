# Importing the dns address of the website.
import socket
add1=socket.gethostbyname("www.infosys.com")
add2=socket.gethostbyname("www.microsoft.com")
print(add1,"\t", add2)
