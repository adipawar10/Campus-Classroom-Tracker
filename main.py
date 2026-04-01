from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, get_db
import models
import schemas
from fastapi.middleware.cors import CORSMiddleware

# 1. Create the app FIRST
app = FastAPI(title="Campus Tracker API")

# 2. Now you can add the middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows your React app to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# This links your SQLAlchemy models to the engine
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "API is successfully connected to the database!"}

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # This takes the data from the web and translates it into your database model
    new_user = models.User(name=user.name, email=user.email, role=user.role)
    
    # This saves it to Postgres
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

# --- ROOM ENDPOINTS ---
@app.post("/rooms")
def create_room(room: schemas.RoomCreate, db: Session = Depends(get_db)):
    new_room = models.Room(
        room_number=room.room_number, 
        building=room.building, 
        floor_number=room.floor_number
    )
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room

@app.get("/rooms")
def get_rooms(db: Session = Depends(get_db)):
    return db.query(models.Room).all()

# --- TICKET ENDPOINTS ---
@app.post("/tickets")
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    new_ticket = models.Ticket(
        user_id=ticket.user_id,
        room_id=ticket.room_id,
        title=ticket.title,
        description=ticket.description,
        priority=ticket.priority
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

# To see the tickets we created earlier
@app.get("/tickets")
def get_tickets(db: Session = Depends(get_db)):
    return db.query(models.Ticket).all()