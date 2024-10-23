# main.py

from translator import translate_usql_to_sql

def main():
    print("Bienvenido al traductor de USQL a SQL.")
    print("Escribe tu consulta USQL y presiona Enter. Escribe 'salir' para terminar.\n")

    while True:
        usql_query = input("USQL> ")
        if usql_query.lower() == 'salir':
            print("Saliendo del traductor. ¡Hasta luego!")
            break
        try:
            sql_query = translate_usql_to_sql(usql_query)
            print(f"SQL> {sql_query}\n")
        except SyntaxError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"Error inesperado: {e}\n")

if __name__ == '__main__':
    main()
