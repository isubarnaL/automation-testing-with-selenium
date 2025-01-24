from selenium import webdriver
from selenium.webdriver.edge.service import Service

edge_driver_path = "C:/Users/lohan/edgedriver_win32/msedgedriver.exe"
service = Service(edge_driver_path)
driver = webdriver.Edge(service=service)

driver.get("https://www.google.com")
print("Page title:", driver.title)
driver.quit()