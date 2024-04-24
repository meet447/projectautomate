import requests

url = "https://www.reddit.com/r/TowerofGod/comments/1cc0714/theory_for_trau_mask/.json"

response = requests.get(url)

data = response.json()

# Loop through each item in the data list
for item in data:
    # Check if the item is of kind 'Listing'
    if item['kind'] == 'Listing':
        # Loop through each child in the 'children' list
        for child in item['data']['children']:
            # Check if the child is of kind 't3'
            if child['kind'] == 't3':
                print("Title:", child['data']['title'])
                print("Subreddit:", child['data']['subreddit'])
                print("Author:", child['data']['author'])
                print("Score:", child['data']['score'])
                print("Number of Comments:", child['data']['num_comments'])
                print("Permalink:", child['data']['permalink'])
                print("URL:", child['data']['url'])
                print("Body:", child['data']['selftext'])
                # Check if the post has any images
                if 'preview' in child['data']:
                    images = child['data']['preview']['images']
                    print("Images:")
                    for image in images:
                        print("- URL:", image['source']['url'])
                else:
                    print("No images.")
                print("Top 3 Comments:")
                # Get the top 3 comments
                top_comments = []
                for comment in child['data']['comments']:
                    if comment['data']['score'] > 0:
                        top_comments.append((comment['data']['author'], comment['data']['body']))
                        if len(top_comments) == 3:
                            break
                for i, (author, body) in enumerate(top_comments, start=1):
                    print(f"{i}. Author: {author}")
                    print(f"   Body: {body}")
                print("---")

