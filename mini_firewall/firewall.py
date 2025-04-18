#firewall simulator
import random
from time import sleep


def random_ip():
    return f"192.168.1.{random.randint(1,20)}"

white_listed=[
    "192.168.1.1","192.168.1.3","192.168.1.5","192.168.1.7","192.168.1.9"
]


for _ in range(10):
    ip=random_ip()
    if ip in white_listed:
        print(f"{ip} is Allowed..")
    else:
        print(f"{ip} is Not Allowed")
    sleep(10)