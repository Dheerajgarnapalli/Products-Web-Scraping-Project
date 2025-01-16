Portl Products Web Scraping Project

Overview:
This project was developed as an assignment for Portl Company to demonstrate web scraping techniques using the BeautifulSoup package. The goal was to extract product information from a webpage and display details for three products available for purchase on the site:
The Portl Studio
The Portl Band
The Portl Ring
Each product is displayed with its name, description, price, product image, and a link to add the item to the cart.

Tech Stack:
Frontend: HTML, CSS
Backend: Python (BeautifulSoup, Requests)

Project Structure:
index.html: Contains the structure of the webpage displaying the products.
style.css: Styles the product page with layout and visual elements.
main.py: Handles web scraping using requests and BeautifulSoup to extract product details.

The HTML and CSS files used for creating the product page are included in the repository, but the primary emphasis of this README is on the web scraping process.

WEB SCRAPING PROCESS

1)Prerequisites:
Before proceeding, ensure that you have Python installed on your machine.
To install the required packages, open your command prompt (or terminal) and use the following commands:
>>pip install beautifulsoup4
>>pip install requests 
>>pip install lxml
These are the key packages:
beautifulsoup4: To parse and extract data from HTML.
requests: To fetch the webpage content.
lxml: An efficient parser for BeautifulSoup.

2)Setting Up Your Environment

You can use any IDE or code editor to run the script. I'll provide instructions for both VS Code and PyCharm:

Create a folder and add the index.html, style.css and main.py file
VS Code:
Open the created folder and click on main.py file

PyCharm:
Open the created folder and click on main.py file
Sometimes, PyCharm might be using the wrong Python interpreter, so you need to ensure it's using the correct one.
Go to File > Settings (or PyCharm > Preferences on macOS).
In the left pane, go to Project: your_project_name > Python Interpreter.
install the packages beautifulsoup, requests, lxml

You need to run the current index.html in the localhost. For that open command prompt and change directory to the created folder where the index.html is located. Run the code below
>>python -m http.server 5050
This will set the localhost to active and we can easily

Now you can run the main.py file in both VS Code and PyCharm


3)Approach

3.1)Importing Required Packages
We begin by importing the necessary packages for web scraping:
>>from bs4 import BeautifulSoup
>>import requests

3.2) Fetching the Webpage Content
We use the requests.get() method to retrieve the HTML content from the webpage. The URL of the webpage is passed as an argument to requests.get(), and we store the returned HTML content in the html_texts variable.
>>html_texts = requests.get('http://localhost:5050/').text
This will get the raw HTML content of the page.
some times the localhost will be offline, you need to open command prompt and change the directory to current file and give the code:
>>python -m http.server 5050

3.3) Parsing the HTML with BeautifulSoup
Once we have the HTML content, we use BeautifulSoup to parse it. The html_texts is passed into BeautifulSoup, specifying the lxml parser.
>>soup = BeautifulSoup(html_texts, 'lxml')

3.4) Extracting the Page Heading
To extract the main heading of the page, we use the find() method. The first argument specifies the tag (<h1> in this case), and the second argument specifies the class name (class_="title"), which was defined in the HTML.
>>title = soup.find('h1', class_="title")
This will fetch the heading of the page (e.g., "Products"), which is printed later.

3.5) Extracting Product Information
Each product is contained within a <div> block with the class box, which is part of the main section with the ID main-box. To extract the product information, we first find all the div blocks with the class box:
>>box = soup.find_all('div', class_='box')
The box variable now contains all the product div blocks. We then iterate over each box using a for loop to extract the product details.

6. Iterating Over Each Product
For each product, we extract the following details:
    >>for each_box in box:
        i+=1
        product_name = each_box.h3.text
        product_desc= each_box.h4.text
        product_price=each_box.h2.text
        product_image=each_box.a.img
	a_tag = each_box.find('a', class_="to_buy")
    	product_cart_link = a_tag['href']
3.7)printing the above created variables 
the output will look like:

Title of the Page: PRODUCTS


Product 1 name: THE PORTL STUDIO
Product 1 description: 43" High-Resolution Multi-Touch
Product 1 price: 125,000 +GST
Product 1 image link: https://portl.co/wp-content/uploads/2021/11/4-1-230x350.jpg
Product 1 cart link: #


Product 2 name: THE PORTL BAND
Product 2 description: 1.39" AMOLED high-resolution display
Product 2 price: 60,000 +GST
Product 2 image link: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTY-OZLq2vIGMA9Gweb4GmWI47SJcXquu65Lg&s
Product 2 cart link: #


Product 3 name: THE PORTL RING
Product 3 description: Compact health-tracking high-resolution sensor
Product 3 price: 45,000 +GST
Product 3 image link: https://res.cloudinary.com/dmezmffej/image/upload/v1721388046/Frame_48098010_2_1.avif
Product 3 cart link: #








