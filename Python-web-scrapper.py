from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

def main():
    # Chrome WebDriver
    driver = webdriver.Chrome()

    driver.get("https://int.bahn.de/en/")

    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='quickFinderBasic-von']")))  # Departure input

    departure = input("Enter departure location (default: Karlsruhe HBF): ").strip()
    if not departure:
        departure = "Karlsruhe HBF"

    destination = input("Enter destination location (default: Berlin Hbf): ").strip()
    if not destination:
        destination = "Berlin Hbf"

    departure_selector = "input[name='quickFinderBasic-von']"
    departure_input = driver.find_element(By.CSS_SELECTOR, departure_selector)
    departure_input.click()
    departure_input.clear()
    departure_input.send_keys(departure)
    departure_input.send_keys(Keys.ENTER)

    destination_selector = "input[name='quickFinderBasic-nach']"
    destination_input = driver.find_element(By.CSS_SELECTOR, destination_selector)
    destination_input.click()
    destination_input.clear()
    destination_input.send_keys(destination)
    destination_input.send_keys(Keys.ENTER)

    first_class_button_selector = "button#option-KLASSE_1"
    first_class_button = driver.find_element(By.CSS_SELECTOR, first_class_button_selector)
    first_class_button.click()

    search_button_selector = "button#searchBtn"
    search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_button_selector)))
    search_button.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".connection")))  # Journey results

    # journey data
    journeys = []
    journey_elements = driver.find_elements(By.CSS_SELECTOR, ".connection")

    for j in journey_elements:
        try:
            dep_time = j.find_element(By.CSS_SELECTOR, ".time.depart").text
            arr_time = j.find_element(By.CSS_SELECTOR, ".time.arrive").text
            duration = j.find_element(By.CSS_SELECTOR, ".duration").text
            price = j.find_element(By.CSS_SELECTOR, ".fare").text

            journeys.append({
                "departure": dep_time,
                "arrival": arr_time,
                "duration": duration,
                "price": price
            })
        except Exception as e:
            print(f"Error extracting data from a journey: {e}")
            continue

    # CSV file
    with open("train_search.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        if csvfile.tell() == 0:
            writer.writerow(["departure", "arrival", "duration", "price"])

        for journey in journeys:
            writer.writerow([journey["departure"], journey["arrival"], journey["duration"], journey["price"]])

    print(f"Saved {len(journeys)} journeys to 'train_search.csv'")

    # driver.quit()


main()
