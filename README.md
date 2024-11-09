#Entregable 3: DSL

## Estudiante: Rodrigo Sotelo


### Instrucciones de uso para los tests unitarios y el programa principal

En los test unitarios se encuentran todos los ejemplos listados en la letra del entregable, así como tests adicionales para probar la funcionalidad de la FluentAPI.

Para ejecutar los test unitarios, se debe ejecutar el siguiente comando en la terminal:

```bash
$ python3 -m unittest test_usql.py
```

Si se desea ejecutar un test en específico, se debe ejecutar el siguiente comando en la terminal:

```bash
$ python3 -m unittest test_usql.TestUsql.test_<nombre_del_test>
```

Se realizó una consola interactiva que traduce el input del usuario USQL a SQL.
Para ejecutar el programa principal, se debe ejecutar el siguiente comando en la terminal:

```bash
$ python3 main.py
```

Se le mostrará un mensaje de bienvenida y podrá empezar a escribir su código USQL. Para salir de la consola interactiva, se debe escribir `salir`.

### Cobertura de código

Para obtener la cobertura de código, se debe instalar la librería `coverage` con el siguiente comando:

```bash
$ pip3 install coverage
```


Para obtener el reporte de cobertura, se debe ejecutar el siguiente comando en la terminal:

```bash
$ coverage run -m unittest test_usql.py
$ coverage report -m
```
Aquí se muestra la cobertura de código de los tests unitarios.

| Archivo              | Stmts | Miss | Cover | Missing                              |
|----------------------|-------|------|-------|--------------------------------------|
| fluent_api.py         | 56    | 17   | 70%   | 21-23, 26-27, 30-32, 35-36, 39-40, 43-44, 66-67, 74 |
| keyword_mapping.py    | 2     | 0    | 100%  | -                                    |
| lexer.py              | 87    | 10   | 89%   | 135, 168, 172-173, 181-186           |
| parser.py             | 109   | 17   | 84%   | 31, 37, 47-50, 134, 138, 162, 170, 191, 197, 210, 213-217 |
| parsetab.py           | 18    | 0    | 100%  | -                                    |
| test_usql.py          | 72    | 1    | 99%   | 99                                   |
| translator.py         | 8     | 2    | 75%   | 11-12                                |
| **TOTAL**             | 352   | 47   | 87%   | -                                    |
