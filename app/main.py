
import os

from flask import Flask, jsonify, request
from flasgger import Swagger
from app.modelo import Equipment, db


def create_monitoring_TI(test_config=None):
    app = Flask(__name__)
    Swagger(app)

    database_url = os.environ.get(
        "DATABASE_URL",
        "sqlite:///equipment.db"
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.get("/health")
    def health():
        """
        Verifica se a API está funcionando.
        ---
        responses:
          200:
            description: API funcionando corretamente
            schema:
              type: object
              properties:
                status:
                  type: string
                  example: ok
        """
        return jsonify(status="ok"), 200

    @app.get("/equipment")
    def list_equipment():
        """
    Lista todos os equipamentos.
    ---
    responses:
      200:
        description: Lista de equipamentos
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              asset_tag:
                type: string
                example: PAT-001
              name:
                type: string
                example: Notebook Dell
              type:
                type: string
                example: Notebook
              responsible:
                type: string
                example: Pablo
              status:
                type: string
                example: ativo
    """
        equipment = Equipment.query.order_by(Equipment.id).all()

        return jsonify(
            [item.to_dict() for item in equipment]
        ), 200

    @app.post("/equipment")
    def create_equipment():
        payload = request.get_json(silent=True) or {}

        name = payload.get("name")
        responsible = payload.get("responsible")

        if not name or not responsible:
            return jsonify(error="Campo incompleto"), 400

        equipment = Equipment(
            name=name,
            responsible=responsible,
            asset_tag=payload.get("asset_tag"),
            type=payload.get("type"),
            status=payload.get("status", "pendente"),
        )

        db.session.add(equipment)
        db.session.commit()

        return jsonify(
            message="Equipamento cadastrado com sucesso.",
            equipment=equipment.to_dict()
        ), 201



    @app.get("/equipment/<int:equipment_id>")
    def get_equipment(equipment_id):
        equipment = db.session.get(Equipment, equipment_id)

        if not equipment:
            return jsonify(error="Equipamento não encontrado."), 404

        return jsonify(equipment.to_dict()), 200


    #CONTINUANDO A DESENVOLVER OS RESTANTES DAS ROTAS. 

    @app.put("/equipment/<int:equipment_id>")
    def put_equipment(equipment_id):
        equipment = db.session.get(Equipment, equipment_id)

        if not equipment:
            return jsonify(error="Equipamento não encontrado."), 404

        payload = request.get_json(silent = True) or {}
        equipment.name = payload.get("name", equipment.name)
        equipment.responsible = payload.get("responsible", equipment.responsible)
        equipment.status = payload.get("status", equipment.status)
        db.session.commit()

        return jsonify(message="Equipamento atualizado com sucesso.",equipment=equipment.to_dict()), 200

    @app.delete("/equipment/<int:equipment_id>")
    def delete_equipment(equipment_id):
        equipment = db.session.get(Equipment, equipment_id)

        if not equipment: 
            return jsonify(error="Equipamento não encontrado."), 404
        
        db.session.delete(equipment)
        db.session.commit()
        return jsonify(message="Equipamento Excluido com Sucesso"),200

    return app
