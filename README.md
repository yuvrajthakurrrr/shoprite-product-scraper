# ShopRite Product Scraper

This project is an automated web scraper designed to extract detailed product data from [ShopRite](https://www.shoprite.com). The tool gathers essential product information, including prices, nutritional values, stock status, and customer ratings, and stores the structured data in a SQL Server database for real-time analysis. The scraper handles dynamic content, manages sessions with cookies and proxy rotation, and incorporates CAPTCHA bypass mechanisms.

## Features

- **Comprehensive Data Extraction**: Captures a wide range of product attributes, including pricing, nutritional data, stock status, and customer ratings.
- **Dynamic Content Handling**: Utilizes Selenium to manage AJAX-based content, infinite scrolling, and pop-ups.
- **Resilient Data Pipeline**:
  - Data cleaning and validation for consistency.
  - Data transformation to SQL-ready format for streamlined ingestion.
- **Session Management & CAPTCHA Bypass**: Rotating proxies and session cookies enable seamless data scraping without interruptions.
- **SQL Database Integration**: Data is stored in SQL Server for easy access, querying, and analysis.

## Technologies

- **Python**: Core programming language.
- **Selenium**: Handles dynamic content and browser interactions.
- **SQL Server**: Stores extracted data for fast retrieval and analysis.
- **Requests & LXML**: Facilitates HTTP requests and HTML parsing.
- **Proxy Rotation & Cookie Management**: Maintains anonymity and bypasses bot detection.
- **JSON Parsing**: Extracts nested data attributes.

## Setup

### Prerequisites

- Python 3.7+
- SQL Server (or any compatible SQL database)
- Chrome WebDriver for Selenium
- Install required packages with:
  ```bash
  pip install -r requirements.txt
