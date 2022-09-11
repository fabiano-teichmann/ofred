from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship


class BaseModel(object):
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(300), nullable=True)


class Domains(BaseModel, AuditMixin, Model):
    def __repr__(self):
        return self.name.__str__()


class Applications(BaseModel, AuditMixin, Model):
    def __repr__(self):
        return self.name.__str__()


class Events(BaseModel, AuditMixin, Model):
    req_path = Column(String, nullable=True)
    application_id = Column(Integer, ForeignKey(Applications.id))
    application_tbl = relationship('Applications', foreign_keys='Events.application_id')
    domain_id = Column(Integer, ForeignKey(Domains.id))
    domain_tbl = relationship('Domains', foreign_keys='Events.domain_id')
    fields_pii_req_body = Column(String, nullable=True)
    req_body = Column(Text, nullable=False)
    fields_pii_resp_body = Column(String, nullable=True)
    resp_body = Column(Text, nullable=True)

    def __repr__(self):
        return self.name.__str__()
