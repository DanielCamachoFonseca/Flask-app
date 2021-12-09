#En este modulo se almacenan todas las rutas del proyecto

from flask import request, render_template, redirect, flash
from flask.views import MethodView #Este modulo importa la logica de la clase MethodView
from src.db import mysql


class IndexController(MethodView): #Heredo de methodview
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM products")
            data = cur.fetchall() #Crea una tupla con todos los datos de la tabla, y los guardo en la variable data
            cur.execute("SELECT * FROM categories")
            categories = cur.fetchall()
            return render_template('public/index.html', data=data, categories=categories)#renderiza el template html y le pasamos por parametro la variable data, donde se encuentran todos los datos de la tabla

    def post(self):
        code = request.form['code']
        name = request.form['name']
        stock = request.form['stock']
        value = request.form['value']
        category = request.form['category']


        #Guardo los datos del formulario en la base de datos - tabla products
        with mysql.cursor() as cur: #creo un alias a la sentencia mysql.cursor()
            try:
                cur.execute("INSERT INTO products VALUES(%s, %s, %s, %s, %s)", (code, name, stock, value, category)) #Inserto los valores del formulario a la tabla de la base de datos
                cur.connection.commit() #Ejecucion de la sentencia
                flash('El producto ha sido agregado correctamente', 'success')
            except:
                flash('Un error ha ocurrido','error')
            return redirect('/') #Retorno a la pagina principal - Index


class DeleteProductController(MethodView):
    def post(self, code):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM products WHERE code = %s", (code, ))
            cur.connection.commit() #Ejecucion de la sentencia 
            return redirect('/') #Retorno a la pagina principal - Index

    
class UpdateProductController(MethodView):
    def get(self, code):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM products WHERE code = %s", (code, ))
            product = cur.fetchone()#Recibe el primer dato que encuentre de acuerdo a la condicion sql
            print(product)
            return render_template('public/update.html', product = product)

    def post(self, code):
        productCode = request.form['code']
        name = request.form['name']
        stock = request.form['stock']
        value = request.form['value']

        with mysql.cursor() as cur:
            cur.execute("UPDATE products SET code = %s, name = %s, stock = %s, value = %s WHERE code = %s", (productCode, name, stock, value, code))
            cur.connection.commit()
        return f"Editing product {code} works!"

class CreateCategoriesController(MethodView):
    def get(self):
        return render_template("public/categories.html")

    def post(self):
        id = request.form['id']
        name = request.form['name']
        description = request.form['description']

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO categories VALUES(%s, %s, %s)", (id, name, description))
            cur.connection.commit()
        return "Success!"

