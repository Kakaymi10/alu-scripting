#!/usr/bin/python3

import requests
import re

def count_words(subreddit, word_list, after=None, word_count={}):
    """Recursive function that queries the Reddit API, parses the title of all hot articles, 
    and prints a sorted count of given keywords"""

    # URL for the subreddit's hot posts in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # User agent header to prevent 429 (Too Many Requests) errors
    headers = {'User-Agent': 'Mozilla/5.0'}
    # Parameters for the request (limit of 100 posts per page, and "after" parameter to get the next page of posts)
    params = {'limit': '100', 'after': after}
    
    # Make the request to the API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    # Check if the subreddit is invalid (status code other than 200)
    if response.status_code != 200:
        print(f"Invalid subreddit: {subreddit}")
        return
    
    # Parse the response JSON data
    data = response.json()
    # Extract the posts from the data
    posts = data['data']['children']
    
    # Loop through each post's title and each word in the word_list
    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            # Use regular expressions to match whole words only
            if word.lower() in re.findall(r'\b\w+\b', title):
                # Increment the count of the word in the word_count dictionary
                word_count[word.lower()] = word_count.get(word.lower(), 0) + 1
    
    # Check if there are no more posts to get
    if not data['data']['after']:
        # Sort the word_count dictionary by count (descending) and then by word (ascending)
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        # Print the sorted word count
        for word, count in sorted_words:
            print(f"{word}: {count}")
        return
    
    # Call the function again with the "after" parameter set to the next page of posts
    return count_words(subreddit, word_list, after=data['data']['after'], word_count=word_count)
