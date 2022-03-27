import random


def generate_ip():
    ip1 = str(random.randint(0, 255))
    ip2 = str(random.randint(0, 255))
    ip3 = str(random.randint(0, 255))
    ip4 = str(random.randint(0, 255))
    ip = (ip1 + '.' + ip2 + '.' + ip3 + '.' + ip4)
    return ip


result = generate_ip()
print(result)
