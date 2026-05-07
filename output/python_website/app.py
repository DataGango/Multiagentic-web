from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return jsonify({
        "status": "success",
        "message": "Python Flask backend is running perfectly!",
        "agent": "AI Web Agent Simulation"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
