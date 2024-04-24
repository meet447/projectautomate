import string, random, requests

def summarise_youtube(id):
        
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,ja;q=0.8',
            'content-type': 'application/json',
            'origin': 'https://www.summarize.tech',
            'referer': 'https://www.summarize.tech/www.youtube.com/watch?v=nUcDgVgJ3hA',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        }
        
        def generate_device_id(length=21):
            chars = string.ascii_letters + string.digits
            return ''.join(random.choices(chars, k=length))

        device_id = generate_device_id()  

        json_data = {
            'url': f'https://youtube.com/watch?v={id}',
            'deviceId': device_id,
            'idToken': None,
        }

        response = requests.post('https://www.summarize.tech/api/summary', headers=headers, json=json_data)

        query = response.text
        
        return query