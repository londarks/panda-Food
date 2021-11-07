import sqlite3
from hashlib import sha1
import hmac
import time
import base64

class Controller():    
    def _encryption(self, raw:str)-> str:
        """Generation HASH password"""
        key = b"AHteQGy0_P2fcvbMBuF5NGxYVFPlWq0m6hgDgW53"
        
        hashed = hmac.new(key, raw.encode("utf-8"), sha1)
        
        # The signature
        return base64.encodebytes(hashed.digest()).decode('utf-8')
    