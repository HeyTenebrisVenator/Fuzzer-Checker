#!/usr/bin/env python3
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import os






def fetch_url(url, output):   
    url = url.replace('\n', '')
    domain = url.replace('https://', '').replace('http://', '').split('/')[0]
    status_code = requests.get(url).status_code




    #check if we have been blocked
    if status_code == 200:
        os.system(f'sudo ffuf -w .wordlist_for_explorer -u {url}/FUZZ')
        status_code = requests.get(url + '/TESTING_IF_THERE_IS_A_FIREWALL').status_code
        if status_code == 404:
            print(f'{url} - BLOCKED')
        elif status_code == 403:
            print(f'{url} - OK')
            open(output, 'a').write('\n' + url)

         

def start_script():
    #check
    try:
        wordlist = open('.wordlist_for_explorer', 'r').readlines()
    except:
        print('Wordlist not found. Creating one .wordlist_for_explorer')
        data = open('.wordlist_for_explorer', 'a')
        index = 0
        while index < 200:
            index += 1
            data.write(f'{index}\n')
        data.close()
        wordlist = open('.wordlist_for_explorer', 'r').readlines()
    output = ''
    save = ''
    args = sys.argv[1:]
    if not args:
            help_command()
            sys.exit(1)
    if '-o' not in args or '--output' not in args:
            output = 'FUZZABLE'
    val = 0
    for arg in args:
            if arg.startswith("--") or arg.startswith("-"):
                option_name = arg[2:] if arg.startswith("--") else arg[1:]
                if option_name == "help" or option_name == "h":
                    help_command()
                    sys.exit(0)
                elif option_name == "list" or option_name == "l":
                    try:
                        list_of_dir = args[val + 1]
                        list_of_dir = open(list_of_dir, 'r', encoding="ISO-8859-1").readlines()
                    except Exception as e:
                        print(f"Error: Could not open file {save}: {e}")
                        sys.exit(1)
                elif option_name == "output" or option_name == "o":
                    try:
                        output = args[val + 1]
                        open(output, 'w').write('')
                    except Exception as e:
                        print(f"Error: Could not open file {save}: {e}")
                        sys.exit(1)
                elif option_name == "install":
                     os.system('sudo apt-get install -y ffuf')
                     os.system('sudo cp fuzzer_checker.py /usr/local/bin/fuzzer_checker; sudo chmod 777 /usr/local/bin/fuzzer_checker')
                     sys.exit(1)
                else:
                    print(f"Unknown option: {option_name}")
                    sys.exit(1)
            val = val + 1
    attack(list=list_of_dir,output=output)



def help_command():
    print("Usage: %s [options]")
    print("Options:")
    print("  -h, --help           Display this help message")
    print("  -l, --list           Path to the list of directories")
    print("  -o, --output         Path to the save output file")
    print("  --install            Install ffuf and put the explorer.py to /usr/local/bin")


def attack(list, output):
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(fetch_url, url, output): url for url in list}
        for future in as_completed(future_to_url):
            url = future_to_url[future]  

start_script()
