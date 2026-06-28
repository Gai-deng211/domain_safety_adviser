from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, UTC

from .base import Base

class Domain(Base):
    __tablename__ = "domains"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    domain: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    registered_on: Mapped[str | None] = mapped_column(String(25), nullable=True)
    expires_on: Mapped[str | None] = mapped_column(String(25), nullable=True)
    updated_on: Mapped[str | None] = mapped_column(String(25), nullable=True)
    registrar: Mapped[str | None] = mapped_column(String(255), nullable=True)
    registrant_organization: Mapped[str | None] = mapped_column(String(255), nullable=True)
    registrant_country: Mapped[str | None] = mapped_column(String(255), nullable=True)
    status: Mapped[str | None] = mapped_column(String(255), nullable=True)
    user_name: Mapped[str | None] = mapped_column(String(255), nullable=True, default=None)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)