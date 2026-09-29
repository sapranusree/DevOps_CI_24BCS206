pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'python -m compileall src'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m unittest discover -s tests -v'
            }
        }

        stage('Result') {
            steps {
                echo 'Cinema Ticket Booking CI completed successfully.'
            }
        }
    }
}