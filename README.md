
# 🛋️ Bespoke Studio  
### AI-Powered Artisan Furniture Marketplace

<div align="center">

**A premium full-stack platform where customers generate custom furniture designs using AI and negotiate directly with artisans in real time.**

🚀 Built with Django • 🎨 AI-driven design • 💬 Real-time negotiation

[✨ Features](#-features) • [🚀 Quick Start](#-quick-start) • [📖 Usage](#-usage-guide) • [🛠 Tech Stack](#-tech-stack) • [📁 Structure](#-project-structure)

</div>

---

## 🌟 Features

### 🧑‍💻 For Customers

- 🎨 **AI Design Studio**  
  Generate custom furniture concepts using AI image models directly from the dashboard.
- 🏺 **Curated Showroom**  
  Browse a premium collection of ready-to-order handcrafted furniture.
- 💾 **Design Vault**  
  Save AI-generated concepts for comparison and future reference.
- 💬 **Live Negotiation**  
  Start real-time chats with artisans linked to specific products or designs.
- 🔗 **Shareable Designs**  
  Share unique item or design links with others.

---

### 🧑‍🎨 For Artisans (Owners)

- 📦 **Inventory Management**  
  Upload furniture items with images, pricing, and availability.
- 🧭 **Command Center Dashboard**  
  Monitor active negotiations and customer requests in real time.
- 🔄 **Stock Control**  
  Toggle availability status instantly.
- 🧾 **Context-Aware Chat**  
  Each chat includes a reference card showing the exact product or design.
- 📊 **Studio Insights**  
  Track active listings and live customer interactions.

---

### ⚙️ Platform Capabilities

- 🔐 **Role-Based Access Control**  
  Separate dashboards for customers and artisans.
- ⚡ **WebSocket-Powered Chat**  
  Instant message updates without page reloads.
- 🎨 **Glassmorphism UI**  
  Modern dark UI with smooth transitions.
- 📱 **Responsive Design**  
  Optimized for desktop browsing and mobile chat.

---

## 🚀 Quick Start

### ✅ Prerequisites

- Python 3.8+
- pip
- Virtual environment (recommended)

---

### 📦 Installation

```bash
git clone https://github.com/salamlakhan7/bespoke-studio.git
cd bespoke-studio
````

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py makemigrations
python manage.py migrate
```

```bash
python manage.py createsuperuser
python manage.py runserver
```

📍 Access:

* App: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Admin: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 📖 Usage Guide

### 👤 Customers

1. Sign up to access the AI Design Studio.
2. Enter prompts to generate multiple furniture concepts.
3. Save selected designs to your vault.
4. Start negotiations with artisans via real-time chat.

---

### 🧑‍🎨 Artisans

1. Register as an artisan to access the dashboard.
2. Upload furniture items and manage stock.
3. Respond to live customer negotiations.
4. Finalize deals using contextual product cards.

---

## 🛠 Tech Stack

### Backend

* **Django 5.2.8**
* **WebSockets (Django Channels)**
* **Pollinations AI API** for image generation
* **SQLite** (local development)
* **Requests, Pillow**

### Frontend

* **Tailwind CSS**
* **HTML5, Vanilla JavaScript**
* **Font Awesome Icons**

---

## 📁 Project Structure

```text
bespoke-studio/
├── b_shop/            # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── studio/            # Core application
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
├── contracts/         # Artisan management
├── media/             # Uploaded images & AI designs
├── manage.py
└── db.sqlite3
```

---

## 🎨 Design Highlights

### 🧠 AI Design Lab

Each prompt generates multiple unique furniture concepts using non-cached seeds for originality.

### 🛒 Contextual Negotiation

Every chat includes a reference card ensuring clarity between buyer and artisan.

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push and open a Pull Request

---

## 📝 License

MIT License

---

## 👤 Author

**Abdul Salam**
Computer Science Graduate
COMSATS University Islamabad (Vehari Campus)
GitHub: [https://github.com/salamlakhan7](https://github.com/salamlakhan7)

---

## 🙏 Acknowledgments

* COMSATS University Islamabad
* Pollinations AI team
* Tailwind CSS community

---

<div align="center">

**Built with passion using Django and AI**

⭐ Star this repo if you find it useful

</div>
```

---

