import hashlib
from os.path import *

hashkart = "a63e16a1ac87c1b7156b1521adaf1133"
hashdriver = "72f9a387bd1bc3562691476706c71224"
def kart():
    if(exists("param/kartParam.bin")):
        curhashkart = hashlib.md5(open('param/kartParam.bin','rb').read()).hexdigest()
        return curhashkart

def driver():
    if(exists("param/driverParam.bin")):
        curhashdriver = hashlib.md5(open('param/driverParam.bin','rb').read()).hexdigest()
        return curhashdriver