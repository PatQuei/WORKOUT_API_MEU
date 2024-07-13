from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat

class Atleta(BaseModel):
    nome: Annotated[str, Field(description = 'Nome do atleta', examples = 'Joao', max_length=50)]
    cpf: Annotated[str, Field(description = 'CPF do atleta', examples = '123456789', max_length=11)]
    idade: Annotated[int, Field(description = 'Idade do atleta', examples = 37)]
    peso: Annotated[PositiveFloat, Field(description = 'Peso do atleta', examples = 67.5)]
    altura: Annotated[PositiveFloat, Field(description = 'Altura do atleta', examples = 1.57)]
    sexo: Annotated[str, Field(description = 'Sexo do atleta', examples = 'F', max_length=1)]
