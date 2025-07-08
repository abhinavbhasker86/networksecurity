FROM python:3.10-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements file if you have one
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . /app

# Set the default command (replace 'app.py' with your main script)
CMD ["python", "app.py"]