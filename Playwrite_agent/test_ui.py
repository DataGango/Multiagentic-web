import re
from playwright.sync_api import Page, expect

def test_hotel_homepage(page: Page):
    print("\n--- Running UI Test: Hotel Homepage ---")
    page.goto("http://127.0.0.1:8000")

    print("Asserting page title is 'Global Hotel Network API'...")
    expect(page).to_have_title(re.compile("Global Hotel Network API"))

    print("Asserting 'Book a Room' yellow button click...")
    page.locator("button.btn-yellow").click()

    print("Asserting notification response-box becomes visible...")
    notification = page.locator("#response-box")
    expect(notification).to_be_visible()
    
    print("Asserting notification text contains success message...")
    expect(notification).to_contain_text("Successfully booked a suite")
    print("UI Test: Hotel Homepage PASSED! ✅")

def test_logout_button(page: Page):
    print("\n--- Running UI Test: Logout Button ---")
    page.goto("http://127.0.0.1:8000")
    
    print("Asserting Logout button presence and visibility...")
    logout_btn = page.locator("text=Logout")
    expect(logout_btn).to_be_visible()
    print("UI Test: Logout Button PASSED! ✅")

def test_hotel_logos(page: Page):
    print("\n--- Running UI Test: Hotel Logos ---")
    page.goto("http://127.0.0.1:8000")
    
    print("Asserting Hilton logo image is visible...")
    hilton_logo = page.locator("img[alt='Hilton']")
    expect(hilton_logo).to_be_visible()
    
    print("Asserting Marriott logo image is visible...")
    marriott_logo = page.locator("img[alt='Marriott']")
    expect(marriott_logo).to_be_visible()
    print("UI Test: Hotel Logos PASSED! ✅")
