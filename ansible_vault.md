To encrypt the inventory file with Ansible Vault, run the below command:
```
$ansible-vault encrypt inventory.txt --output enc_inven.txt
```
Viewing encrypted file
```
ansible-vault view enc_inven.txt
```
Running Ansible with Vault-Encrypted Files
```
ansible-playbook -i enc_inven.txt playbook.yml --ask-vault-pass
```
