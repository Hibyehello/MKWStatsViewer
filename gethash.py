import hashlib

print(hashlib.md5(open('param/driverParam.bin','rb').read()).hexdigest())