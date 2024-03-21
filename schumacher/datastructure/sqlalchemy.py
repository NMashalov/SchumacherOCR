from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey,String
from sqlalchemy import engine


class Base(DeclarativeBase):
    pass

class WorkBook(Base):
    __tablename__ = "workbook"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    name: Mapped[str] = mapped_column(String(30))



class Illustration(Base):
    __tablename__ = "timetable"
    id: Mapped[int] = mapped_column(primary_key=True)