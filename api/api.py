from flask_restful import Api, Resource

# Flask API Configuration
api = Api(
    catch_all_404s=True,
    prefix='/api'
)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
