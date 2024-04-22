#IMPORT START
from flask import Flask, request, jsonify, render_template, session, redirect, send_from_directory, Response, stream_with_context

import g4f.Provider
from g4f.client import Client
import g4f

import requests, time
#IMPORT END

app = Flask(__name__)

#API ROUTE FOR STREAMING YT TO BLOG STREAM
@app.route("/api/ytblog/<id>")
def web_yt(id):
    
    model = ""
    
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

        json_data = {
            'url': f'https://youtube.com/watch?v={id}',
            'deviceId': 'sHb6pfPavbCvGUUeniQQL',
            'idToken': None,
        }

        response = requests.post('https://www.summarize.tech/api/summary', headers=headers, json=json_data)

        query = response.text
        
        message = '''
        Generate HTML code with various sections, various paras, headers and more, do not generate css and js only html for the following youtube video transcript by summarising it:
        
        //////////////////
        {}
        '''.format(query)
        
        client = Client()
        chat_completion = client.chat.completions.create(
            model="dbrx-instruct",
            messages=[{"role": "user", "content": message}],
            stream=True
        )

        for completion in chat_completion:
            yield completion.choices[0].delta.content or ""

    return Response(generate_completion(), content_type="text/event-stream")

#ROUTE FOR GENERATING SITE
@app.route("/generate/<id>")
def test_page(id):
    return render_template("blog.html", id=id)


@app.route("/generate-site/<model>/<query>")
def test(model, query):
    def generate_completion():
        message = '''
        Generate HTML and CSS code for a website based on the provided query, incorporating Bootstrap and JavaScript as needed. Ensure the code represents a complete webpage with all features specified in the query. Avoid creating a basic template; instead, provide the entire page's code. Include CSS and JavaScript within the same HTML document. Omit any additional content or instructions beyond generating the code
        query: {}
        '''.format(query)
        
        client = Client()
        chat_completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": message}],
            stream=True
        )

        for completion in chat_completion:
            yield completion.choices[0].delta.content or ""

    return Response(generate_completion())


