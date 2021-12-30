#Modulo que se encarga de almacenar los errores
from flask.views import MethodView
from flask import render_template

class NotFoundController(MethodView):
    def get(self, error):
        return render_template("public/404.html", error=error)