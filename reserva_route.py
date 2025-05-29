from flask import Blueprint, request
from controller.reserva_controller import (
    criar_reserva,
    listar_reservas,
    deletar_reserva,
    buscar_reserva_por_id
)

routes = Blueprint("routes", __name__)

# Rota para criar uma nova reserva
@routes.route("/reservas", methods=["POST"])
def post_reserva():
    return criar_reserva(request.json)

# Rota para listar todas as reservas
@routes.route("/reservas", methods=["GET"])
def get_reservas():
    return listar_reservas()

# Rota para buscar uma reserva específica por ID
@routes.route("/reservas/<int:reserva_id>", methods=["GET"])
def get_reserva_por_id(reserva_id):
    return buscar_reserva_por_id(reserva_id)

# Rota para deletar uma reserva por ID
@routes.route("/reservas/<int:reserva_id>", methods=["DELETE"])
def delete_reserva(reserva_id):
    return deletar_reserva(reserva_id)
