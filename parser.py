import requests
import os
from bs4 import BeautifulSoup

# ========= Parser configuration ===========
url = "http://www.gutenberg.org/cache/epub/5402/pg5402.html"
parse_to = "grose.py"
# ==========================================

# Download the target file
page = requests.get(url)

# Prepare the soup
soup = BeautifulSoup(page.content, 'html.parser')
p_list = soup.find_all('p')

text_list = []
for p in p_list:
    text_list.append(p.get_text())

# Write list to file
path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(path, parse_to), 'a+') as f:
    f.write("master_list = " + text_list.__repr__())
