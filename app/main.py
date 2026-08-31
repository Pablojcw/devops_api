
import os

from flask import Flask, jsonify, request

from app.modelo import Equipment, db


def create_monitoring_TI(test_config=None):
    app = Flask(__name__)

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
        return jsonify(status="ok"), 200

    @app.get("/equipment")
    def list_equipment():
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

        return jsonify(equipment.to_dict()), 201

    @app.get("/equipment/<int:equipment_id>")
    def get_equipment(equipment_id):
        equipment = db.session.get(Equipment, equipment_id)

        if not equipment:
            return jsonify(
                error="Equipamento não encontrado."
            ), 404

        return jsonify(equipment.to_dict()), 200

    return app
