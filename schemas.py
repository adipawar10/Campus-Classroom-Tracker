from pydantic import BaseModel

# This defines exactly what data we expect when creating a user
class UserCreate(BaseModel):
    name: str
    email: str
    role: str

# Schema for creating a Room
class RoomCreate(BaseModel):
    room_number: str
    building: str
    floor_number: int

# Schema for creating a Ticket
class TicketCreate(BaseModel):
    user_id: int
    room_id: int
    title: str
    description: str
    priority: str = "medium"