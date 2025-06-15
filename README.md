# DevOps Internship Assignment — Flask App Deployment 🚀

This project demonstrates containerizing a simple Python Flask web app using Docker and deploying it on an AWS EC2 instance.

---

## 🧱 Tech Stack
- Python 3.9
- Flask
- Docker
- AWS EC2 (Ubuntu 22.04)
- Git & GitHub

---

## 📁 Project Structure

devops-flask-app/
│
├── app.py
├── requirements.txt
└── Dockerfile



---

## 🧪 Local Docker Instructions

### Build the image:
```bash
docker build -t flask-app .
```
You can now access the app locally by navigating to http://localhost:5000 in your browser.

☁️ AWS EC2 Deployment Instructions
🔧 Prerequisites
-An AWS account with EC2 access

    -A running EC2 instance (Ubuntu 22.04 LTS, t2.micro)

    -Security group configured to allow port 80 (HTTP) traffic

🖥️ EC2 Setup Instructions
1. SSH into your EC2 instance
Use the .pem key downloaded when you launched the instance:

```bash
Copy
Edit
chmod 400 your-key.pem
ssh -i your-key.pem ubuntu@<your-ec2-public-ip>
```
2. Install Docker and Git
Run the following commands on your EC2 instance:

```bash
Copy
Edit
sudo apt update
sudo apt install -y docker.io git
sudo systemctl start docker
sudo usermod -aG docker ubuntu
newgrp docker
```
3. Clone your GitHub repository
Clone your project code from GitHub:

```bash
Copy
Edit
git clone https://github.com/Ashwin-premani/devops-flask-app.git
cd devops-flask-app
```
4. Build the Docker image
```bash
Copy
Edit
docker build -t flask-app .
```
5. Run the Docker container on port 80
```bash
Copy
Edit
docker run -d -p 80:80 flask-app
```
🌍 Access the App
Once the container is running, open your browser and go to:

```cpp
Copy
Edit
http://<your-ec2-public-ip>
```
✅ Your Flask app should now be live on the internet! 🎉

