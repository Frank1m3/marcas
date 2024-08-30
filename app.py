from flask import Flask, render_template, request, redirect, url_for,flash
from dao.MarcaDao import MarcaDao

app = Flask(__name__)

# flash requiere esta sentencia
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/marcas-index')
def marcas_index():
    # Creacion de la instancia 
    marcasDao = MarcaDao()
    lista_marcas = marcasDao.getMarcas()
    return render_template('marcas-index.html', lista_marcas=lista_marcas)

@app.route('/marcas')
def marcas():
    return render_template('marcas.html')

@app.route('/guardar-marca', methods=['POST'])
def guardarMarca():
    marca = request.form.get('txtDescripcion').strip()
    if marca == None or len(marca) < 1:
        # mostrar un mensaje al usuario
        flash('Debe escribir algo en la descripcion', 'warning')

       
        return redirect(url_for('marcas'))

    marcadao = MarcaDao()
    marcadao.guardarMarca(marca.upper())

    # mostrar un mensaje al usuario
    flash('Guardado exitoso', 'success')

    # redireccionar a la vista ciudades
    return redirect(url_for('marcas_index'))

@app.route('/marcas-editar/<id>')
def marcasEditar(id):
    marcadao = MarcaDao()
    return render_template('marcas-editar.html', marca=marcadao.getMarcaById(id))


@app.route('/actualizar-marca', methods=['POST'])
def actualizarMarca():
    id = request.form.get('txtIdMarca')
    descripcion = request.form.get('txtDescripcion').strip()

    if descripcion == None or len(descripcion) == 0:
        flash('No debe estar vacia la descripcion')
        return redirect(url_for('marcasEditar', id=id))

    # actualizar
    marcadao = MarcaDao()
    marcadao.updateMarca(id, descripcion.upper())

    return redirect(url_for('marcas_index'))

@app.route('/marcas-eliminar/<id>')
def marcasEliminar(id):
    marcadao = MarcaDao()
    marcadao.deleteMarca(id)
    return redirect(url_for('marcas_index'))

# se pregunta por el proceso principal
if __name__=='__main__':
    app.run(debug=True)