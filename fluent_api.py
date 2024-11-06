# fluent_api.py

class QueryBuilder:
    def __init__(self):
        self.query = ""

    def select(self, *args):
        columns = ', '.join(args) if args else 'TODO'
        self.query += f"TRAEME {columns} "
        return self

    def from_table(self, table_name):
        self.query += f"DE LA TABLA {table_name} "
        return self

    def where(self, condition):
        self.query += f"DONDE {condition} "
        return self

    def group_by(self, *args):
        columns = ', '.join(args)
        self.query += f"AGRUPANDO POR {columns} "
        return self

    def having(self, condition):
        self.query += f"WHERE DEL GROUP BY {condition} "
        return self

    def order_by(self, *args):
        columns = ', '.join(args)
        self.query += f"ORDENA POR {columns} "
        return self

    def limit(self, number):
        self.query += f"COMO MUCHO {number} "
        return self

    def join(self, table_name):
        self.query += f"MEZCLANDO {table_name} "
        return self

    def on(self, condition):
        self.query += f"EN {condition} "
        return self

    def insert_into(self, table_name, *columns):
        cols = ', '.join(columns)
        self.query += f"METE EN {table_name} ({cols}) "
        return self

    def values(self, *values):
        vals = ', '.join(values)
        self.query += f"LOS VALORES ({vals}) "
        return self

    def update(self, table_name):
        self.query += f"ACTUALIZA {table_name} "
        return self

    def set(self, **kwargs):
        assignments = ', '.join([f"{k} = {v}" for k, v in kwargs.items()])
        self.query += f"SETEA {assignments} "
        return self

    def delete_from(self, table_name):
        self.query += f"BORRA DE LA {table_name} "
        return self

    def build(self):
        self.query = self.query.strip() + ";"
        return self.query

    def __str__(self):
        return self.build()
