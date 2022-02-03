from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

class Evento(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column ( db.String(100) )
    categoria = db.Column ( db.String(20) ) # Conferencia, Seminario, Congreso Curso
    lugar = db.Column ( db.String(100) )
    direccion = db.Column ( db.String(250) )
    fechaInicio = db.Column ( db.String(10) )
    fechaFin = db.Column ( db.String(10) )


class Evento_Schema(ma.Schema):
    class Meta:
        fields = ("id", "nombre", "categoria","lugar","direccion","fechaInicio","fechaFin")

post_schema = Evento_Schema()

posts_schema = Evento_Schema(many = True)

class ListarEventos(Resource):
    def get(self):
        eventos = Evento.query.all()
        return posts_schema.dump(eventos)
    def post(self):
        nuevo_evento = Evento(nombre = request.json['nombre'], categoria = request.json['categoria']
        , lugar = request.json['lugar'], direccion = request.json['direccion']
        , fechaInicio = request.json['fechaInicio'], fechaFin = request.json['fechaFin'])
        db.session.add(nuevo_evento)
        db.session.commit()
        return post_schema.dump(nuevo_evento)
class ListarEvento(Resource):
    def get(self, id_evento):
        evento = Evento.query.get_or_404(id_evento)
        return post_schema.dump(evento)
    def put(self, id_evento):
        evento = Evento.query.get_or_404(id_evento)
        if 'nombre' in request.json:
            evento.nombre = request.json['nombre']
        if 'categoria' in request.json:
            evento.categoria = request.json['categoria']
        if 'lugar' in request.json:
            evento.lugar = request.json['lugar']
        if 'direccion' in request.json:
            evento.direccion = request.json['direccion']
        if 'fechaInicio' in request.json:
            evento.fechaInicio = request.json['fechaInicio']
        if 'fechaFin' in request.json:
            evento.fechaFin = request.json['fechaFin']
        db.session.commit()
        return post_schema.dump(evento)
    def delete(self, id_evento):
        evento = Evento.query.get_or_404(id_evento)
        db.session.delete(evento)
        db.session.commit()
        return '', 204
            
                    
api.add_resource(ListarEventos,'/eventos')
api.add_resource(ListarEvento, '/eventos/<int:id_evento>')


if __name__ == '__main__':
    
 app.run(host="172.24.41.200", port="5000",debug=True)
