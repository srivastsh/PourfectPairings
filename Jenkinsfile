pipeline {
    agent any

    environment {
        PROJECT_ID = 'pourfectpairings'
        IMAGE_NAME = 'pourfectpairings-image'
        SERVICE_NAME = 'pourfectpairings-service'
        REGION = 'us-central1'
    }

    stages {
        stage('Build and Push Docker Image') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'PourfectPairings', variable: 'GC_KEY')]) {
                        sh "echo '$GC_KEY' > keyfile.json"
                        sh "gcloud auth activate-service-account --key-file keyfile.json"
                    }
                    sh "docker build -t gcr.io/${PROJECT_ID}/${IMAGE_NAME}:latest ."
                    sh "docker push gcr.io/${PROJECT_ID}/${IMAGE_NAME}:latest"
                }
            }
        }
        stage('Deploy to Cloud Run') {
            steps {
                script {
                    sh "gcloud config set run/region ${REGION}"
                    sh "gcloud config set project ${PROJECT_ID}"
                    sh "gcloud run deploy ${SERVICE_NAME} --image gcr.io/${PROJECT_ID}/${IMAGE_NAME}:latest --platform managed --allow-unauthenticated"
                }
            }
        }
    }

    post {
        always {
            sh 'rm -f keyfile.json'
        }
    }
}
