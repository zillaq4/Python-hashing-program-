
import hashlib
import os

print("#######This program is used to hash a text using hashlib python function combining sha256 + a salt  #####")

salt = os.urandom(16)

text_to_hash = input("Enter the text you want hashed>>>>")


print(hashlib.sha256((salt+text_to_hash.encode())).hexdigest())

print("|\n"
        "||\n"
        "|||\n"
        "||||\n")
print("######Thank you for using me####")


