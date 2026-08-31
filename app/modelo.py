
from datetime import datetime, timezone

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Equipment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    asset_tag = db.Column(db.String(140), nullable=False)
    name = db.Column(db.String(140), nullable=False)
    type = db.Column(db.String(70), nullable=False)
    responsible = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20),nullable=False,default="pendente")
    created_at = db.Column(db.DateTime,default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        return {
            "id": self.id,
            "asset_tag": self.asset_tag,
            "name": self.name,
            "type": self.type,
            "responsible": self.responsible,
            "status": self.status,
            "created_at": (self.created_at.isoformat()if self.created_at else None),
        }