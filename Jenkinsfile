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
                sh "docker-compose --version"
                sh "sudo su jenkins"
                sh "sudo docker-compose up --build -d"
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