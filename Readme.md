# Student Feedback System — DevOps Mini Project

**Course:** CSM Department | **Guide:** S. Yoganandh (Assistant Professor)

---

## 📁 Project Structure

```
student-feedback-system/
├── app/
│   ├── app.py            ← Flask backend
│   ├── database.py       ← SQLite database logic
│   └── requirements.txt  ← Python dependencies
├── templates/
│   └── index.html        ← HTML frontend
├── static/
│   └── style.css         ← CSS styling
├── Dockerfile            ← Docker image definition
├── Jenkinsfile           ← CI/CD pipeline stages
├── ansible/
│   ├── inventory         ← Ansible host configuration
│   └── deploy.yml        ← Ansible deployment playbook
└── README.md
```

---

## 🛠️ Tools Required

| Tool     | Purpose                  |
|----------|--------------------------|
| Git      | Version control          |
| Python   | Run Flask app locally    |
| Docker   | Containerize the app     |
| Jenkins  | Automate CI/CD pipeline  |
| Ansible  | Automate deployment      |

---

## ▶️ Step 1 — Run Locally (Without Docker)

```bash
cd app
pip install -r requirements.txt
python app.py
```
Open: http://localhost:5000

---

## 🐳 Step 2 — Run with Docker

```bash
# Build Docker image
docker build -t student-feedback-app .

# Run container
docker run -p 5000:5000 student-feedback-app
```
Open: http://localhost:5000

---

## ⚙️ Step 3 — Jenkins CI/CD Pipeline Setup

1. Install Jenkins on your machine
2. Create a new Pipeline job in Jenkins
3. Set SCM to your GitHub repository
4. Jenkins will automatically use the `Jenkinsfile`

**Pipeline Stages:**
- **Source** → Pull code from GitHub
- **Build** → Build Docker image
- **Test** → Run basic tests
- **Deploy** → Trigger Ansible deployment

---

## 🤖 Step 4 — Ansible Deployment

```bash
# Run the deployment playbook manually
ansible-playbook ansible/deploy.yml -i ansible/inventory
```

---

## 🌐 Access the Application

After deployment:
```
http://localhost:5000
```

---

## 🔄 CI/CD Workflow

```
Developer pushes code → GitHub Webhook → Jenkins triggers
→ Build Docker image → Run tests → Ansible deploys container
→ Application live at http://localhost:5000
```

---

## 📚 Learning Outcomes

- ✅ Web development with Python Flask
- ✅ Database interaction with SQLite
- ✅ Containerization with Docker
- ✅ CI/CD automation with Jenkins
- ✅ Infrastructure automation with Ansible
- ✅ Real-world DevOps lifecycle experience
