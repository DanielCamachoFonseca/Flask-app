#Modulo que se encarga de almacenar los errores
from flask.views import MethodView

class NotFoundController(MethodView):
    def get(self, error):
        return f'Page not found {error}'