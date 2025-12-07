pipeline {
    agent any

    // Jenkins will poll GitHub every minute
    triggers {
        pollSCM('* * * * *')
    }

    environment {
        DOCKER_IMAGE = 'rik7614/devops-lab'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Source already checked out by Jenkins SCM.'
                sh 'ls -la'
            }
        }

        stage('Build & Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-hub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh """
                        echo "Logging into Docker Hub..."
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin

                        echo "Building image: ${DOCKER_IMAGE}:${BUILD_NUMBER}"
                        docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .

                        echo "Tagging as latest..."
                        docker tag ${DOCKER_IMAGE}:${BUILD_NUMBER} ${DOCKER_IMAGE}:latest

                        echo "Pushing image tags..."
                        docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                        docker push ${DOCKER_IMAGE}:latest

                        docker logout
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh """
                echo "Applying Kubernetes manifests (in case resources don't exist)..."
                kubectl apply -f k8s/deployment.yaml
                kubectl apply -f k8s/service.yaml

                echo "Updating Deployment to use image tag: ${BUILD_NUMBER}"
                kubectl set image deployment/devops-lab devops-lab=${DOCKER_IMAGE}:${BUILD_NUMBER} --record

                echo "Waiting for rollout to finish..."
                kubectl rollout status deployment/devops-lab

                echo "Pods:"
                kubectl get pods -l app=devops-lab

                echo "Services:"
                kubectl get svc
                """
            }
        }
    }
}
