import requests
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary





binary = FirefoxBinary('./file')
browser = webdriver.Firefox(firefox_binary=binary)
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'www.instagram.com'

# # 404 400 406 500 504.....
# # print(response.text)
# try:
#     response = requests.get(url)
#     if response.status_code == 200:
#         print('do something')
# except:
#     pass


# print('finaly')


# engine = webdriver.Firefox()
browser.get(url)
