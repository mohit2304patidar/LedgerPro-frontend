from pydantic import BaseModel

class UnitCreate(BaseModel):
    name: str
    symbol: str