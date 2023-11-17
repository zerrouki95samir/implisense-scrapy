import sqlite3
import csv

# Connect to SQLite database
conn = sqlite3.connect('implisense.db')
cursor = conn.cursor()

# Fetch data from the database
cursor.execute('SELECT DISTINCT url FROM company_urls')
rows = cursor.fetchall()

# Write data to a CSV file
with open('company_urls.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'URL'])  # Writing header
    writer.writerows(rows)

# Close the database connection
conn.close()