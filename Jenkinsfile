pipeline {
    agent any

    // Single source of truth for the trigger
    triggers {
        // poll git every minute
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
                echo "Applying Kubernetes manifests..."
                kubectl apply -f k8s/deployment.yaml
                kubectl apply -f k8s/service.yaml

                echo "Pods:"
                kubectl get pods -l app=devops-lab
                echo "Services:"
                kubectl get svc
                '''
            }
        }
    }
}
