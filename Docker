# Base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaining files to the working directory
COPY . .

# Expose the port for the Flask application (if applicable)
EXPOSE 5000

# Command to run the application
CMD [ "python", "app.py" ]