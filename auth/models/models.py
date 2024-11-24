from pydantic import EmailStr
from sqlalchemy.orm import declarative_base, Mapped, mapped_column



Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False,index=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

