# Step 1: Use an official, lightweight Python runtime base image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file into the container at /app
COPY requirements.txt .

# Step 4: Install the dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of our application code into the container
COPY . .

# Step 6: Expose the port Flask runs on (5000)
EXPOSE 5000

# Step 7: Define the command to run the application when the container starts
CMD ["python", "app.py"]