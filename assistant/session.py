from agents import SQLiteSession

from assistant.config import DATABASE_PATH, SESSION_ID


def create_session():
    return SQLiteSession(
        SESSION_ID,
        DATABASE_PATH,
    )
