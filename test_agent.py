import os
import sys
from playwright.sync_api import sync_playwright

def test_website(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} does not exist. Please run agent.py first.")
        sys.exit(1)
        
    print(f"Testing {file_path}...")
    abs_path = os.path.abspath(file_path)
    file_url = f"file://{abs_path}"
    
    with sync_playwright() as p:
        print("Launching browser...")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(file_url)
        
        # Take a screenshot to verify visual output
        screenshot_path = "output/screenshot.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")
        
        # Basic validation: check if body exists and has content
        body_text = page.locator("body").inner_text()
        if len(body_text.strip()) > 0:
            print("Test passed: Page rendered and has visible content.")
        else:
            print("Warning: Page body appears to be empty. The generation might have failed.")
            
        browser.close()

if __name__ == "__main__":
    test_website("output/index.html")
