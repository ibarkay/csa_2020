

OUTFILE="output.txt"
key = "xor"

fin = open('xor-with-xor.bin', "rb")
x = fin.read()
l = len(x)
key = key * (l/len(key))

o = ""
index = 0
for item in x:
    o += chr(ord(item) ^ ord(key[index]))
    index = (index + 1)%len(key)

fin.close()
fout = open(OUTFILE, "w")
fout.write(o)
fout.close()