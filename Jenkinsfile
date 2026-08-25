pipeline {

    agent any

    environment {
        APP_NAME = "employee-management"
        IMAGE_NAME = "employee-management"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build \
                        -t ${IMAGE_NAME}:${IMAGE_TAG} \
                        -t ${IMAGE_NAME}:latest \
                        .
                '''
            }
        }
    }

    post {

        success {
            echo "Build ${BUILD_NUMBER} completed successfully."
        }

        failure {
            echo "Build ${BUILD_NUMBER} failed."
        }

        always {
            echo "Cleaning workspace..."
            cleanWs()
        }
    }
}