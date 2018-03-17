from struct import *
import pprint
import collections  

P = pack('hhh', 1, 2, 3)
U = unpack('hhh', P)

print(P)
print(U) 
