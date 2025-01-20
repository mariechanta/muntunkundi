FROM node:14-slim
WORKDIR /app
COPY package.json .
RUN npm install --only=production
COPY . .
EXPOSE 8080
CMD ["npm", "start"]

# Base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]


