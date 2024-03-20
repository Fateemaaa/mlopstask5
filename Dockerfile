# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the local repository to the container
COPY . /app

# Install required packages
RUN pip install -r requirements.txt

# Command to run your application (can be modified based on your project structure)
CMD ["python", "app.py"]
