**Ad-hoc Commands - Execute modules from the command line**
```
ansible webservers -m service -a "name=jenkins state=started"
ansible webservers -m ping
ansible webservers -m command -a "/sbin/reboot -t now"
```

From playbooks, Ansible modules are executed in a very similar way:

```
- name: reboot the servers
  command: /sbin/reboot -t now
```
