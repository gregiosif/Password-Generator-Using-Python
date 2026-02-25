"""
Password Generator Using Python
Copyright 2026 Grigorios Iosifidis
Licensed under the Apache License, Version 2.0
See LICENSE file for details.
"""

import secrets
import string

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

password = generate_password(16)
print("Secure Password:", password)
