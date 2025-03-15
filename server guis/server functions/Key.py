import random
import string
def generate_license_key():
    segments = [''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(4)]
    return '-'.join(segments)