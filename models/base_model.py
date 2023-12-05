#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

class BaseModel():
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = created_at

    def __init__(self):
        self.id = BaseModel.id
        self.created_at = BaseModel.created_at.now()
        self.updated_at = BaseModel.updated_at

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        id = self.id
        created_at = self.created_at
        updated_at = self.updated_at

        return {"id": id, "created_at": created_at.isoformat(), "updated_at": updated_at.isoformat()}

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

