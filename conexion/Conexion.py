import psycopg2

class Conexion:

    """Metodo constructor
    """
    def __init__(self):
        self.con = psycopg2.connect("dbname=examenfinal user=postgres host=localhost password=postgres port=5433")

    """getConexion

        retorna la instancia de la base de datos
    """
    def getConexion(self):
        return self.con