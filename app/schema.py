from pydantic import BaseModel,PositiveFloat
from typing import Optional

class ProdutosSchema(BaseModel):
    id: int
    titulo: str 
    descricao: Optional[str] = None
    preco: PositiveFloat