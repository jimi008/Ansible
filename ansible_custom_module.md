we will have below playbook

```yml
- name: Test Jinja2 Templating
  hosts: webserver1
  tasks:
    - userdata: name=Gaurav age=18
```

By default, Ansible uses the modules from its default location. To make it use the custom module that you created, set the path of the module script by exporting it using below command:

```
export ANSIBLE_LIBRARY=/path/to/module/userdata.py
```
