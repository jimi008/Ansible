```ini
webserver1 ansible_host=192.168.25.15 ansible_ssh_pass=password ansible_connection=ssh ansible_port=22 ansible_user=root
webserver2 ansible_host=192.168.25.17 ansible_ssh_pass=password ansible_connection=ssh ansible_port=22 ansible_user=root
webserver3 ansible_host=192.168.25.18 ansible_ssh_pass=password ansible_connection=ssh ansible_port=22 ansible_user=root

sqlserver1 ansible_host=192.168.25.19 ansible_ssh_pass=password ansible_connection=ssh ansible_port=22 ansible_user=root
sqlserver2 ansible_host=192.168.25.20 ansible_ssh_pass=password ansible_connection=ssh ansible_port=22 ansible_user=root
sqlserver3 ansible_host=192.168.25.21 ansible_ssh_pass=password ansible_connection=ssh ansible_port=22 ansible_user=root

nfsserver1 ansible_host=192.168.25.19 ansible_ssh_pass=password ansible_connection=ssh ansible_port=22 ansible_user=root
nfsserver2 ansible_host=192.168.25.20 ansible_ssh_pass=password ansible_connection=ssh ansible_port=22 ansible_user=root
nfsserver3 ansible_host=192.168.25.21 ansible_ssh_pass=password ansible_connection=ssh ansible_port=22 ansible_user=root


[webservers]
webserver1
webserver2
webserver3


[dbservers]
dbserver1
dbserver2
dbserver3


[nfsservers]
nfsserver[1:3]

[production:children]
webservers
dbservers

```

When we run below command it will ping all the webservers and dbserver that are present in group_inventory.txt file.
```sh
$ansible production -m ping -i inventory_all.txt`
```
