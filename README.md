# Fuzzer-Checker
Fuzzer Checker is a tool that try to check if the firewall allow the activation of fuzzer, like ffuf or dirb.

!WARNING, THIS TOOL CHECK, AFTER A SHORT FUZZ, IF THE DOMAIN/SUBDOMAIN STILL ALLOW YOU TO ENTER. SO THIS CHECK IF YOU HAVE BEEN BLOCKED!

Tip: use a VPN to not block your true IP

TO INSTALL

The first thing to do is install the requirements.txt

```sudo pip install requirements.txt```

After that you can run the command:

```sudo python3 fuzzer_checker --install```

this code will install ffuf and make a copy of the script and put it in the /usr/local/bin


WHY USE IT?

This tool was created for bug bounters, and it was created to help them to find subdomains and domains that are vulnerable to fuzz, or scanning

But keep in mind that the firewall can block you, so don't try using this tool without a VPN or other technique


HOW DOES IT WORKS?

This script only works with domains or subdomains that have 200 as status code.

Another thing to say is that this code will create a wordlist called *.wordlist_for_explorer*, this is a testing wordlists with numbers that goes from 0 to 199, so there is 200 lines.

First, the script checks the status code before the fuzzing, to make sure the code is 200.

Secondly, the ffuf will start fuzzing the website with the custom wordlist

After that, the script will check again the status code. If the status code modify to 404, the website blocked you. Else, they permit you to make fuzzing and execute scanners without direct restriction


MODIFICATIONS

The script is totally modificable, and you can "model" the code in the way you want


If you want to increase or decrease the workers number, you can try to find this line and modify the *workers* variable

![Captura de tela de 2025-02-08 18-51-18](https://github.com/user-attachments/assets/73cda3eb-0d22-4115-8d24-0b7b2914e05a)


If you want to incresa or decrese the wordlist size, you can try to find this line and modify the value

![Captura de tela de 2025-02-08 18-55-43](https://github.com/user-attachments/assets/17e1079d-d31f-4e20-8463-3a5d01413e06)

