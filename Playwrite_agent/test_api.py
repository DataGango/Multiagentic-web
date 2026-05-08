from playwright.sync_api import sync_playwright

def test_booking_api():
    print("\n--- Running API Test: Booking ---")
    with sync_playwright() as p:
        api_request_context = p.request.new_context(base_url="http://127.0.0.1:8000")
        
        print("Sending POST request to /api/book for Hilton Maldives Resort...")
        response = api_request_context.post("/api/book", data={"hotel": "Hilton Maldives Resort"})
        
        print("Asserting response HTTP status code is exactly 200 OK...")
        assert response.status == 200
        
        response_body = response.json()
        print(f"Received Database Response: {response_body}")
        
        print("Asserting 'status' dictionary key exists...")
        assert "status" in response_body
        print("Asserting 'status' value equals 'success'...")
        assert response_body["status"] == "success"
        
        print("Asserting 'message' dictionary key exists...")
        assert "message" in response_body
        print("Asserting expected text is within the database message...")
        assert "Successfully booked a suite" in response_body["message"]
        print("API Test: Booking PASSED! ✅")
        
        api_request_context.dispose()

def test_cancel_api():
    print("\n--- Running API Test: Cancel Booking ---")
    with sync_playwright() as p:
        api_request_context = p.request.new_context(base_url="http://127.0.0.1:8000")
        
        print("Sending POST request to /api/cancel for Hilton Maldives Resort...")
        response = api_request_context.post("/api/cancel", data={"hotel": "Hilton Maldives Resort"})
        
        print("Asserting response HTTP status code is exactly 200 OK...")
        assert response.status == 200
        
        response_body = response.json()
        print(f"Received Database Response: {response_body}")
        
        print("Asserting valid JSON response structure exists...")
        assert "status" in response_body
        assert "message" in response_body
        
        print("Asserting status is either 'success' or 'error' (depending on previous bookings)...")
        assert response_body["status"] in ["success", "error"]
        print("API Test: Cancel Booking PASSED! ✅")
        
        api_request_context.dispose()
