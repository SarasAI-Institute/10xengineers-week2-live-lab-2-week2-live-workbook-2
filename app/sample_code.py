# Sample code for testing your custom agents
# Use your documentation agent to document this code
# Use your review agent to find issues

from typing import List, Optional
from datetime import datetime


class UserManager:
    def __init__(self):
        self.users = {}
        self.sessions = {}
    
    def create_user(self, username, email, password):
        if username in self.users:
            return None
        user = {
            "id": len(self.users) + 1,
            "username": username,
            "email": email,
            "password": password,  # Issue: storing plain text password
            "created_at": datetime.now()
        }
        self.users[username] = user
        return user
    
    def authenticate(self, username, password):
        user = self.users.get(username)
        if user and user["password"] == password:
            session_id = f"sess_{len(self.sessions)}"
            self.sessions[session_id] = username
            return session_id
        return None
    
    def get_user(self, username):
        return self.users.get(username)
    
    def delete_user(self, username):
        if username in self.users:
            del self.users[username]
            # Issue: doesn't clean up sessions
            return True
        return False
    
    def list_users(self):
        return list(self.users.values())


def calculate_age(birth_year):
    return datetime.now().year - birth_year


def format_users_report(users, include_email=True):
    lines = []
    for u in users:
        line = f"User: {u['username']}"
        if include_email:
            line += f" ({u['email']})"
        lines.append(line)
    return "\n".join(lines)


def validate_email(email):
    # Issue: very basic validation
    return "@" in email


def search_users(users, query):
    results = []
    q = query.lower()
    for u in users:
        if q in u["username"].lower() or q in u["email"].lower():
            results.append(u)
    return results

