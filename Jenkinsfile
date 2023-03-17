pipeline {
    agent any

    environment {
        PROJECT_ID = 'pourfectpairings'
        IMAGE_NAME = 'pourfectpairings-image'
        SERVICE_NAME = 'pourfectpairings-service'
        REGION = 'us-central1'
    }

    options {
        // Clean the workspace before the build starts
        cleanWs()
    }

    stages {
        stage('Build and Push Docker Image') {
            steps {
                script {
                    withCredentials([file(credentialsId: 'PourfectPairingsFile', variable: 'GC_KEY')]) {
                        sh "cp ${GC_KEY} keyfile.json"
                        sh "/Users/shagun/google-cloud-sdk/bin/gcloud auth activate-service-account --key-file keyfile.json"
                    }
                    sh "docker build -t gcr.io/${PROJECT_ID}/${IMAGE_NAME}:latest ."
                    sh "docker push gcr.io/${PROJECT_ID}/${IMAGE_NAME}:latest"
                }
            }
        }
        stage('Deploy to Cloud Run') {
            steps {
                script {
                    sh "/Users/shagun/google-cloud-sdk/bin/gcloud config set run/region ${REGION}"
                    sh "/Users/shagun/google-cloud-sdk/bin/gcloud config set project ${PROJECT_ID}"
                    sh "/Users/shagun/google-cloud-sdk/bin/gcloud run deploy ${SERVICE_NAME} --image gcr.io/${PROJECT_ID}/${IMAGE_NAME}:latest --platform managed --allow-unauthenticated"
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
