import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

passlen = int(input("Enter the length of password: "))

if passlen > len(s):  
    print(f"Error: Maximum password length can be {len(s)}.")
else:
    p = "".join(random.sample(s, passlen))
    print(f"Generated Password: {p}")