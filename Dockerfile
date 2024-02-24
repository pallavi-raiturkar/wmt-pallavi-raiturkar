# Use an official Python 3.11 runtime as a base image
FROM python:3.11.8-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies
RUN pip install --progress-bar off --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Set the environment variable to ensure output is sent straight to the terminal without being first buffered
ENV PYTHONUNBUFFERED 1

# Set the PYTHONPATH environment variable
ENV PYTHONPATH /app

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]






