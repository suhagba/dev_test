"""
Write some code to print the SHA256 hash of the string "This is a string"
"""
from hashlib import sha256

s = "This is a string"

# Your code goes here
hash_object = sha256(s.encode('utf-8'))
hex_dig = hash_object.hexdigest()
print("SHA256 hash of string is",hex_dig)