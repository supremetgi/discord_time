import requests 
from datetime import datetime
import config


current_time = datetime.now().strftime("%H:%M:%S")
current_time = str(current_time)

header = {
    'Authorization':config.Auth,
    'Content-Type':'application/json'
}
payload = {
    'content':f"the time is {current_time}"
}
r = requests.post(f'https://discord.com/api/v9/channels/{config.channel_id}/messages', json=payload, headers=header)
print(r)

