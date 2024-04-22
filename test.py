import requests

cookies = {
    'csrfToken': '1uneoW2kdkpomO3vDGJy4mM8',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ja;q=0.8',
    'content-type': 'application/json',
    # 'cookie': 'csrfToken=1uneoW2kdkpomO3vDGJy4mM8',
    'origin': 'https://gptgod.online',
    'referer': 'https://gptgod.online/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-csrf-token': '1uneoW2kdkpomO3vDGJy4mM8',
}

json_data = {
    'content': 'who are you',
    'model': 'gpt-3.5-turbo',
    'token': '0.4fqHrCUtqohC8k1aatf4lKz7oja_mONfvIbuDQ-0ATVVi1EZORKJC-87i09aLLim_ymhZ7nAvVo3RkJBvJcPtdVo3_N_d1GrjSDm5ciiCPtpX6ECT7M5gLBcTrXVRvNtpLoVyXNeDBOsvI3zGU4k4J7Og79z0gOKm6iB1A8NF_uxTGEaMLsC8uhbfVgtLrCP_GxRE1V29_0K4E5pdBLa-x0FhXt8vsPcYX82N0lSCximxZHyzyvUugMrNX4bnhQZ8HDdEUm0y67RZm2DGpRdfveH_i6VWz0mz5y4gJzCoBsyi-ed-7YkrJ1PES97w3e92BBmH_yxjSGdjaUHieo4l2KWRb5ug7clzc4zZwXoGkMCVEeDVRlQfHVfX7hoU2DQiWPpTc3MEJCzWKQ4r5rZ2poe01jAJp4YoR0f8pMAEsU5mEiJ25mwqQU62324b-VlOdBch5yjSf6EIf-3Z65yZQ.czH1DD6qYxnp62RAmBleww.4c3f21649e9d9f07ac0114c8c427b29475470e137d2a0a5e2a594e7d8ce54db0',
    'search': False,
}

response = requests.post('https://gptgod.online/api/session/free/chat', cookies=cookies, headers=headers, json=json_data)

print(response.json())