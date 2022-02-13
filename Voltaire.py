from selenium import webdriver
import time
import json
import os
from selenium.webdriver.common.by import By
import subprocess
import difflib
import re
from urllib.parse import unquote
from colorama import *

class Voltaire:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        ch_output = subprocess.Popen(["chromedriver"])
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(1)

    def Header(self):
        os.system('cls')

        print(f"""
{Fore.GREEN}__   __   _ _        {Fore.RED}_{Fore.GREEN}         
\ \ / /__| | |_ __ _{Fore.RED}(_){Fore.GREEN}_ _ ___ 
 \ V / {Fore.WHITE}_{Fore.GREEN} \ |  _/ {Fore.WHITE}_{Fore.GREEN}` | | '_/ -_)
  \_/\___/_|\__\__,_|_|_| \___|{Fore.RESET} [{Fore.RED}solved{Fore.RESET}]
""")

        self.par = input(f' [{Fore.GREEN}*{Fore.RESET}] Supérieur / Excellence ? => ')
        self.nb = input(f' [{Fore.GREEN}*{Fore.RESET}] Test number => ')

        try:
            int(self.nb)
            pass
        except ValueError:
            print(f' [{Fore.RED}!{Fore.RESET}] INT is required !')
            time.sleep(3.5)
            self.Header()

    def solver(self):
        data_filename = f"Module{self.nb}.txt"

        directory = f"./src/{self.par}/"
        reponses = []

        for filename in os.listdir(directory): #Credit => https://github.com/sylvain-reynaud/projet-voltaire-solver
            if filename.endswith(data_filename):
                with open(directory + filename, 'r', encoding="utf-8") as f:
                    data = f.read()
                    try:
                        data = data[data.index("[\"java.util.ArrayList"):data.index("]")] + "]"
                        data = data.replace("\\", "\\\\")
                        reponses += json.loads(data)
                    except:
                        pass
        reponses = [x for x in reponses if "\\x3C" in x]

        input(f' [{Fore.GREEN}*{Fore.RESET}] Ready ? (Enter to start)')
        print(f' [{Fore.GREEN}*{Fore.RESET}] Test 7 Started with 1 attempt every 5 seconds !')

        while True:
            try:
                time.sleep(5)
                items = self.driver.find_elements(By.XPATH, "/html/body/div[5]/div[2]/div[3]/div/div[1]/div/div/div[2]/div")
                for item in items:
                    phrase = item.text

                possibilites = difflib.get_close_matches(phrase, reponses)
                if len(possibilites) != 0:
                    toPrint = re.sub(r"<B>(.*)<\/B>", fr"{Fore.GREEN}\1{Fore.RESET}", unquote(possibilites[0].replace("\\x", "%")))
                    print(f' [{Fore.GREEN}*{Fore.RESET}]', toPrint)
        
                else:
                    print(f' [{Fore.GREEN}*{Fore.RESET}] Il n\'y a pas de faute')
                    self.driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/button").click()
                    self.driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[3]/div/div[3]/div[2]/button").click()
                    
            except:
                print(f' [{Fore.RED}*{Fore.RESET}] Attempt Failed !')

Voltaire_solved = Voltaire()
Voltaire_solved.Header()
Voltaire_solved.solver()