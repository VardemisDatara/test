from struct import *
import pprint
import collections  

class data_handling:
    def __init__(self, *args, **kwargs):
        self.P = pack('hhh', 1, 2, 3)
        self.U = unpack('hhh', self.P)


test = data_handling()
print(test.P)
print(test.U) 
