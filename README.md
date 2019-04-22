# webhookalert
> :warning: WARNING: This project was built to notify Discord guild members/admins if one of their webhook links were found on the web. I take **zero** responsibility for any illegitimate or otherwise unwanted use of this program.    
Basically, if you're gonna use this program to be a total cunt, just don't.

> If you have a problem with the ethics of this program, please feel free to create an issue and we can discuss it there.

## How this program works
Currently all webhook links need to be prepopulated in a list. There's no automated searching for webhook links (yet), nor does this program work with **Bot** tokens.

Once webhook tokens are in the `list.txt` file and the program is ran, any duplicates are removed, as well as any line not matching the Discord Webhook API base URL (`https://discordapp.com/api/webhooks/`).

After that, a GET request is made to each valid webhook URL. If the GET request returns a status code that isn't 200 or 204, the invalid URL is stored in a list and that iteration is skipped. If the GET request shows that the webhook is valid, a POST request is made to the webhook URL, with the final message looking like this (assuming the default message has not been changed):    
![Example of message posted](https://i.imgur.com/kIZd59t.png)

Once all webhook URLs in the file have been checked, the program moves on and removes all invalid URLs that were found in the previous stage.

The program is designed to run on a loop, as I feel that having your webhook tokens leaked is somewhat of an urgent matter, so the program should be looped often enough to be annoying to guilds/guild admins, prompting them to remove their webhook - but not so often as to breach Discord rate limits. There is also a delay of 1 second between each POST request. I don't recommend removing this, and I recommend the program be looped on a delay of no less than 15 minutes.

## Requirements
Only Requests! Everything else uses built-in modules/functions.    
`pip install requests`
