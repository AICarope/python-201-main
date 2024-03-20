# Use a quotes API, e.g. https://api.quotable.io/quotes/random
# to fetch a random quote. Then use string manipulation to convert it to
# Doge speech (https://en.wikipedia.org/wiki/Doge_(meme))
# Create a tiny webpage that displays a doge image together
# with the altered quote. You can get an image URL from another API:
# http://shibe.online/api/shibes
# Write the code logic to make the API calls and assign the output to
# `doged_quote` and `doge_image_url` respectively.
# Then write the `html` string to a `.html` file and look at it in your browser.


import requests
quote_api_response = requests.get('https://api.quotable.io/random')
# Make API call to fetch the doge image URL
image_api_response = requests.get('https://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true')

import json
# Extract the quote and author from the quote API response
quote_data = quote_api_response.json()
quote = quote_data['content']
author = quote_data['author']

# Extract the doge image URL from the image API response
image_data = image_api_response.json()
doge_image_url = image_data[0]

#convert the quote to doge speech
def to_doge_speech(quote):
    # Implement logic to convert the quote to doge speech
    doged_quote = quote.replace('love', 'luv').replace('friendship', 'friendshibe')
    return doged_quote
doged_quote = to_doge_speech(quote)


# Create the HTML string
html = f'''
<!DOCTYPE html>
<html>
<head>
    <title>Doge Quote</title>
</head>
<body>
    <img src="{doge_image_url}" alt="Doge Image">
    <p>{doged_quote} - {author}</p>
</body>
</html>
'''

# Write the HTML string to a .html file
with open('doge_quote.html', 'w') as file:
    file.write(html)

    # Note:this one is very confusing. Need help.