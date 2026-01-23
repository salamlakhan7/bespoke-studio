🛋️ Bespoke Studio: AI-Powered Artisan Marketplace
<div align="center">

A high-end furniture ecosystem where customers visualize custom designs using generative AI and negotiate directly with master artisans.

Core Features • Tech Stack • Installation • User Flow

</div>

🌟 Core Features
🎨 For Customers (The Design Lab)
🧠 AI Concept Generator - Generate high-fidelity furniture designs using Flux AI models directly from the dashboard.

🔒 Design Vault - Save and categorize generated concepts for future reference or negotiation.

🛋️ Premium Showroom - Browse ready-to-ship handcrafted furniture with an immersive, visual-first UI.

💬 Smart Negotiation - Initiate chats that automatically reference specific items, including AI-generated designs.

⚒️ For Artisans (Command Center)
📊 Artisan Dashboard - Manage all active customer inquiries and live negotiations in one central hub.

📦 Inventory Management - List new stock, update pricing, and manage availability for the public showroom.

🔗 Contextual Chat - View exactly which product or AI concept a customer is referencing via "Daraz-style" item cards.

📱 Real-time Sync - WebSocket-powered messaging for instant price locking and design approval.

🛠️ Tech Stack
Backend & AI
Django 5.2.8 - Core framework for robust marketplace logic.

Pollinations AI API - Powering the Flux image generation engine.

Django Channels - Handling asynchronous WebSocket communication for chat.

Memurai/Redis - Real-time message brokering and session management.

Frontend & Design
Tailwind CSS - Modern utility-first styling for a sleek, dark-mode aesthetic.

Glassmorphism UI - High-end visual effects with backdrop blurs and translucent panels.

AJAX / JavaScript - Seamless, non-refreshing interactions for the "Save to Vault" and "Copy URL" features.

🚀 Installation
Clone the repository

Bash

git clone https://github.com/salamlakhan7/bespoke-studio.git
cd bespoke-studio
Setup Environment

Bash

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
Database & Admin

Bash

python manage.py migrate
python manage.py createsuperuser
Launch Application

Bash

# Use Daphne for WebSocket support
daphne -b 127.0.0.1 -p 8000 b_shop.asgi:application
📖 User Flow
Code snippet

graph TD
    A[Customer Dashboard] --> B[AI Image Generation]
    B --> C[Save to Vault]
    C --> D[Initiate Negotiation]
    D --> E[Artisan Context Card]
    E --> F[Price Approval & Sale]
👥 Authors
Abdul Salam - Initial Work & Architecture - salamlakhan7.

<div align="center">

Made with ❤️ for the COMSATS Final Year Project

⭐ Star this repo if you find this AI implementation useful!

</div>
