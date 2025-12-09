"""Database configuration for the Book API."""

from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite database URL. Database file will be created in the current directory.
DATABASE_URL = "sqlite:///./books.db"

# For SQLite + FastAPI we need check_same_thread=False.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# Session factory used in FastAPI dependencies.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models.
Base = declarative_base()
