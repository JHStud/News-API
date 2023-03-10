import requests
from send_email import send_email

api_key = "a0d2d7bdbfd946ac80c6f8224eefb779"
url = "https://newsapi.org/v2/everything?q=" \
      "tesla&from=2023-01-09&sortBy=published" \
      "At&apiKey=a0d2d7bdbfd946ac80c6f8224eefb779"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
      body = body + article["title"] + "\n" + article["description"] + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)
