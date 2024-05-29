import hashlib

# Example for user ID eq 3 and challenge ID eq 2
user_id=3
challenge_id=2

# Change this strings to your own (same as in CTFd instance)
string_1=b"String1"
string_2=b"String2"
string_3=b"String3"

# Generate flag and put it in the your CTF environment
flag_hash=hashlib.sha256(string_1+int(user_id).to_bytes(4, byteorder='big')+string_2+int(challenge_id).to_bytes(4, byteorder='big')+string_3).hexdigest()
print("flag{"+flag_hash+"}")