from app import db

class NetworkTraffic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    src_ip = db.Column(db.String(50))
    dst_ip = db.Column(db.String(50))
    protocol = db.Column(db.String(10))
    packet_size = db.Column(db.Integer)

class Threat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    threat_level = db.Column(db.String(10))
    src_ip = db.Column(db.String(50))
    dst_ip = db.Column(db.String(50))
    action_taken = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime)
