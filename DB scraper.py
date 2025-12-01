from playwright.sync_api import sync_playwright
import csv


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        #  site
        page.goto("https://int.bahn.de/en?dbkanal_007=sprachauswahl-en")

        page.wait_for_load_state("load")     # Full load
        page.wait_for_timeout(3000)     

        departure = input("Enter departure location (default: Karlsruhe HBF): ").strip()
        if not departure:
            departure = "Karlsruhe HBF"    

        destination = input("Enter destination location (default: Berlin Hbf): ").strip()
        if not destination:
            destination = "Berlin Hbf"

        departure_selector = "input[name='quickFinderBasic-von']"
        departure_input = page.locator(departure_selector)
        departure_input.click()
        departure_input.fill(departure)
        departure_input.press("Enter")

        destination_selector = "input[name='quickFinderBasic-nach']"
        destination_input = page.locator(destination_selector)
        destination_input.click()
        destination_input.fill(destination)
        destination_input.press("Enter")
        
        page.wait_for_timeout(2000)

        mode_section = page.locator("span.quick-finder-option-area__heading", has_text="Mode of transport")
        mode_section.click()
        page.wait_for_timeout(1000)

        
        search_button = page.locator("button[data-test-id='quick-finder-save-button']")
        search_button.wait_for(state="visible")
        search_button.click()
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(5000)  

        results = page.locator("div.result-train-row")

        with open("train_search.csv", "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            for i in range(min(10, results.count())):
                row = results.nth(i)

                all_texts = row.all_inner_texts()
                for text in all_texts:
                    writer.writerow([text])

        # keep browser open
        # browser.close()


main()
