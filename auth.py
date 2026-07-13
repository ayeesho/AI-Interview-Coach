import bcrypt
import sqlite3
from database.database import get_connection
DB_PATH = "database/interview.db"


def create_user(username, email, password):

    conn = get_connection()
    cursor = conn.cursor()

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    try:

        cursor.execute("""
        INSERT INTO users(username,email,password)
        VALUES(?,?,?)
        """, (
            username,
            email,
            hashed_password
        ))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def login_user(email, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, username, password
    FROM users
    WHERE email=?
    """, (email,))

    user = cursor.fetchone()

    conn.close()

    if user:

        stored_password = user[2]

        if bcrypt.checkpw(
            password.encode(),
            stored_password
        ):
            return user

    return None