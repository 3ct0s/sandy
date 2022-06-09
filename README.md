<h1 align="center">
  <br>
  <a href="https://github.com/3ct0s/"><img src="https://upload.wikimedia.org/wikipedia/en/thumb/a/a0/Sandy_Cheeks.svg/1200px-Sandy_Cheeks.svg.png" width=400 weigth=500 alt="Disctopia"></a>
  <br>
  Sandy
  <br>
</h1>

<h4 align="center">Sandy the Sandbox Enumration Tool</h4>

<p align="center">
    <img src="https://img.shields.io/badge/Platform-Windows-purple">
    <img src="https://img.shields.io/badge/Version-1.0.0-purple">
    <img src="https://img.shields.io/badge/Python-3.5+-purple">
</p>

---

## What is Sandy?

Sandy is a Sandbox Enumeration tool that can be used to extract information from a sandbox virtual machine. All of the info gets packaged in a TXT file which then gets send to the user with the use of **Discord Webhooks**

*/!\ Keep in mind that the tool will only work on sandboxes that allows web traffic to reach its destination*

## Sandy Features:

### It will extract a list of the following:
- All the running processes
- Operating System Version
- CPU Model
- Hostname
- Installed Software
- UAC Status
- Screenshot of the desktop

## How to use Sandy?

You will need to edit the main.py script and add your own Discord Webhook URL. Then you will need to package the script manually into an EXE with the use of tools like PyInstaller, Py2Exe, PyArmor, Nuitka etc.

The last thing you have to do is to upload the EXE into any sandbox analysis environment you want. If the sandbox environment allows web traffic to normally reach its destination, then Sandy will extract the information and send it to the user.