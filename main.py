import sys
import io

# Set UTF-8 encoding for stdout and stderr
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from bs4 import BeautifulSoup
import requests

try:
    # Fetch the HTML content from the local web server
    html_texts = requests.get('http://localhost:5050/#').text
    #print(html_texts)
except requests.exceptions.RequestException as e:
    print(f"Error fetching the page :",e)
    exit()


# Parse the HTML content using BeautifulSoup and lxml parser
try:
    soup = BeautifulSoup(html_texts, 'lxml')
except Exception as e:
    print(f"Error parsing the HTML content :",e)
    exit()

# Extract the title of the page
try:
    title = soup.find('h1', class_="title")
    if title:
        print("Title of the Page:", title.text)
    else:
        print("Title not found")
except Exception as e:
    print(f"Error fetching the title:")

print("\n")  # Adding a blank line for better readability

# Extract all divs with class 'box'
try:
    box = soup.find_all('div', class_='box')
except Exception as e:
    print(f"Error fetching 'box' divs :",e)
    exit()

# Loop through each box and extract product details
i = 0
for each_box in box:
    i += 1
    try:
        # Extract product name from <h3> tag
        product_name = each_box.h3.text if each_box.h3 else "No product name"
        # Extract product description from <h4> tag
        product_desc = each_box.h4.text if each_box.h4 else "No product description"
        # Extract product price from <h2> tag
        product_price = each_box.h2.text if each_box.h2 else "No product price"
        # Extract product image link from <img> tag inside <a> tag
        product_image = each_box.a.img['src'] if each_box.a and each_box.a.img else "No image link"
        # Extract product cart link
        a_tag = soup.find('a', class_="to_buy")
        product_cart_link = a_tag['href']


        # Print the extracted product details
        print(f"Product {i} name: {product_name}")
        print(f"Product {i} description: {product_desc}")
        print(f"Product {i} price: {product_price}")
        print(f"Product {i} image link: {product_image}")
        print(f"Product {i} cart link: {product_cart_link}")
        print("\n")

    except Exception as e:
        print(f"Error processing product {i}: {e}")
