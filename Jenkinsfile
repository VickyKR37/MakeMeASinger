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
                sh "ln -s MakeMeASinger/docker-compose.yml build"
            }
        }
        stage('Test') {
            steps {
                sh "bash test.sh"
            }
        }    
    
        // stage('Deploy') {
        //     steps {
        //         //
        //     }
        // }
    }
}