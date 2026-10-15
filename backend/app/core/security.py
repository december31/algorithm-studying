import hashlib
import hmac
import os
import secrets
from typing import Tuple


def hash_incantation(incantation: str) -> str:
    """Hash a secret incantation (password) using PBKDF2-HMAC-SHA256 with a salt."""
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac("sha256", incantation.encode("utf-8"), salt, 100_000)
    return f"{salt.hex()}${key.hex()}"


def verify_incantation(plain_incantation: str, stored_hash: str) -> bool:
    """Verify a secret incantation against the stored salt$hash."""
    try:
        salt_hex, key_hex = stored_hash.split("$")
        salt = bytes.fromhex(salt_hex)
        expected_key = bytes.fromhex(key_hex)
        actual_key = hashlib.pbkdf2_hmac("sha256", plain_incantation.encode("utf-8"), salt, 100_000)
        return hmac.compare_digest(expected_key, actual_key)
    except Exception:
        return False


def generate_hero_token() -> str:
    """Generate a cryptographically secure token for the hero session."""
    return f"hero_{secrets.token_urlsafe(32)}"
