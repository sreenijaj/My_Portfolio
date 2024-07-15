# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app


# Copy the requirements file and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local code to the container's workspace
COPY . .

# Expose the port the app runs on
EXPOSE 8501

# Run the Streamlit application
CMD ["streamlit", "run", "app.py"]
