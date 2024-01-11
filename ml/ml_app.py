from flask import Flask, jsonify, request
import threading
from ml_training import train_larger_model  # Assuming this is your training script

app = Flask(__name__)

@app.route('/start-training', methods=['GET', 'POST'])
def start_training():
    # Run training in a separate thread to avoid blocking
    threading.Thread(target=train_larger_model).start()
    return jsonify({"message": "Training started"})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
