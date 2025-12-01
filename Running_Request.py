import requests
import webbrowser
import os

url = "https://fc254.farmconnect.eu/"

# Send GET request
response = requests.get(url)

# Check if successful
if response.status_code == 200:
    print("Page content successfully retrieved!")
    print(response.text[:500])  # Print first 500 characters

    # Save HTML to a file
    file_path = "farmconnect_page.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(response.text)

    # Open the HTML file in the default web browser
    full_path = os.path.abspath(file_path)
    webbrowser.open(f"file://{full_path}")

else:
    print(f"Failed to access the page. Status code: {response.status_code}")