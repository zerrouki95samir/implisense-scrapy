# Implisense Spider
This is a Scrapy spider designed to crawl the Implisense website and extract URLs of company pages. The extracted URLs are stored in a SQLite database for further processing or analysis.

## Prerequisites
Before running the spider, ensure the following prerequisites are met:

1. Python: The code is written in Python, so you need to have Python installed on your machine. You can download it from python.org
2. Scrapy: Scrapy is required to run the spider. It can be installed via pip:
```
pip install scrapy
```
3. SQLite: The spider uses SQLite to store the extracted URLs. SQLite comes pre-installed with Python, so no additional installation is required.

## Installation
1. Clone or Download the Repository: If you have git installed, you can clone the repository. Alternatively, you can download the code as a zip file and extract it.
```
git clone https://github.com/zerrouki95samir/implisense-scrapy.git
```
2. Navigate to the Project Directory: Change your directory to where the spider's code is located.
```
cd implisenseSpider
```

## Usage
To run the spider, use the following command:
```
scrapy crawl implisense
```
This command starts the spider named 'implisense', which will begin crawling the Implisense website and storing company URLs in the SQLite database named 'implisense.db'.

## Output
The spider stores the extracted URLs in a SQLite database file named implisense.db. This file is created in the same directory as the spider. You can use any SQLite database viewer to check the extracted data.

## Author
This project was developed by Zerrouki Samir. For any queries or assistance, feel free to contact me at samir.etude.zerrouki@gmail.com.