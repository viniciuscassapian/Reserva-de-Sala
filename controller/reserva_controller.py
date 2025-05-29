from models.reserva_model import Reserva
from database import db
from flask import jsonify
import requests
from datetime import datetime

def validar_turma(turma_id):
    try:
        resp = requests.get(f"http://localhost:5000/turmas/{turma_id}")
        return resp.status_code == 200
    except requests.exceptions.RequestException:
        return False

def criar_reserva(data):
    turma_id = data.get("turma_id")

    if not validar_turma(turma_id):
        return jsonify({"erro": "Turma não encontrada"}), 400

    # Converter data para datetime, se for string
    data_str = data.get("data")
    data_obj = None
    if data_str:
        try:
            data_obj = datetime.fromisoformat(data_str)
        except ValueError:
            return jsonify({"erro": "Formato de data inválido. Use ISO 8601"}), 400

    reserva = Reserva(
        turma_id=turma_id,
        sala=data.get("sala"),
        data=data_obj,
    )

    db.session.add(reserva)
    db.session.commit()

    return jsonify(reserva.to_dict()), 201  # Retorna o objeto criado em JSON

def listar_reservas():
    reservas = Reserva.query.all()
    # Use o to_dict() para serializar os objetos
    return jsonify([r.to_dict() for r in reservas])

def buscar_reserva_por_id(reserva_id):
    reserva = Reserva.query.get(reserva_id)

    if not reserva:
        return jsonify({"erro": "Reserva não encontrada"}), 404

    return jsonify(reserva.to_dict()), 200

def deletar_reserva(reserva_id):
    reserva = Reserva.query.get(reserva_id)

    if not reserva:
        return jsonify({"erro": "Reserva não encontrada"}), 404
    
    db.session.delete(reserva)
    db.session.commit()

    return jsonify({"mensagem": "Reserva deletada com sucesso"}), 200
