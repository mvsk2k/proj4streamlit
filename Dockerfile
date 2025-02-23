# Use the official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Streamlit app files
COPY . .

# Expose the Streamlit default port
EXPOSE 8080

# Command to run the Streamlit app
#CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
#CMD ["streamlit", "run", "app.py", "--server.port=$PORT", "--server.address=0.0.0.0"]
CMD ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]

