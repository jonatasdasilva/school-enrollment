from datetime import datetime
from sqlalchemy.orm import registry, Mapped, mapped_column
from sqlalchemy import func, UniqueConstraint


table_registry = registry()


@table_registry.mapped_as_dataclass
class Student:
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    classroom: Mapped[str]
    responsible: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    __table_args__ = (
        UniqueConstraint('name', 'responsible', name='student_unique'),
    )
 