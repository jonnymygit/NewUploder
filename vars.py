#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "21805580"))
API_HASH = environ.get("API_HASH", "b008874785e462ece4a6a2fbb2023824")
BOT_TOKEN = environ.get("BOT_TOKEN", "8446886102:AAGLAmarErqrKQaYQgP8pL601ZUE6o2mJ00")

OWNER = int(environ.get("OWNER", "7192966134"))
CREDIT = environ.get("CREDIT", "200")

TOTAL_USER = os.environ.get('TOTAL_USERS', '').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set





