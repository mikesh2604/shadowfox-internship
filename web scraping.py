import requests
from bs4 import BeautifulSoup

# Set headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.124 Safari/537.36"
}

# Amazon search URL for shirts (India)
url = "https://www.amazon.in/s?k=shirts+for+men"

# Send HTTP request
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Find all shirt containers
products = soup.find_all("div", {"data-component-type": "s-search-result"})

# Print details of first 5 shirts
for product in products[:5]:
    title = product.h2.text.strip()

    # Extract price
    price_tag = product.find("span", class_="a-price-whole")
    price = f"₹{price_tag.text}" if price_tag else "Price not available"

    # Extract rating
    rating_tag = product.find("span", class_="a-icon-alt")
    rating = rating_tag.text if rating_tag else "No rating"

    print(f"Title : {title}")
    print(f"Price : {price}")
    print(f"Rating: {rating}")
    print("=" * 50)
