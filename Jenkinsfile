pipeline {
    agent any

    // Jenkins will poll Git every minute and trigger when it sees a new commit
    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Source already checked out by Jenkins SCM.'
                sh 'ls -la'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                set -e

                echo "Applying Kubernetes manifests..."
                kubectl apply -f k8s/deployment.yaml
                kubectl apply -f k8s/service.yaml

                echo
                echo "Pods:"
                kubectl get pods -l app=devops-lab -o wide || true

                echo
                echo "Services:"
                kubectl get svc
                '''
            }
        }
    }
}
