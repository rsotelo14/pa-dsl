import unittest
from translator import translate_usql_to_sql
from fluent_api import QueryBuilder

class TestUSQL(unittest.TestCase):
    def test_select_query(self):
        usql = "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;"
        sql = translate_usql_to_sql(usql)
        expected_sql = "SELECT * FROM usuarios WHERE edad > 18;"
        self.assertEqual(sql, expected_sql)

    def test_distinct_query(self):
        usql = "TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid';"
        sql = translate_usql_to_sql(usql)
        expected_sql = "SELECT DISTINCT nombre FROM clientes WHERE ciudad = 'Madrid';"
        self.assertEqual(sql, expected_sql)

    def test_insert_query(self):
        usql = "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25);"
        sql = translate_usql_to_sql(usql)
        expected_sql = "INSERT INTO usuarios (nombre , edad) VALUES ('Juan' , 25);"
        self.assertEqual(sql, expected_sql)

    def test_update_query(self):
        usql = "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';"
        sql = translate_usql_to_sql(usql)
        expected_sql = "UPDATE empleados SET salario = 3000  WHERE puesto = 'ingeniero';"
        self.assertEqual(sql, expected_sql)

    def test_join_query(self):
        usql = "TRAEME TODO DE LA TABLA pedidos MEZCLANDO clientes EN pedidos.cliente_id = clientes.id DONDE clientes.ciudad = 'Barcelona';"
        sql = translate_usql_to_sql(usql)
        expected_sql = "SELECT * FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id WHERE clientes.ciudad = 'Barcelona';"
        self.assertEqual(sql, expected_sql)

    def test_group_by_query(self):
        usql = "TRAEME CONTANDO(TODO) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY CONTANDO(*) > 5;"
        sql = translate_usql_to_sql(usql)
        expected_sql = "SELECT COUNT(*) FROM ventas GROUP BY producto HAVING COUNT(*) > 5;"
        self.assertEqual(sql, expected_sql)

    def test_delete_query(self):
        usql = "BORRA DE LA TABLA clientes DONDE edad ENTRE 18 AND 25;"
        sql = translate_usql_to_sql(usql)
        expected_sql = "DELETE FROM clientes  WHERE edad BETWEEN 18 AND 25;"
        self.assertEqual(sql, expected_sql)

    def test_alter_add_column(self):
        usql = "CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO;"
        sql = translate_usql_to_sql(usql)
        expected_sql = "ALTER TABLE empleados ADD COLUMN direccion VARCHAR(255) NOT NULL;"
        self.assertEqual(sql, expected_sql)

    def test_alter_drop_column(self):
        usql = "CAMBIA LA TABLA empleados ELIMINA LA COLUMNA direccion;"
        sql = translate_usql_to_sql(usql)
        expected_sql = "ALTER TABLE empleados DROP COLUMN direccion;"
        self.assertEqual(sql, expected_sql)

    # Incluye tus otras pruebas aquí

    def test_fluent_api_select(self):
        query = (QueryBuilder()
                 .select("nombre")
                 .from_table("clientes")
                 .where("ciudad = 'Madrid'")
                 .build())
        expected_usql = "TRAEME nombre DE LA TABLA clientes DONDE ciudad = 'Madrid';"
        self.assertEqual(query, expected_usql)
        sql = translate_usql_to_sql(query)
        expected_sql = "SELECT nombre FROM clientes WHERE ciudad = 'Madrid';"
        self.assertEqual(sql, expected_sql)

    def test_fluent_api_insert(self):
        query = (QueryBuilder()
                 .insert_into("usuarios", "nombre", "edad")
                 .values("'Juan'", "25")
                 .build())
        expected_usql = "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25);"
        self.assertEqual(query, expected_usql)
        sql = translate_usql_to_sql(query)
        expected_sql = "INSERT INTO usuarios (nombre , edad) VALUES ('Juan' , 25);"
        self.assertEqual(sql, expected_sql)

    def test_fluent_api_update(self):
        query = (QueryBuilder()
                 .update("empleados")
                 .set(salario=3000)
                 .where("puesto = 'ingeniero'")
                 .build())
        expected_usql = "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';"
        self.assertEqual(query, expected_usql)
        sql = translate_usql_to_sql(query)
        expected_sql = "UPDATE empleados SET salario = 3000  WHERE puesto = 'ingeniero';"
        self.assertEqual(sql, expected_sql)


if __name__ == '__main__':
    unittest.main()
