import uuid
import random
import string
import time

def generate_uuid() -> str:
    return str(uuid.uuid4())

def generate_order_number() -> str:
    timestamp = int(time.time() * 1000)
    rand_chars = "".join(random.choices(string.ascii_uppercase, k=4))
    return f"ORD-{timestamp}-{rand_chars}"

def generate_sku(category: str, brand: str) -> str:
    cat_code = category[:3].upper()
    brand_code = brand[:3].upper()
    rand_num = random.randint(1000, 9999)
    return f"SKU-{cat_code}-{brand_code}-{rand_num}"

def generate_tracking_number(carrier: str = "FEDEX") -> str:
    carrier_prefix = carrier[:3].upper()
    rand_digits = "".join(random.choices(string.digits, k=12))
    return f"{carrier_prefix}{rand_digits}"
