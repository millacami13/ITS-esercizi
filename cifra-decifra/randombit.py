import sys
import random

if len(sys.argv) != 2:
    print (f"Usage: {sys.argv[0]} <file name>")
    sys.exit(1)

#Ora devo leggere il file binario
data = None
with open(sys.argv(1), "rb") as f:
    data = f.read()    

#Ora in data ho il binario del file (16 byte)
#Scelgo quale byte modificare
pos = random.randint(0, len(data)-1)

byte = data(pos)

#Ora scelgo quale bit di byte modificare
bit = random.randint (0,7)
mask = 1 << bit

byte = byte ^ mask

data = data [:pos] + bytes([byte]) + data [pos +1:]

with open (sys.argv[1], "wb") as f:
    f.write(data)

print (f"Ho modificato il bit {bit} del byte al posto {pos} nel file {sys.argv[1]}")    