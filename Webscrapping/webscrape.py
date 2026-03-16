import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Establish URL for reviews. Will potentially extend or change to other review pages for the location.
# Uncomment to use either URL for respective site
# Hyatt Official site: 
# URL = "https://www.hyatt.com/hyatt-regency/en-US/sjurc-hyatt-regency-grand-reserve-puerto-rico/reviews"

# TripAdvisor site
URL = "https://www.tripadvisor.com/Hotel_Review-g1006845-d284987-Reviews-Hyatt_Regency_Grand_Reserve_Puerto_Rico-Rio_Grande_Puerto_Rico.html#REVIEWS"

# Yelp site: 
# URL = "https://www.yelp.com/biz/hyatt-regency-grand-reserve-r%C3%ADo-grande?osq=Hyatt+Regency+Grand+Reserve+Puerto+Rico&override_cta=Get+information"

# Google Reivews
# URL = "https://www.google.com/travel/search?q=hyatt%20regency%20grand%20resort&g2lb=4965990%2C72471280%2C72560029%2C72573224%2C72647020%2C72686036%2C72803964%2C72882230%2C72958624%2C73059275%2C73064764%2C121529349%2C121543878&hl=en-PR&gl=pr&ssta=1&ts=CAEaSQopEicyJTB4OGMwNDljMjRkMDlhNzMzNToweGUzOWUxNGRlZjZmYmQ4MjMSHBIUCgcI6g8QBBgDEgcI6g8QBBgEGAEyBAgAEAAqBwoFOgNVU0Q&qs=CAEyFENnc0lvN0R2dC0tYmhjX2pBUkFCOAJCCQkj2Pv23hSe40IJCSPY-_beFJ7j&ap=MAC6AQdyZXZpZXdz&ictx=111&ved=0CAAQ5JsGahgKEwjgl5GgmZGTAxUAAAAAHQAAAAAQggE"

options = Options()
options.add_experimental_option("detach", True)

PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
options.binary_location = PATH

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Get URL
driver.get(URL)
print(driver.title)


# # Click read more, and load more button to avoid truncated text data
# read_more_butt = driver.find_elements(By.XPATH, '//button[.//span[text()="Read more"]]')
# for button in read_more_butt:
#     try:
#         driver.execute_script("arguments[0].click();", button)
#         time.sleep(random.uniform(1,3))
#     except:
#         pass

# # Click on next page
# next_page_butt = driver.find_element(By.XPATH, '//a[@aria-label="Next page"]')
# try:
#     driver.execute_script("arguments[0].click();", button)
#     time.sleep(random.uniform(1,3))
# except:
#     pass

#Initiate list to store data
MAX_REVIEWS = 150
review_data = []

while True:
    # Click read more, and load more button to avoid truncated text data
    read_more_butt = driver.find_elements(By.XPATH, '//button[.//span[text()="Read more"]]')
    for button in read_more_butt:
        try:
            driver.execute_script("arguments[0].click();", button)
            time.sleep(random.uniform(1,3))
        except:
            pass

    # Extract review data: review, rating, date
    reviews = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ryPjd"))
    )

    for review in reviews[:5]:
        review_text = review.find_element(By.CSS_SELECTOR, ".biGQs._P.VImYz.AWdfh").text
        rating = review.find_element(By.CSS_SELECTOR, "svg.evwcZ title").get_attribute("innerHTML")
        date = review.find_element(By.CSS_SELECTOR, ".RUZll").text
        date_of_stay = review.find_element(By.CSS_SELECTOR,".biGQs._P.VImYz.xENVe").text
        trip_type = review.find_element(By.CSS_SELECTOR, ".biGQs._P.VImYz.xENVe").text

        review_data.append({
            "review": review_text,
            "rating": rating,
            "date": date,
            "date of stay": date_of_stay,
            "trip type" : trip_type
        })

        if len(review_data) >= MAX_REVIEWS:
            break

    if len(review_data) >= MAX_REVIEWS:
        break

    # Click on next page
    try:
        next_page_butt = driver.find_element(By.XPATH, '//a[@aria-label="Next page"]')
        driver.execute_script("arguments[0].click();", button)
        time.sleep(random.uniform(1,3))
    except:
        break

print("Finished scrapping")
print(review_data[:5])
print(f"Total of reviews scrapped: {len(review_data)}")

# Quit driver
driver.quit()

# Trip Advisor Hyatt website dataframe
review_df = pd.DataFrame(review_data).to_csv("Trip_Advisor_Hyatt_Data.csv", index=False)

