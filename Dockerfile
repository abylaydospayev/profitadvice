# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_SECRET_KEY=eebde5e429d4d7d3c6fef4c25467d067a24880a8a5260b3c
ENV COHERE_API_KEY=D7VTCq4nHTJUJAToDVrwKJjCwWyOxATTgZs1bIF7

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]