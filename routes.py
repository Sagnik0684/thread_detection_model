from flask import request, jsonify, render_template
from models import NetworkTraffic, Threat
from app import db

def initialize_routes(app):
    @app.route('/')
    def dashboard():
        return render_template('dashboard.html')

    @app.route('/api/upload', methods=['POST'])
    def upload_data():
        data = request.json
        traffic = NetworkTraffic(**data)
        db.session.add(traffic)
        db.session.commit()
        return jsonify({"message": "Data uploaded successfully!"}), 201

    @app.route('/api/alerts', methods=['GET'])
    def get_alerts():
        alerts = Threat.query.all()
        return jsonify([alert.to_dict() for alert in alerts])
