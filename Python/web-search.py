from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import argparse
import time


def list_to_string(lst):
    return ''.join(lst)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Google Search')
    parser.add_argument('search_string', type=str, help='String to search on Google')
    args = parser.parse_args()

    search_string = args.search_string.replace(' ', '+')

    # Use a headless browser
    options = webdriver.ChromeOptions()
    
    # Provide the path to ChromeDriver using Service
    service = Service('chromedriver_win32/chromedriver.exe')
    
    # Create the WebDriver using the Service and options
    browser = webdriver.Chrome(service=service, options=options)

    try:
        for i in range(1):
            url = f"https://www.google.com/search?q={search_string}&start={i}"
            browser.get(url)
            time.sleep(5)  # Add a delay to allow the page to load
            
        # Do additional processing if needed
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        browser.quit()  # Close the browser window
