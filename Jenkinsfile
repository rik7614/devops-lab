pipeline {
    agent any

    // 👇 This makes Jenkins automatically check GitHub every minute
    triggers {
        // Poll SCM roughly every 1 minute
        pollSCM('H/1 * * * *')
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
