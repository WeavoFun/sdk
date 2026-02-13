from pydantic import BaseModel

class Transaction(BaseModel):
    id: int
    notional: float
    gas_fee: float
    actor: str
