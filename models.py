from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    role = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=func.now())

class Room(Base):
    __tablename__ = "rooms"
    room_id = Column(Integer, primary_key=True, index=True)
    room_number = Column(String(20), nullable=False)
    building = Column(String(100), nullable=False)
    floor_number = Column(Integer, nullable=False)

class Ticket(Base):
    __tablename__ = "tickets"
    ticket_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    room_id = Column(Integer, ForeignKey("rooms.room_id"))
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(String(20), default="open")
    priority = Column(String(10), default="medium")
    progress_percentage = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.now())