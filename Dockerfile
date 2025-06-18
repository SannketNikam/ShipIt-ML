FROM python:3.8-slim-buster

# Optional: uncomment if you still need system packages like git, wget, etc.
# RUN apt update -y && apt install -y git wget

WORKDIR /app

# Copy code to container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port required by Hugging Face Spaces
EXPOSE 7860

# Run your Flask app
CMD ["python", "app.py"]
