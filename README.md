##README
This repository contains a collection of scripts to deploy and test a secure Apache web server using Ansible and to validate credit card numbers using Python.

#Prerequisites
Ansible installed on your control node.
Python 3.x installed on your local machine.
SSH access to your web server.
Repository Contents
deploy_web_server.yml - An Ansible playbook to install and configure an Apache web server with SSL and firewall settings.

test_web_server.yml - An Ansible playbook to test the configuration of the deployed web server.

credit_card_validation.py - A Python script to validate credit card numbers according to certain rules.

Setup & Running
Apache Web Server
Make sure your server details are correctly set up in Ansible's inventory hosts file.

Run the Ansible playbook to set up the web server:

bash
Copy code
ansible-playbook -i hosts deploy_web_server.yml
Run the Ansible playbook to test the web server:

bash
Copy code
ansible-playbook -i hosts test_web_server.yml
Credit Card Validation
You can directly run the Python script as follows:

bash
Copy code
python3 credit_card_validation.py
Enter the number of credit cards to check followed by the credit card numbers when prompted.

Notes
The scripts provided are basic examples and should be modified according to your specific use cases. They may lack some features necessary for a production environment.
Remember, using a self-signed certificate for the web server will cause a security warning to be displayed in the user's web browser.
Credit card validation is done based on the rules provided and does not check whether a credit card number actually exists.
