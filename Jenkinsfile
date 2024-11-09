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
                
                sh 'mv main.html /var/www/html/documentins/usql.html'
            }
        }
		stage('Send Email') {
            steps {
                emailext(
                    subject: "Actualizacion en USQL",
                    body: "Se acaba de hacer una actualización en el repositorio del proyecto de USQL. Para ver la nueva documentación vaya a http://ec2-34-201-54-91.compute-1.amazonaws.com",
                    to: "rsotelosilva@gmail.com",
                    from: "rsotelosilva@gmail.com"
                )
            }
        }

    }
}
