# 🛋️ Bespoke Studio - AI-Powered Artisan Furniture Marketplace

<div align="center">

**A high-end, full-stack marketplace enabling customers to generate custom furniture designs using AI and negotiate directly with artisans through real-time communication.**

[Features](https://www.google.com/search?q=%23-features) • [Screenshots](https://www.google.com/search?q=%23-screenshots) • [Installation](https://www.google.com/search?q=%23-installation) • [Usage](https://www.google.com/search?q=%23-usage) • [Tech Stack](https://www.google.com/search?q=%23-tech-stack)

</div>

---

## 🌟 Features

### For Customers

* 🎨 **AI Design Studio** - Generate high-fidelity furniture concepts using Flux AI models directly from your dashboard.
* 🏺 **Showroom Access** - Browse a premium collection of ready-to-ship handcrafted inventory.
* 💾 **Design Vault** - Save your favorite AI-generated concepts to a personal gallery for later review.
* 💬 **Smart Negotiation** - Initiate discussions with artisans that automatically reference specific products or AI designs.
* 🔗 **Shareable Links** - Copy unique item URLs to share specific designs or showroom pieces with others.

### For Artisans (Owners)

* 📢 **Inventory Management** - List new furniture items with high-resolution images, descriptions, and pricing.
* 👥 **Command Center** - Monitor all active customer inquiries and live negotiations from a central dashboard.
* ✅ **Availability Toggle** - Manage stock status with "In Stock" and "Sold Out" indicators in real-time.
* 💬 **Contextual Chat** - View exactly which product or concept a customer is inquiring about via "Reference Cards".
* 📈 **Studio Analytics** - Track the total number of live negotiations and active inventory items.

### Platform Features

* 🔐 **Secure Role-Based Access** - Distinct dashboards and permissions for Master Artisans and Customers.
* ⚡ **Real-time Messaging** - Instant chat synchronization for seamless price negotiations.
* 🎨 **Glassmorphism UI** - Modern, premium aesthetic with dark-mode panels and smooth CSS animations.
* 📱 **Adaptive Design** - Fully optimized experience for desktop showroom browsing and mobile chat.

---

## 🚀 Quick Start

### Prerequisites

* Python 3.8 or higher
* pip (Python package manager)
* Virtual environment (recommended)

### Installation

1. **Clone the repository**
```bash
 git clone https://github.com/salamlakhan7/bespoke-studio.git
 cd bespoke-studio

```


2. **Create and activate virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

```


3. **Install dependencies**
```bash
pip install -r requirements.txt

```


4. **Run database migrations**
```bash
python manage.py makemigrations
python manage.py migrate

```


5. **Create a superuser (admin)**
```bash
python manage.py createsuperuser

```


6. **Run the development server**
```bash
python manage.py runserver

```


7. **Access the application**
* Main site: `http://127.0.0.1:8000`
* Admin panel: `http://127.0.0.1:8000/admin`



---

## 📖 Usage Guide

### For Customers

1. **Join the Studio** - Sign up as a customer to access the Design Lab.
2. **Generate Designs** - Use the "New Design" tab to enter prompts and generate 5 unique furniture iterations.
3. **Save to Vault** - Save concepts you love; they will appear in your "Saved Concepts" gallery.
4. **Negotiate** - Click "Negotiate" on any showroom item or saved design to start a chat with the artisan.

### For Artisans

1. **Register as Artisan** - Create an owner account to access the Command Center.
2. **Update Showroom** - Use "Manage Inventory" to upload new furniture pieces.
3. **Live Chat** - Monitor the "Live Negotiations" list to respond to customer inquiries.
4. **Finalize Deals** - Use the contextual product cards in chat to confirm which item is being sold.

---

## 🛠️ Tech Stack

### Backend

* **Django 5.2.8** - High-level Python web framework.
* **Pollinations AI API** - Image generation engine for furniture visualization.
* **SQLite** - Database used for local storage of inventory and user designs.
* **Requests/Pillow** - Handling external API calls and image processing.

### Frontend

* **Tailwind CSS** - Modern utility-first CSS for premium styling.
* **HTML5 & Vanilla JS** - Structure and AJAX-based "Save to Vault" functionality.
* **FontAwesome** - Professional iconography for UI elements.

---

## 📁 Project Structure

```
bespoke-studio/
├── b_shop/                        # Project configuration
│   ├── settings.py                # Django settings
│   ├── urls.py                    # Main URL routing
│   └── wsgi.py                    # WSGI config
├── studio/                        # Main Application
│   ├── templates/                 # HTML UI layers
│   │   ├── studio/                # Customer & Showroom templates
│   │   └── registration/          # Auth templates
│   ├── models.py                  # DB Models (StockItem, DesignConcept)
│   ├── views.py                   # AI & Shop Logic
│   └── forms.py                   # Stock & Signup forms
├── contracts/                     # Artisan Management
│   ├── templates/                 # Artisan Dashboard templates
│   └── ...
├── media/                         # User-uploaded furniture & AI designs
├── manage.py                      # Management script
└── db.sqlite3                     # Local Database

```

---

## 🎨 Features in Detail

### AI Design Lab

The system uses millisecond-precision seeds to ensure that every furniture prompt generates five unique, non-cached variations for the user.

### "Daraz-Style" Referencing

When a negotiation starts, the platform creates a "Reference Card" at the top of the chat. This ensures both parties are looking at the same item, price, and image throughout the discussion.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewStyle`)
3. Commit your changes (`git commit -m 'Add New furniture Style'`)
4. Push to the branch (`git push origin feature/NewStyle`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

---

## 👥 Authors

* **Abdul Salam** - *Initial Architecture* - [salamlakhan7](https://github.com/salamlakhan7)

---

## 🙏 Acknowledgments

* COMSATS University Islamabad, Vehari Campus
* The Pollinations AI team for the Flux API
* Tailwind CSS community for the design inspiration

---

<div align="center">

**Made with ❤️ using Django & AI**

⭐ Star this repo if you find it helpful!

</div>

