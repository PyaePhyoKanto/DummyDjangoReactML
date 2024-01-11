FROM pytorch/pytorch

# Set the working directory
WORKDIR /ml

# Install Python dependencies
COPY requirements_ml.txt /ml/
RUN pip install --no-cache-dir -r requirements_ml.txt

# Copy the Flask app and ML training script
COPY ml_app.py /ml/
COPY ml_training.py /ml/

# Command to run the Flask app
# -u for unbuffered output for testing purpose
CMD ["python", "-u", "ml_app.py"]
