pipeline {
    agent any

    stages {
        stage('Build and Push Docker Image') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'PourfectPairings', variable: 'GOOGLE_APPLICATION_CREDENTIALS_JSON')]) {
                        sh 'echo "$GOOGLE_APPLICATION_CREDENTIALS_JSON" > gcp-key.json'
                        sh 'gcloud auth activate-service-account --key-file=gcp-key.json'
                        sh 'gcloud config set project pourfectpairings'
                        sh 'gcloud auth configure-docker'
                        sh 'docker build -t gcr.io/pourfectpairings/pourfectpairings .'
                        sh 'docker push gcr.io/pourfectpairings/pourfectpairings'
                    }
                }
            }
        }
        stage('Deploy to Cloud Run') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'PourfectPairings', variable: 'GOOGLE_APPLICATION_CREDENTIALS_JSON')]) {
                        sh 'echo "$GOOGLE_APPLICATION_CREDENTIALS_JSON" > gcp-key.json'
                        sh 'gcloud auth activate-service-account --key-file=gcp-key.json'
                        sh 'gcloud config set project pourfectpairings'
                        sh 'gcloud run deploy pourfectpairings --image gcr.io/pourfectpairings/pourfectpairings --platform managed --region us-central1 --allow-unauthenticated'
                    }
                }
            }
        }
    }
}
