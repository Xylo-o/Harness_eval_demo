from sqlalchemy import JSON, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import os



class Base(DeclarativeBase):
    pass


class Run(Base):
    __tablename__= "runs"

    id: Mapped[int]
    suite_name: Mapped[str]
    model_name: Mapped[str]
    model_version: Mapped[int]
    started_at: Mapped[int]
    finished_at: Mapped[int]
    git_sha: Mapped[str]


class TestCase(Base):
    __tablename__= "test_cases"

    id: Mapped[int]
    suite_name: Mapped[str]
    prompt: Mapped[str]
    metadata: Mapped[dict] = mapped_column(JSON)
    scorer_config: Mapped[dict] = mapped_column(JSON)


class Result(Base):
    __tablename__= "results"

    id: Mapped[int]
    run_id: Mapped[int]
    test_case_id: Mapped[int]
    raw_response: Mapped[str]
    latency_ms: Mapped[float]
    tokens_in: Mapped[int]
    tokens_out: Mapped[int]
    cost: Mapped[int]


class Score(Base):
    __tablename__= "scores"

    id: Mapped[int]
    result_id: Mapped[int]
    scorer_name: Mapped[str]
    passed: Mapped[bool]
    score: Mapped[float]
    detail: Mapped[dict] = mapped_column(JSON)


class FailureLabel(Base):
    __tablename__= "failure_labels"

    id: Mapped[int]
    result_id: Mapped[int]
    category: Mapped[str]
    note: Mapped[str]

engine = create_engine(os.getenv("DATABASE_URL"), echo=True)
Base.metadata.create_all(engine)