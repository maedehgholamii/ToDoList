from sqlalchemy import Column
from model.entity import *

class AddTask(Base):
    __tablename__ = "add_task"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(20), nullable=False)

