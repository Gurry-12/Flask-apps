from app import create_app, db
from app.models import User
from app.security.hashing import hash_password


def create_admin():
    app = create_app()
    with app.app_context():
        if User.query.filter_by(username="admin").first():
            print("Admin user already exists.")
            return
        admin = User(
            username="admin",
            email="admin@example.com",
            role="admin",
            password_hash=hash_password("admin123"),  # Change this in production!
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin user created successfully.")


if __name__ == "__main__":
    create_admin()
