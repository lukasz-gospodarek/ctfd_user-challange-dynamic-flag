user_id=3
challenge_id=2

string_1=b"String1"
string_2=b"String2"
string_3=b"String3"

import hashlib
flag_hash=hashlib.sha256(string_1+int(user_id).to_bytes(4, byteorder='big')+string_2+int(challenge_id).to_bytes(4, byteorder='big')+string_3).hexdigest()
print("flag{"+flag_hash+"}")