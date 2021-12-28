from enum import unique
from . import db

class doc_table(db.Model):
    __tabel__ ='doc_table'
    id = db.Column(db.BigInteger,primary_key=True)
    doc_title  = db.Column(db.String(200))
    doc_link = db.Column(db.String(200),unique = True)
    doc_date = db.Column(db.String(10))

    def __init__(self, doc_title, doc_link, doc_date):
        self.doc_title = doc_title
        self.doc_link = doc_link
        self.doc_date = doc_date

    def __repr__(self):
        return '<id {}>'.format(self.id)
    

  
class entity_table(db.Model):
    entity_id = db.Column(db.BigInteger,primary_key=True)
    entity_name = db.Column(db.String(200))
    entity_type = db.Column(db.String(50))
    entity_count = db.Column(db.Integer)
    doc_id = db.Column(db.BigInteger,db.ForeignKey('doc_table.id'))





    




