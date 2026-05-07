from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/booking', methods=['POST'])
def booking():
    return jsonify({"status": "success", "message": "Booking Confirmed for Poulomi's Hotel!"})

@app.route('/api/claim', methods=['POST'])
def claim():
    return jsonify({"status": "success", "message": "Claim submitted successfully."})

@app.route('/api/payment', methods=['POST'])
def payment():
    return jsonify({"status": "success", "message": "Payment processed securely."})

@app.route('/api/checkout', methods=['POST'])
def checkout():
    return jsonify({"status": "success", "message": "Check-out complete. Thank you for your stay!"})

@app.route('/api/checkin', methods=['POST'])
def checkin():
    return jsonify({"status": "success", "message": "Check-in complete. Enjoy your stay at the beach resort!"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
