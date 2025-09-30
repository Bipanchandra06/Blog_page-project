#  Blog Post Website  

A feature-rich blogging platform built with **Django** (backend) and **Bootstrap** (frontend) that allows users to create, share, and interact with blog posts.  

##  Features  

- **User Authentication**  
  - Sign up, log in, and log out  
  - Secure password management  
  - Profile page with editable details & avatar  

- **Blog Management**  
  - Create, update, and delete blog posts  
  - Rich text formatting (Markdown/HTML supported)  
  - Upload images for posts  

- **Post Interaction**  
  - Like/unlike posts  
  - View post details  

- **Filtering & Categories**  
  - Browse posts by categories  
  - Search posts by keywords  
  - Sort by date, popularity, or author  

- **Responsive UI**  
  - Built with **Bootstrap 5** for modern, mobile-friendly layouts  
  - Clean and intuitive design  

##  Tech Stack  

- **Backend**: Django (Python)  
- **Frontend**: HTML, CSS, Bootstrap  
- **Database**: SQLite (default) 
- **Authentication**: Django’s built-in user auth system  

## ⚙️ Installation  
# 1. Clone the repository
git clone https://github.com/yourusername/blogsite.git
cd blogsite

# 2. Create a virtual environment & activate it
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser (admin account)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver

Now open http://127.0.0.1:8000/
 in your browser

REST API for mobile integration

