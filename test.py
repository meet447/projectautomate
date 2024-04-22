import random
import string

def generate_device_id(length=21):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

device_id = generate_device_id()  

print(device_id)