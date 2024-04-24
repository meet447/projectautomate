#IMPORT START
from flask import Flask, request, jsonify, render_template, session, redirect, send_from_directory, Response, stream_with_context

import g4f.Provider
from g4f.client import Client
import g4f

import g4f.providers
import requests, time

import random
import string

import asyncio
from asyncio import WindowsSelectorEventLoopPolicy

asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

#IMPORT END

app = Flask(__name__)

client = Client(
            provider=g4f.Provider.RetryProvider([
                g4f.Provider.Acytoo,
                g4f.Provider.You,
                g4f.Provider.Vercel,
                g4f.Provider.PerplexityAi,
                g4f.Provider.PerplexityLabs,
                g4f.Provider.H2o,
                g4f.Provider.HuggingChat,
                g4f.Provider.HuggingFace,
                g4f.Provider.AiChatOnline,
                g4f.Provider.DeepInfra,
                g4f.Provider.Llama,
                g4f.Provider.Liaobots,
                g4f.Provider.MetaAI,
                g4f.Provider.Hashnode,
                g4f.Provider.ChatgptFree,
            ])
        )

#API ROUTE FOR STREAMING YT TO BLOG STREAM
@app.route("/api/ytblog/<id>")
def web_yt(id):
        
    def generate_completion():
        
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
        
        message = '''
        Generate HTML code with various sections, various paras, headers and more, do not generate css and js only html for the following youtube video transcript into a blog, also add all the links and extra stuff at the end.Only Generate the Code do not include anything else like "Hers your html code" in your response
        
        //////////////////
        {}
        '''.format(query)
        
        try:
            chat_completion = client.chat.completions.create(
            model=g4f.models.codellama_70b_instruct,
            messages=[{"role": "user", "content": message}],
            stream=True
        )
        
        except:
            chat_completion = client.chat.completions.create(
                model=g4f.models.default,
                messages=[{"role": "user", "content": message}],
                stream=True
            )

        for completion in chat_completion:
            yield completion.choices[0].delta.content or ""

    return Response(generate_completion(), content_type="text/event-stream")

#ROUTE FOR GENERATING SITE BASED ON YT VIDEO
@app.route("/generate/<id>")
def test_page(id):
    return render_template("blog.html", id=id)

#ROUTE FOR GENERATING SITE BASED ON QUERY
@app.route("/generate-site/<path:query>")
def test(query):
    def generate_completion():
        message = '''
        Generate HTML and CSS code for a website based on the provided query, incorporating Bootstrap and JavaScript as needed. Ensure the code represents a complete webpage with all features specified in the query. provide the entire page's code. Make it interactive, Include CSS and JavaScript within the same HTML document. Omit any additional content or instructions beyond generating the code, Only Generate the code do not include anything except code in your response, Do not include something like "Here is the HTML, CSS, and JavaScript code" in your response
        query: {}
        '''.format(query)
        

        chat_completion = client.chat.completions.create(
            model=g4f.models.default,
            messages=[{"role": "user", "content": message}],
            stream=True
        )

        for completion in chat_completion:
            yield completion.choices[0].delta.content or ""

    return Response(generate_completion())


#ROUTE FOR INDEX    
@app.route("/")
def index_page():
   return render_template("home.html")