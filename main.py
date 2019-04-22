import requests
import json
import os
from time import sleep

CWD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')

WEBHOOK_CONTENT = {"username":"Your webhooks are compromised!","avatar_url":"https://i.imgur.com/9zJupPr.jpg","content":"@everyone","embeds":[{"description":"Hi there! This is a friendly notice from an anonymous Discord user! \nThis webhook link was found on a random GitHub repo.\n\nIn case you're unaware, this isn't something that you should do as it would allow people (with worse intentions than myself) to send random messages such as spam, server invites, links to virus websites or pornographic content. \n\nI would advise that you go into your Server's settings and delete this webhook, and in future, take better care so that your webhook links do not fall into the wrong hands!\n(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ).","color":16731212,"image":{"url":"https://i.imgur.com/vncwRtz.png"}}]}
BROKEN_LINKS = []

WEBHOOK_LIST = CWD + "list.txt"
with open(WEBHOOK_LIST, 'r+') as webhooks:
    # Load all lines into a variable of some kind
    lines = webhooks.read().splitlines()

    # Remove duplicates
    read_lines = []
    webhooks.seek(0)
    for line in lines:
        if line not in read_lines:
            if "https://discordapp.com/api/webhooks/" not in line:
                continue
            webhooks.write(f"{line}\n")
            read_lines.append(line)
    webhooks.truncate()
    webhooks.seek(0)

    # Reload our list of lines
    lines = webhooks.read().splitlines()

    # Begin link checking
    for link in lines:
        r = requests.get(link)
        # Check if the link is a valid webhook. Only valid webhooks return status 200 or 204
        if r.status_code not in (200, 204):
            BROKEN_LINKS.append(link)
            # Don't know why we're giving the status of dead webhooks. Enable it if you want.
            #print(f"{r.status_code}, {r.text}")
            continue
        getResponse = json.loads(r.text)
        getStatus = r.status_code
        print(f"Status {r.status_code} - Posting webhook to {getResponse['channel_id']} in guild {getResponse['guild_id']}\n")
        r = requests.post(link, data=json.dumps(WEBHOOK_CONTENT), headers={"Content-Type": "application/json"})
        sleep(1)

    # Go to the beginning of the file
    webhooks.seek(0)
    for link in lines:
        if link not in BROKEN_LINKS:
            # If current link does not match any link in the list we made earlier, write it
            webhooks.write(f"{link}\n")
    # Remove all text after cursor (executed after the above for loop is finished)
    webhooks.truncate()