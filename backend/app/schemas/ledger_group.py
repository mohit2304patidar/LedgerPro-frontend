from pydantic import BaseModel

class LedgerGroupCreate(BaseModel):
    name: str
    parent_group: str | None = None
    nature: str

class LedgerGroupResponse(LedgerGroupCreate):
    id: int

    class Config:
        from_attributes = True