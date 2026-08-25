pipeline {

    agent any

    environment {
        APP_NAME = "employee-management"
        IMAGE_NAME = "employee-management"
        IMAGE_TAG = "${BUILD_NUMBER}"
        CONTAINER_NAME = "employee-management"
        HOST_PORT = "8000"
        CONTAINER_PORT = "8000"
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

                    python --version
                    pip --version

                    pip install --upgrade pip
                    pip install -r requirements.txt
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

        stage('Deploy') {
            steps {
                sh '''
                    echo "Stopping existing container..."

                    docker stop ${CONTAINER_NAME} || true

                    echo "Removing existing container..."

                    docker rm ${CONTAINER_NAME} || true

                    echo "Starting new container..."

                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        -p ${HOST_PORT}:${CONTAINER_PORT} \
                        ${IMAGE_NAME}:${IMAGE_TAG}

                    echo "Deployment completed."

                    docker ps --filter "name=${CONTAINER_NAME}"
                '''
            }
        }
    }

    post {

        success {
            echo "Build ${BUILD_NUMBER} completed successfully."
            echo "Application deployed successfully."
        }

        failure {
            echo "Build ${BUILD_NUMBER} failed."
        }

        always {
            cleanWs()
        }
    }
}