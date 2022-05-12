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
                sh "ln -s MakeMeASinger/docker-compose.yml builds"
            }
        }
        stage('Test') {
            steps {
                sh "bash test.sh"
            }
        }    
    
        stage('Deploy') {
               steps {
                sh "scp -i ~/ansible_id_rsa docker-compose.yaml managers:/home/jenkins/docker-compose.yml"
                sh "scp -i ~/ansible_id_rsa nginx.conf managers:/home/jenkins/nginx.conf"
                sh "ansible-playbook -i configuration/inventory.yaml configuration/playbook.yml"
            }
        }
    }
}
