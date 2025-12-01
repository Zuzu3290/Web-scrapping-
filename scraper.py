#Playwright lets you import two types of APIs: sync and async
from playwright.sync_api import sync_playwright
import csv

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        #the use of chromium is due to browsers call (chromium, firefox and webkit)
        page = browser.new_page()
        pages = int(input("enter the number of pages to scrape: "))
        for i in range(1, pages+1):
            try:
                page.goto(f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={i}")
 # goto() function modifcatio is possible to reach a specific page of the url.
                print(page.title())
    #browser.close()
            except:
             print("Error")
             page.wait_for_timeout(7000)

            titles = page.get_by_role("heading").all()

            with open("laptops.csv", "a") as csvfile:
                writer = csv.writer(csvfile)
                for title in titles:
                    laptop = title.locator("a.title").all_inner_texts()
                    if len(laptop) == 1:
                        writer.writerow([laptop[0]])

        browser.close()

 #enter a site’s URL, and wait for it to load
        # page.wait_for_timeout(7000) 
        # titles = page.get_by_role("heading").all()

        # for title in titles:
        #     laptop = title.locator("a.title").all_inner_texts()
        #     if len(laptop) == 1:
        #         print(laptop[0])

        # page.get_by_role("listitem").get_by_text("2", exact=True).click()

        # page.wait_for_timeout(5000)

        # titles = page.get_by_role("heading").all()

        # for title in titles:
        #     laptop = title.locator("a.title").all_inner_texts()
        #     if len(laptop) == 1:
        #         print(laptop[0])

main()