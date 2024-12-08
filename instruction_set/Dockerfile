# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /decomplexify

# Copy the current directory contents into the container at /app
COPY . /decomplexify

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 3001 available to the world outside this container
EXPOSE 3001

# Run Flask when the container starts
CMD ["python", "api.py"] 
