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

@click.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from blog.models import Tag
    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("created tags")      
     