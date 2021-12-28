from enum import unique
from . import db


class Doc_table(db.Model):
    __tablename__ = 'doc_table'
    id = db.Column(db.BigInteger,primary_key=True)
    doc_title  = db.Column(db.String(200))
    doc_link = db.Column(db.String(200),unique = True)
    doc_date = db.Column(db.Date)

    

  
class Entity_table(db.Model):
    entity_id = db.Column(db.BigInteger,primary_key=True)
    entity_name = db.Column(db.String(200))
    entity_type = db.Column(db.String(50))
    entity_count = db.Column(db.Integer)
    doc_id = db.Column(db.BigInteger,db.ForeignKey('doc_table.id'))






    




