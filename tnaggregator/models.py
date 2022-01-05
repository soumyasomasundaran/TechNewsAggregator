from . import db
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from . import app

class doc_table(db.Model):
    __tabel__ ='doc_table'
    id = db.Column(db.BigInteger,primary_key=True)
    doc_title  = db.Column(db.String(200))
    doc_link = db.Column(db.String(200),unique = True)
    doc_date = db.Column(db.DateTime)
    doc_summary = db.Column(db.TEXT)
    __table_args__ = (db.UniqueConstraint(doc_title, doc_link, name='uix_1'),)


    def __init__(self, doc_title, doc_link, doc_date,doc_summary):
        self.doc_title = doc_title
        self.doc_link = doc_link
        self.doc_date = doc_date
        self.doc_summary = doc_summary
        
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

    def get_reset_token(self,expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'],expires_sec)
        return s.dumps({'user_id':self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return user_table.query.get(user_id)

class rss_table(db.Model):
    def __init__(self,rss_id,rss):
        self.rss_id = rss_id
        self.rss = rss
    
    rss_id = db.Column(db.Integer, primary_key = True)
    rss = db.Column(db.String(200),unique = True)


