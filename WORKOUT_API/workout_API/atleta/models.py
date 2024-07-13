from datetime import datetime
from workout_API.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, Integer, String, ForeignKey
from workout_API.categorias.models import CategoriaModel
from workout_API.centro_de_treinamento.models import CentroTreinamentoModel

class AtletaMoidel(BaseModel):
    __tablename__='atletas'

    pk_id = Mapped[int] = mapped_column(Integer, primary_key=True)
    nome = Mapped[str] = mapped_column(String(50), nullable=False)
    cpf = Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade= Mapped[int] = mapped_column(Integer, nullable=False)
    peso= Mapped[float] = mapped_column(float, nullable=False)
    altura= Mapped[float] = mapped_column(float, nullable=False)
    sexo = Mapped[str] = mapped_column(String(1), nullable=False)
    created_at = Mapped[datetime] = mapped_column(DateTime, nullable=False)
    categoria: Mapped['CategoriaModel'] = relationship (back_populates = 'atleta')
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categoria.pk_id'))
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship (back_populates = 'atleta')
    centros_treinamento_id: Mapped[int] = mapped_column(ForeignKey('centro_de_treinamento.pk_id'))