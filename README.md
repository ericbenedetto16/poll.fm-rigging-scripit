SiLive hosts their Polls with poll.fm which fails to use a ReCaptcha for verification. Although there is a limit on polls per 20-30 minute span, using Selenium in multiple instances on different machines, or with proxies allows for a flood of votes and poll rigging. I have used this and successfully swayed polls.

Prerequisites:
- Python
- Selenium
- Google Chrome
- ChromeDriver (for your version of Google Chrome)

How To Use:
1. Open script.py in your text editor of choice.
2. Find the poll.fm URL by disabling JavaScript on the SiLive poll page and following Step 2.
3. Inspect the link that redirects you to the Poll and copy the poll.fm URL.
4. Replace POLL_URL with this url you just copied.
5. Find the option you want the program to select and Inspect the Radio Element.
6. Once the Inspector is open on the Radio Element, find the parent or child element whose ID starts with PDI_answer.
7. Copy this ID and replace POLL_ANSWER_ID with this ID.
8. In Terminal or Command Prompt, cd to the Directory where you have this script saved locally.
9. Run 'python script.py' in the directory and let the program run.

Warnings:
- ChromeDriver has a TimeOut and after some hours of running (not sure exactly how many), the script stops running. There is a possibility to add a Try/Catch statement to keep the script running, but for now you have to manually restart it by writing the command 'python script.py' again in your local directory.

Resources:
http://chromedriver.chromium.org/
https://selenium-python.readthedocs.io/
