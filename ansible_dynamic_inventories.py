#!/usr/bin/python

'''
Ansible accepts any kind of executable file as an inventory file. Hence, you can build your own dynamic inventory the way you like, the only restriction is that you have to pass it to Ansible as JSON.
You could create an executable binary, a script, or anything else that can be run and will output JSON to stdout, and Ansible will call it with the argument --list when you run, as an example, ansible all -i my-inventory-script -m ping.
'''
import json
import argparse
def get_inventory_data():
    data =  {
      "database": {
          "hosts": ["sqlserver1"],
          "vars" : {
              "ansible_ssh_pass": "password",
              "ansible_ssh_host": "192.168.25.15"
           }
       }
    }
    return data
if __name__ == "__main__":
    data = get_inventory_data()
    #print(json.dumps(data))
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--host', action='store')
    arg = parser.parse_args()
    if arg and arg.list:
        print(json.dumps(data))
    elif arg.host:
        print(json.dumps({'_meta': {'hostvars': {}}}))
