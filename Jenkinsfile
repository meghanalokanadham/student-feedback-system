pipeline {
    agent any

    environment {
        IMAGE_NAME = 'student-feedback-app'
        CONTAINER_NAME = 'feedback-container'
        APP_PORT = '5000'
    }

    stages {

        stage('Source') {
            steps {
                echo '=== Stage 1: Pulling source code from GitHub ==='
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo '=== Stage 2: Building Docker Image ==='
                sh 'docker build -t ${IMAGE_NAME}:latest .'
            }
        }

        stage('Test') {
            steps {
                echo '=== Stage 3: Running Basic Tests ==='
                sh '''
                    docker run --rm ${IMAGE_NAME}:latest python -c "
import sys
sys.path.insert(0, '/app/app')
from database import init_db
init_db()
print('Database initialization: PASSED')
print('All tests passed successfully!')
"
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo '=== Stage 4: Deploying via Ansible ==='
                sh 'ansible-playbook ansible/deploy.yml -i ansible/inventory'
            }
        }

    }

    post {
        success {
            echo '✅ Pipeline completed successfully! App is running at http://localhost:5000'
        }
        failure {
            echo '❌ Pipeline failed. Check the logs above for errors.'
        }
    }
}
