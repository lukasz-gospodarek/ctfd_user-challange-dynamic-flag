# ctfd_user-challange-dynamic-flag

CTFd Dynamic flag by user ID &amp; chalange ID

## Description

Code modification allows you to generate dynamic flags by user id and challange id.

## Instruction

1. clone CTFd GitHub repository
2. change directory to **CTFd** `cd CTFd`
3. in file `CTFd/api/v1/challenges.py` replace line (2x)

```
status, message = chal_class.attempt(challenge, request)
```

to line

```
status, message = chal_class.attempt(challenge, request, user)
```

4. in file `CTFd/plugins/challenges/__init__.py`

- replace line

```
def attempt(cls, challenge, request):
```

to line

```
def attempt(cls, challenge, request, user):
```

- add block of code after `flags = Flags.query.filter_by(challenge_id=challenge.id).all()`

```
        user_id=int(user.id)
        import hashlib
        string_1=b"String1"
        string_2=b"String2"
        string_3=b"String3"
        flag_hash=hashlib.sha256(string_1+int(user_id).to_bytes(4, byteorder='big')+string_2+int(challenge.id).to_bytes(4, byteorder='big')+string_3).hexdigest()
        if submission=="flag{"+flag_hash+"}":
            return True, "Correct"
```

## Script
You can just execute automated script

## Generate flag
After this steps you don't have to add flag to the challange. You can just generate and add flag to your CTF environment. It will be validated for the specific:
 - Strings (3x)
 - user id
 - challange id
