from bs4 import BeautifulSoup
import json


file_path = 'amazon_results.txt'

#open the file created by the scraper and read it andg
with open(file_path, 'r') as file:
    content = file.read()




html_string = content

soup = BeautifulSoup(html_string, 'lxml')


products = soup.select('.puis-card-container')


all_products_data = []

for product in products:
    data = {}
    

    title_tag = product.select_one('h2 a span')
    data['title'] = title_tag.text.strip() if title_tag else 'N/A'
    

    price_tag = product.select_one('.a-price .a-offscreen')
    data['price'] = price_tag.text.strip() if price_tag else 'N/A'
    

    original_price_tag = product.select_one('.a-price.a-text-price .a-offscreen')
    data['original_price'] = original_price_tag.text.strip() if original_price_tag else 'N/A'
    

    image_tag = product.select_one('.s-image')
    data['image_url'] = image_tag['src'] if image_tag else 'N/A'
    

    link_tag = product.select_one('h2 a')
    data['url'] = link_tag['href'] if link_tag else 'N/A'
    

    all_products_data.append(data)


with open('products.json', 'w') as json_file:
    json.dump(all_products_data, json_file, indent=4)

print('Data has been saved to products.json')

