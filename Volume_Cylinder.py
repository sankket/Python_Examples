#Find the Volume of the Cylinder.
class Volume:
    def __init__(self):
        self.a =1
        self.f=1
        self.c=1
    def volume(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
        print('Volume of Box is ',l*b*h)
vol = Volume()
vol.volume(4,6,8)
