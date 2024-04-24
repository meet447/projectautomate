import requests

class Reddit:
    
    base_url = "https://www.reddit.com/"
    
    def search_data(self, query):
        
        url = Reddit.base_url + f"/search.json?q={query}&restrict_sr=on&include_over_18=on&sort=relevance&t=all"
        
        response = requests.get(url)
        
        data = response.json()
        
        for post in data['data']['children']:
            post_data = post['data']
            post_url = post_data['url']
            if post_url.startswith("https://www.reddit.com/r/"):
                image_url = post_data['thumbnail']
                if image_url not in ["self", "default"]:
                    title = post_data['title']
                    subreddit = post_data['subreddit']
                    print("Post URL:", post_url)
                    print("Image URL:", image_url)
                    print("Title:", title)
                    print("Subreddit:", subreddit)


Reddit().search_data("rtx 3050")
