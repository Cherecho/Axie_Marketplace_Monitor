import json
import requests
from datetime import datetime as dt

USERNAME = "Axie Infinity Sniper"
AVATAR_URL = "https://assets.axieinfinity.com/axies/2725511/axie/axie-full-transparent.png"
COLOUR = "1636343"
WEBHOOK = "https://discord.com/api/webhooks/1005194946376114287/kIi7_polpdC5jSAPXWg1TYdiZmgEdlTHvtsjaqXc4R-wnfc0xbnOLK_p5XNZmGtDAXNK"


def discord_webhook(title: str , url: str, cards: list, thumbnail: str, price: str):
    """
    Sends a Discord webhook notification to the specified webhook URL
    """
    data = {
        "username": USERNAME,
        "avatar_url": AVATAR_URL,
        "embeds": [{
            "title": "**"+title+"**",
            "url": url,
            "image": {
                "url": thumbnail
            },
            "thumbnail": {"url": thumbnail},
            "footer": {"text": "Team Axie Infinity Snipers"},
            "color": int(COLOUR),
            "timestamp": str(dt.utcnow()),
            "fields": [
                {"name": "**Eyes:**", "value": "```"+cards[0]+"```"},
                {"name": "**Ears:**", "value": "```"+cards[1]+"```"},
                {"name": "**Back:**", "value": "```"+cards[2]+"```"},
                {"name": "**Mouth:**", "value": "```"+cards[3]+"```"},
                {"name": "**Horn:**", "value": "```"+cards[4]+"```"},
                {"name": "**Price:**", "value": "**```"+price+" USD```**"}
            ]
        }]
    }

    result = requests.post(WEBHOOK, data=json.dumps(data), headers={"Content-Type": "application/json"})

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        logging.error(msg=err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))