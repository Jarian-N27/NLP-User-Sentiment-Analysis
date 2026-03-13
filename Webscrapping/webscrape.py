from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Establish URL for reviews. Will potentially extend or change to other review pages for the location.
# Hyatt Official site: "https://www.hyatt.com/hyatt-regency/en-US/sjurc-hyatt-regency-grand-reserve-puerto-rico/reviews"
# Google review site: "https://www.google.com/travel/search?q=hyatt%20regency%20grand%20resort&g2lb=4965990%2C72471280%2C72560029%2C72573224%2C72647020%2C72686036%2C72803964%2C72882230%2C72958624%2C73059275%2C73064764%2C121529349%2C121543878&hl=en-PR&gl=pr&ssta=1&ts=CAEaSQopEicyJTB4OGMwNDljMjRkMDlhNzMzNToweGUzOWUxNGRlZjZmYmQ4MjMSHBIUCgcI6g8QBBgDEgcI6g8QBBgEGAEyBAgAEAAqBwoFOgNVU0Q&qs=CAEyFENnc0lvN0R2dC0tYmhjX2pBUkFCOAJCCQkj2Pv23hSe40IJCSPY-_beFJ7j&ap=MAC6AQdyZXZpZXdz&ictx=111&ved=0CAAQ5JsGahgKEwjgl5GgmZGTAxUAAAAAHQAAAAAQggE"
# Yelp site: "https://www.yelp.com/biz/hyatt-regency-grand-reserve-r%C3%ADo-grande?osq=Hyatt+Regency+Grand+Reserve+Puerto+Rico&override_cta=Get+information"

# Uncomment to use either URL for respective site
# Google Reivews
URL = "https://www.google.com/travel/search?q=hyatt%20regency%20grand%20resort&g2lb=4965990%2C72471280%2C72560029%2C72573224%2C72647020%2C72686036%2C72803964%2C72882230%2C72958624%2C73059275%2C73064764%2C121529349%2C121543878&hl=en-PR&gl=pr&ssta=1&ts=CAEaSQopEicyJTB4OGMwNDljMjRkMDlhNzMzNToweGUzOWUxNGRlZjZmYmQ4MjMSHBIUCgcI6g8QBBgDEgcI6g8QBBgEGAEyBAgAEAAqBwoFOgNVU0Q&qs=CAEyFENnc0lvN0R2dC0tYmhjX2pBUkFCOAJCCQkj2Pv23hSe40IJCSPY-_beFJ7j&ap=MAC6AQdyZXZpZXdz&ictx=111&ved=0CAAQ5JsGahgKEwjgl5GgmZGTAxUAAAAAHQAAAAAQggE"

# Yelp
# URL = "https://www.yelp.com/biz/hyatt-regency-grand-reserve-r%C3%ADo-grande?osq=Hyatt+Regency+Grand+Reserve+Puerto+Rico&override_cta=Get+information"


options = Options()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Get URL
driver.get(URL)

# Quit driver
driver.quit()