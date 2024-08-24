from core.configs import settings

from sqlalchemy import Column, Integer, String


class CursoModel(settings.DBBaseModel):
    __tablename__ = "cursos"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    aulas: int = Column(Integer)
    horas: int = Column(Integer)

    def update_fields(self, **kwargs):
        if kwargs.get("titulo"):
            self.titulo = kwargs.get("titulo")
        if kwargs.get("aulas"):
            self.aulas = kwargs.get("aulas")
        if kwargs.get("horas"):
            self.horas = kwargs.get("horas")
