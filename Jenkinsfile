pipeline {
    agent any
    stages {
        stage('Clonar Repositorio') {
            steps {
                git url: 'https://github.com/rsotelo14/pa-dsl.git', branch: 'master'
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                sh 'python3 -m unittest test_usql.py'
            }
        }
        stage('Generar Documentación') {
            steps {
                
                sh 'python3 -m pydoc -w main'
                
                sh 'sudo mv src/main.html /var/www/html/documentins/usql.html'
            }
        }
    }
}
