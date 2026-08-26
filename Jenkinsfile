pipeline {

    agent any

    environment {
        APP_NAME = "employee-management"

        IMAGE_NAME = "employee-management"
        IMAGE_TAG = "${BUILD_NUMBER}"

        CONTAINER_NAME = "employee-management"

        HOST_PORT = "8000"
        CONTAINER_PORT = "8000"

        DOCKER_NETWORK = "employee-network"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Checking out source code..."

                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    set -e

                    echo "Python version:"
                    python3 --version

                    echo "Creating virtual environment..."

                    python3 -m venv venv

                    . venv/bin/activate

                    echo "Python version inside virtual environment:"
                    python --version

                    echo "Pip version:"
                    pip --version

                    echo "Upgrading pip..."

                    pip install --upgrade pip

                    echo "Installing dependencies..."

                    pip install -r requirements.txt
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    set -e

                    echo "Building Docker image..."

                    docker build \
                        -t ${IMAGE_NAME}:${IMAGE_TAG} \
                        -t ${IMAGE_NAME}:latest \
                        .

                    echo "Docker image created successfully."

                    docker images ${IMAGE_NAME}
                '''
            }
        }

        stage('Deploy') {
            steps {

                withCredentials([
                    string(
                        credentialsId: 'employee-db-username',
                        variable: 'DB_USERNAME'
                    ),
                    string(
                        credentialsId: 'employee-db-password',
                        variable: 'DB_PASSWORD'
                    ),
                    string(
                        credentialsId: 'employee-db-name',
                        variable: 'DB_NAME'
                    )
                ]) {

                    sh '''
                        set -e

                        echo "Starting deployment..."

                        echo "Checking Docker network..."

                        if ! docker network inspect ${DOCKER_NETWORK} >/dev/null 2>&1; then
                            echo "Docker network ${DOCKER_NETWORK} does not exist."
                            echo "Creating Docker network..."

                            docker network create ${DOCKER_NETWORK}
                        else
                            echo "Docker network ${DOCKER_NETWORK} already exists."
                        fi

                        echo "Checking MySQL container..."

                        if docker ps --format '{{.Names}}' | grep -q "^mysql-server$"; then
                            echo "MySQL container is running."
                        else
                            echo "WARNING: mysql-server is not currently running."
                        fi

                        echo "Connecting MySQL container to network..."

                        docker network connect ${DOCKER_NETWORK} mysql-server 2>/dev/null || true

                        echo "Stopping existing application container..."

                        docker stop ${CONTAINER_NAME} 2>/dev/null || true

                        echo "Removing existing application container..."

                        docker rm ${CONTAINER_NAME} 2>/dev/null || true

                        echo "Starting new application container..."

                        docker run -d \
                            --name ${CONTAINER_NAME} \
                            --network ${DOCKER_NETWORK} \
                            -p ${HOST_PORT}:${CONTAINER_PORT} \
                            -e DATABASE_URL="$DATABASE_URL" \
                            ${IMAGE_NAME}:${IMAGE_TAG}

                        echo "Application container started."

                        echo "Waiting for application to start..."

                        sleep 5

                        echo "Checking container status..."

                        if [ "$(docker inspect -f '{{.State.Running}}' ${CONTAINER_NAME})" = "true" ]; then
                            echo "Application container is running successfully."
                        else
                            echo "Application container failed to start."
                            echo "Container logs:"
                            docker logs ${CONTAINER_NAME}
                            exit 1
                        fi

                        echo "Running containers:"

                        docker ps --filter "name=${CONTAINER_NAME}"

                        echo "Deployment completed successfully."
                    '''
                }
            }
        }
    }

    post {

        success {
            echo "========================================="
            echo "Build ${BUILD_NUMBER} completed successfully."
            echo "Application deployed successfully."
            echo "Application: ${APP_NAME}"
            echo "Container: ${CONTAINER_NAME}"
            echo "Port: ${HOST_PORT}"
            echo "========================================="
        }

        failure {
            echo "========================================="
            echo "Build ${BUILD_NUMBER} failed."
            echo "Please check the Jenkins console output."
            echo "========================================="
        }

        always {
            echo "Cleaning Jenkins workspace..."

            cleanWs()
        }
    }
}