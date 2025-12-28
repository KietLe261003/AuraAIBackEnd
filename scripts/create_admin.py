"""
Script to create the initial admin user.
Run this script once to create the admin account.

Usage: python scripts/create_admin.py
"""
import asyncio
import sys
import os

# Add parent directory to path to import app modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import select
from app.db.base import async_session_maker
from app.models.user import User
from app.core.security import get_password_hash


async def create_admin_user():
    """Create the initial admin user if not exists."""
    
    admin_email = "admin@auraai.com"
    admin_password = "123456"
    admin_full_name = "Admin User"
    
    async with async_session_maker() as session:
        # Check if admin already exists
        result = await session.execute(
            select(User).where(User.email == admin_email)
        )
        existing_user = result.scalar_one_or_none()
        
        if existing_user:
            print(f"Admin user '{admin_email}' already exists.")
            return
        
        # Create new admin user
        hashed_password = get_password_hash(admin_password)
        admin_user = User(
            email=admin_email,
            hashed_password=hashed_password,
            full_name=admin_full_name,
            is_admin=True
        )
        
        session.add(admin_user)
        await session.commit()
        
        print(f"Admin user created successfully!")
        print(f"Email: {admin_email}")
        print(f"Password: {admin_password}")
        print("Please change the password after first login.")


if __name__ == "__main__":
    asyncio.run(create_admin_user())
