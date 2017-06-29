from app.blog import Blog
from database import Database
from menu import Menu

Database.initialize()

menu = Menu()

menu.run_menu()
