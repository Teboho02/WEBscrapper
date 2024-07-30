import requests



search_url = 'https://www.amazon.co.za/s?k='

#anything you want to search for and
query = 'Samsung'


def download_html(url):
    file_path = 'amazon_results.txt'
    try:

        response = requests.get(url)

        response.raise_for_status()  
        

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)
        
        print(f'HTML page downloaded successfully as {file_path}')
    
    except requests.RequestException as e:
        print(f'Error fetching the HTML page: {e}')



download_html(search_url+query)

