pipeline {
    agent any
    stages {

        stage('Clone repository') {
            steps {
                checkout scm
            }
        }


        stage('Build') {
            steps { 
                sh "docker-compose build --parallel"
            }
        }
        // stage('Test') {
        //     steps {
        //         //
        //     }
        // }
        // stage('Deploy') {
        //     steps {
        //         //
        //     }
        // }
    }
}