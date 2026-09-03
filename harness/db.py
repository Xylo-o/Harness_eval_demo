from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Run(Base):
    __tablename__= "runs"

    id: Mapped[int]

class TestCase(Base):
    __tablename__= "test_cases"

    id: Mapped[int]

class Result(Base):
    __tablename__= "results"

    id: Mapped[int]

class Score(Base):
    __tablename__= "scores"

    id: Mapped[int]

class FailureLabel(Base):
    __tablename__= "failure_labels"

    id: Mapped[int]
