pipeline {
    agent any

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
                echo "Applying Kubernetes manifests..."
                kubectl apply -f k8s/deployment.yaml
                kubectl apply -f k8s/service.yaml

                echo "Pods:"
                kubectl get pods
                echo "Services:"
                kubectl get svc
                '''
            }
        }
    }
}
