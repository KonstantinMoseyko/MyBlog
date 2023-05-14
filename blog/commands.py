import os
import click
from blog.models.database import db


@click.command("create-admin")
def create_admin():
    """
    Run in your terminal:
    ➜ flask create-admin
    > created admin: <User #1 'admin'>
    """
    from blog.models import User
    
    admin = User(username="admin", is_staff=True)
    admin.password = os.getenv("ADMIN_PASSWORD") or "adminpass"
    
    db.session.add(admin)
    db.session.commit()
    
    print("created admin:", admin)
        