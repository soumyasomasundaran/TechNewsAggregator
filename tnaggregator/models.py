from os import EX_TEMPFAIL
from . import db
from flask_login import UserMixin

class doc_table(db.Model):
    __tabel__ ='doc_table'
    id = db.Column(db.BigInteger,primary_key=True)
    doc_title  = db.Column(db.String(200))
    doc_link = db.Column(db.String(200),unique = True)
    doc_date = db.Column(db.DateTime)
    __table_args__ = (db.UniqueConstraint(doc_title, doc_link, name='uix_1'),)


    def __init__(self, doc_title, doc_link, doc_date):
        self.doc_title = doc_title
        self.doc_link = doc_link
        self.doc_date = doc_date
    def __repr__(self):
        return '<id {}>'.format(self.id)
    

  
class entity_table(db.Model):
    def __init__(self,entity_id,entity_name,entity_type,entity_count):
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.entity_type = entity_type
        self.entity_count = entity_count



    entity_id = db.Column(db.BigInteger,primary_key=True)
    entity_name = db.Column(db.String(200))
    entity_type = db.Column(db.String(50))
    entity_count = db.Column(db.Integer)
    doc_id = db.Column(db.BigInteger,db.ForeignKey('doc_table.id'))

    def __repr__(self):
        return '<id {}>'.format(self.entity_id)
    



class user_table(db.Model,UserMixin):
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
        
        

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    id = db.Column(db.Integer, primary_key = True)
    username= db.Column(db.String(150))
    email = db.Column(db.String(150))
    password = db.Column(db.String(150) )
    is_admin = db.Column(db.Boolean, default = False)
    __table_args__ = (db.UniqueConstraint(username, email, name='uix_2'),)

    


class rss_table(db.Model):
    def __init__(self,rss_id,rss):
        self.rss_id = rss_id
        self.rss = rss
    
    rss_id = db.Column(db.Integer, primary_key = True)
    rss = db.Column(db.String(200),unique = True)


