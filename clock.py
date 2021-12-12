from os import times_result
from pickletools import int4
import socket
import struct
import time
from unicodedata import decimal
from xml.etree.ElementPath import _T

def RequestTimefromNtp(addr='0.de.pool.ntp.org'):
    REF_TIME_1970 = 2208988800  # Reference time
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = b'\x1b' + 47 * b'\0'
    client.sendto(data, (addr, 123))
    data, address = client.recvfrom(1024)
    t = int
    if data:
        
        t = struct.unpack('!12I', data)[10]
        t -= REF_TIME_1970
    return time.time(t), t

if __name__ == "__main__":
    print(RequestTimefromNtp())