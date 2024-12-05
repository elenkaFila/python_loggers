import csv
from datetime import datetime
from selenium import webdriver
 
# create webdriver object
driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/")
 
# get browser log
logs = driver.get_log("browser")
with open('logs/logs.csv', 'a', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file,delimiter=" ")
            writer.writerow([f'\n{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}', logs])

# add only log level severe
log_errors = []
for entry in logs:
    if entry['level']=='SEVERE':
        log_errors.append(f'\n{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}')
        log_errors.append(entry['message'])          
        with open('logs/log_severe.csv', 'a', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file,delimiter=" ")
            writer.writerow(log_errors)