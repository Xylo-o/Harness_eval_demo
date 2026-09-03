import os
from datetime import datetime
from sqlalchemy import JSON, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Run(Base):
    __tablename__ = "runs"

    id: Mapped[int] = mapped_column(primary_key=True)
    suite_name: Mapped[str]
    model_name: Mapped[str]
    model_version: Mapped[str]
    started_at: Mapped[datetime] = mapped_column(default=datetime.now)
    finished_at: Mapped[datetime | None]
    git_sha: Mapped[str]


class TestCase(Base):
    __tablename__ = "test_cases"

    id: Mapped[int] = mapped_column(primary_key=True)
    suite_name: Mapped[str]
    prompt: Mapped[str]
    case_metadata: Mapped[dict] = mapped_column(JSON)
    scorer_config: Mapped[dict] = mapped_column(JSON)


class Result(Base):
    __tablename__ = "results"

    id: Mapped[int] = mapped_column(primary_key=True)
    run_id: Mapped[int] = mapped_column(ForeignKey("runs.id"))
    test_case_id: Mapped[int] = mapped_column(ForeignKey("test_cases.id"))
    timeouted: Mapped[bool]
    raw_response: Mapped[str]
    latency_ms: Mapped[int]
    tokens_in: Mapped[int | None]
    tokens_out: Mapped[int | None]
    cost: Mapped[float | None]


class Score(Base):
    __tablename__ = "scores"

    id: Mapped[int] = mapped_column(primary_key=True)
    result_id: Mapped[int] = mapped_column(ForeignKey("results.id"))
    scorer_name: Mapped[str]
    passed: Mapped[bool | None]
    score: Mapped[float]
    detail: Mapped[dict] = mapped_column(JSON)


class FailureLabel(Base):
    __tablename__ = "failure_labels"

    id: Mapped[int] = mapped_column(primary_key=True)
    result_id: Mapped[int] = mapped_column(ForeignKey("results.id"))
    category: Mapped[str]
    note: Mapped[str]

engine = create_engine(os.getenv("DATABASE_URL", "sqlite///harness.db"), echo=True)
Base.metadata.create_all(engine)

