from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

options = Options()
service = Service(executable_path="/snap/bin/geckodriver")
browser = webdriver.Firefox(options=options, service=service)
browser.get("http://localhost:8000")

assert "Congratulations" in browser.title
print("OK")

