# 🧸 Toyshop

<img src="https://github.com/user-attachments/assets/d020f64f-b908-4833-8df2-1990acf29ec1" alt="Toyshop ER Diagram" width="600"/>

**Toyshop** is an online toy store built with Django 5.2.  
It allows users to register, log in, browse toys by categories, and place orders. Admins can manage toys, categories, and orders through the admin panel.

---

## 🚀 Features

- 🔐 User authentication and registration  
- 📧 Email verification via SMTP  
- 🧸 Toy catalog with categories  
- 📦 Image upload with automatic resizing (Pillow)  
- ☁️ Dropbox media storage  
- 🧑‍💼 Admin panel for managing the store  
- 💌 Flash messages via Django messages framework  
- 💅 Styled forms using Django Crispy Forms + Tailwind (crispy-tailwind)  
- ⚡ HTMX for partial page updates and dynamic interactions  
- 🧰 Django Debug Toolbar for development insights  
- 🛠️ Environment management via django-environ  

---

## 🧠 Tech Stack

- **Python** `3.13+`
- **Django** `5.2`
- **Tailwind CSS** (via `crispy-tailwind`)
- **Dropbox** (via `django-storages`)
- **Pillow** for image processing
- **Ruff** for code linting
- **uv** — fast Python package manager

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/kram3ko/toys-shop.git
cd toys-shop
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install uv and project dependencies

```bash
pip install uv
uv sync
```

---

## 🔐 Environment Setup

Create a `.env` file in the root of the project with the following content:

```env
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost

# DB Settings
Your db settings

# Email (Gmail SMTP)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password

#DROPBOX SETTING
oauth2_access_token=

oauth2_refresh_token=
app_key=
app_secret=


```

---

## 🧪 Running the Project

```bash
python manage.py migrate
python manage.py loaddata toys_fixture.json
python manage.py createsuperuser
python manage.py runserver
   
```

```
Defualt users
login: customer@toyshop.com - registered base customer
login: shop_admin@toyshop.com - Shop adminstator with rules
login: admin@toyshop.com - super admin
password: toyshop0987
 

```
---

## 🧼 Code Style

```bash
ruff check .
ruff format .
```

---

## 📚 Resources

- [ER Diagram](https://dbdiagram.io/d/Toyshop-67eaf48b4f7afba184dacbc3)
- [Dropbox Storage Docs](https://django-storages.readthedocs.io/en/latest/backends/dropbox.html)
- [Gmail SMTP Setup](https://support.google.com/mail/answer/7126229?hl=en)

---

## 👤 Author

**Volodymyr Vynohradov**  
[GitHub](//https://github.com/kram3ko/)

---

## 📄 License

This project is licensed under the MIT License.
