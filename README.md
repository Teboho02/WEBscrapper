# Amazon SA Web Scraper

## What is this?

This is a Python-based web scraping tool designed to extract product information from Amazon South Africa (amazon.co.za). The scraper downloads product search results and parses them to extract structured data including product titles, prices, images, and URLs. The extracted data is saved in JSON format for easy analysis and comparison.

The project aims to help users compare prices and find the best deals on products from Amazon SA.

## Features

- **Automated Web Scraping**: Downloads HTML content from Amazon SA search results
- **Data Extraction**: Parses product information including:
  - Product titles
  - Current prices
  - Original prices (if discounted)
  - Product images
  - Product URLs
- **JSON Export**: Saves extracted data in a structured JSON format
- **Easy to Use**: Simple command-line execution via shell script

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Teboho02/WEBscrapper.git
cd WEBscrapper
```

2. Install required Python packages:
```bash
pip install -r requirements.txt
```

## Usage

### Method 1: Using the run script
```bash
bash run.sh
```

### Method 2: Running scripts manually
```bash
# Step 1: Download product data
python3 Ascraper.py

# Step 2: Extract and parse data
python3 extract.py
```

### Customizing the search
Edit `Ascraper.py` and modify the `query` variable (line 8) to search for different products:
```python
query = 'Samsung'  # Change this to search for different products
```

## Output

- `amazon_results.txt`: Raw HTML content from Amazon search results
- `products.json`: Structured JSON file containing extracted product data

## Requirements

- Python 3.x
- requests
- beautifulsoup4
- lxml

## Future Enhancements

- Add Takealot scraper for price comparison
- Implement command-line arguments for dynamic queries
- Add user-agent rotation to avoid blocking
- Implement rate limiting and respectful scraping
- Add price comparison functionality

## Disclaimer

This tool is for educational purposes only. Please review and comply with Amazon's Terms of Service and robots.txt before scraping. Use responsibly and respect rate limits.