import os
import sys
import socket

HOSTS_FILE = '/etc/hosts'

def add_entry(file, ip_address, website):
    file.write(f'{ip_address} {website}\n')

def block_website(website):
    with open(HOSTS_FILE, 'a') as file:
        if website.startswith("www."):
            root_domain = website[4:]
        else:
            root_domain = website
            website = f"www.{website}"
        
        add_entry(file, '127.0.0.1', website)
        add_entry(file, '127.0.0.1', root_domain)
        add_entry(file, '::1', website)
        add_entry(file, '::1', root_domain)
    print(f'Blocked {root_domain} and {website}')

def unblock_website(website, hosts_content):
    new_content = [line for line in hosts_content if not line.strip().endswith(f' {website}')]
    with open(HOSTS_FILE, 'w') as file:
        file.writelines(line + '\n' for line in new_content)
    print(f'Unblocked {website}')

def main():
    if os.geteuid() != 0:
        sys.exit('Please run this script as root.')

    action = input('Enter "block" to block websites or "unblock" to unblock websites: ').lower()

    if action not in ('block', 'unblock'):
        sys.exit('Invalid action. Please enter either "block" or "unblock".')

    with open('blocked_websites.txt', 'r') as file:
        blocked_websites = [line.strip() for line in file]

    with open(HOSTS_FILE, 'r') as file:
        hosts_content = file.readlines()

    for website in blocked_websites:
        if action == 'block':
            block_website(website)
        elif action == 'unblock':
            unblock_website(website, hosts_content)

    os.system('dscacheutil -flushcache')

if __name__ == '__main__':
    main()

