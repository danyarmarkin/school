def hex_xor(x, y):
    xi = int(x, 16)
    r = hex(xi ^ y)[2:]
    return "0" + r if len(r) < 2 else r


f = open("pic_v2.bmp", "rb")
out = open("out.bmp", "wb")

i = 0
while b := f.read(1):
    r = hex_xor(b.hex(), i)
    i += 1
    i %= 256
    out.write(bytes.fromhex(r))

out.close()
f.close()

