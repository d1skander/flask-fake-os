from models.user import Base, db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func


class MessageInChat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    message: Mapped[str]
    username: Mapped[str]
    date = Column(DateTime(timezone=True), server_default=func.now())