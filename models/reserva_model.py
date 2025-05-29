from database import db

class Reserva(db.Model):
    __tablename__ = 'reservas'

    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer, nullable=False)
    sala = db.Column(db.String(50), nullable=False)
    data = db.Column(db.DateTime(20), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "turma_id": self.turma_id,
            "sala": self.sala,
            "data": self.data.isoformat() if self.data else None
        }