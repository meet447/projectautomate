import requests

def fetch_event_stream():
    response = requests.get("http://127.0.0.1:5000/ytweb", stream=True)
    if response.status_code == 200:
        for line in response.iter_lines():
            if line:
                print(line.decode('utf-8'))  # Decode bytes to string and print
    else:
        print("Failed to fetch event stream")

fetch_event_stream()
