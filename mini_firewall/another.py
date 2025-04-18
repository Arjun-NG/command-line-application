import random
import time
from time import sleep


def random_ip():
    return f"192.168.1.{random.randint(1,20)}"

def action_rules(ip,rules):
    for rule_ip,action in rules.items():
        if ip == rule_ip :
            return action
    return "Allow"


def main():
    print("MINI FIREWALL SIMULATOR")
    print("************************")
    firewall_rules ={
        "192.168.1.1":"block",
        "192.168.1.3":"block",
        "192.168.1.5":"block",
        "192.168.1.7":"block",
        "192.168.1.9":"block"
    }

    for _ in range(20):
        ip=random_ip()
        action=action_rules(ip,firewall_rules)
        random_number=random.randint(0,9999)
        print(f"{ip}  is {action}  and the instance is {random_number}")
        sleep(1)

if __name__=="__main__":
    main()