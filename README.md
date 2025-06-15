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
Prerequisites
AWS account with access to EC2

EC2 instance (Ubuntu 22.04, t2.micro) created

Security group with port 80 open for HTTP traffic

EC2 Setup
SSH into your EC2 instance using the .pem key file you downloaded when creating the EC2 instance.

bash
Copy
Edit
chmod 400 <your-key.pem>
ssh -i <your-key.pem> ubuntu@<your-ec2-public-ip>
Install Docker and Git on your EC2 instance:

bash
Copy
Edit
sudo apt update
sudo apt install -y docker.io git
sudo systemctl start docker
sudo usermod -aG docker ubuntu
newgrp docker
Clone your GitHub repo with the project code:

bash
Copy
Edit
git clone https://github.com/Ashwin-premani/devops-flask-app.git
cd devops-flask-app
Build the Docker image on EC2:

bash
Copy
Edit
docker build -t flask-app .
Run the Docker container on port 80:

bash
Copy
Edit
docker run -d -p 80:80 flask-app
Accessing the App
Once the container is running, navigate to the public IP address of your EC2 instance in a web browser:

cpp
Copy
Edit
http://<your-ec2-public-ip>
Your Flask app should now be live on the internet! 🎉
