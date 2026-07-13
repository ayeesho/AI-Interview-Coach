import sqlite3
import os
import json
from datetime import datetime

# ==========================================================
# DATABASE LOCATION
# ==========================================================

DB_FOLDER = "database"
DB_NAME = os.path.join(DB_FOLDER, "interview.db")

os.makedirs(DB_FOLDER, exist_ok=True)


# ==========================================================
# CONNECTION
# ==========================================================

def get_connection():
    return sqlite3.connect(DB_NAME)


# ==========================================================
# CREATE TABLES
# ==========================================================

def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    # ------------------------------------------------------
    # USERS TABLE
    # ------------------------------------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL

    )
    """)

    # ------------------------------------------------------
    # INTERVIEWS TABLE
    # ------------------------------------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interviews(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT NOT NULL,

        company TEXT NOT NULL,

        role TEXT NOT NULL,

        difficulty TEXT NOT NULL,

        topics TEXT NOT NULL,

        interview_date TEXT NOT NULL,

        overall_score REAL,

        technical_score REAL,

        communication_score REAL,

        confidence_score REAL,

        feedback TEXT,

        conversation TEXT

    )
    """)

    conn.commit()
    conn.close()


# ==========================================================
# USER FUNCTIONS
# ==========================================================

def create_user(username, email, password):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("""

        INSERT INTO users(username,email,password)

        VALUES(?,?,?)

        """, (username, email, password))

        conn.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        conn.close()


def login_user(username, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT * FROM users

    WHERE username=? AND password=?

    """, (username, password))

    user = cursor.fetchone()

    conn.close()

    return user


# ==========================================================
# SAVE INTERVIEW
# ==========================================================

def save_interview(

        username,
        company,
        role,
        difficulty,
        topics,
        overall_score,
        technical_score,
        communication_score,
        confidence_score,
        feedback,
        conversation

):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO interviews(

        username,

        company,

        role,

        difficulty,

        topics,

        interview_date,

        overall_score,

        technical_score,

        communication_score,

        confidence_score,

        feedback,

        conversation

    )

    VALUES(?,?,?,?,?,?,?,?,?,?,?,?)

    """, (

        username,

        company,

        role,

        difficulty,

        json.dumps(topics),

        datetime.now().strftime("%Y-%m-%d %H:%M"),

        overall_score,

        technical_score,

        communication_score,

        confidence_score,

        feedback,

        json.dumps(conversation)

    ))

    conn.commit()
    conn.close()


# ==========================================================
# GET USER INTERVIEWS
# ==========================================================

def get_interviews(username):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM interviews

    WHERE username=?

    ORDER BY id DESC

    """, (username,))

    data = cursor.fetchall()

    conn.close()

    return data

# ==========================================================
# INTERVIEW HISTORY
# ==========================================================

def get_interview_history(username):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM interviews
        WHERE username=?
        ORDER BY interview_date DESC
    """, (username,))

    history = cursor.fetchall()

    conn.close()

    return history

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM interviews

    WHERE username=?

    ORDER BY id DESC

    """, (username,))

    data = cursor.fetchall()

    conn.close()

    return data

# ==========================================================
# DASHBOARD ANALYTICS
# ==========================================================

def get_average_score(username):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT AVG(overall_score)

    FROM interviews

    WHERE username=?

    """, (username,))

    score = cursor.fetchone()[0]

    conn.close()

    if score is None:
        return 0

    return round(score, 2)


def get_best_score(username):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT MAX(overall_score)

    FROM interviews

    WHERE username=?

    """, (username,))

    score = cursor.fetchone()[0]

    conn.close()

    if score is None:
        return 0

    return round(score, 2)


def get_total_interviews(username):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT COUNT(*)

    FROM interviews

    WHERE username=?

    """, (username,))

    count = cursor.fetchone()[0]

    conn.close()

    return count


# ==========================================================
# DELETE INTERVIEW
# ==========================================================

def delete_interview(interview_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    DELETE FROM interviews

    WHERE id=?

    """, (interview_id,))

    conn.commit()
    conn.close()


# ==========================================================
# DATABASE INITIALIZATION
# ==========================================================

initialize_database()

