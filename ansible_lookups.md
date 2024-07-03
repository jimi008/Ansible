Consider below inventory file without password details:

```ini
webserver1 ansible_host=192.168.25.15
sqlserver1 ansible_host=192.168.25.16

[webservers]
webserver1

[databaseservers]
sqlserver1

[web_database_servers]
webserver1
sqlserver1
```

Store the password details in .csv format file as follows:
```csv
Hostname,Password
webserver1,password
sqlserver1,password
```
use the lookup file in our playbook

```yml
- name: Test Connectivity
  hosts: webserver1
  vars:
    ansible_ssh_pass: "{{ lookup('csvfile', 'webserver1 file=credentials.csv delimiter=,') }}"
  tasks:
    - name: create a dummy file on webserver
      command: touch /tmp/csv_lookups.txt
```
