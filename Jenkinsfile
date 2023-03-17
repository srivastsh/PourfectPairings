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
                    withCredentials([[$class: 'GoogleRobotPrivateKeyCredentials', credentialsId: 'PourfectPairings']]) {
                        sh 'gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS'
                    }
                    sh "gcloud builds submit --tag gcr.io/$PROJECT_ID/$IMAGE_NAME ."
                }
            }
        }
        stage('Deploy to Cloud Run') {
            steps {
                script {
                    sh "gcloud run deploy $SERVICE_NAME --image gcr.io/$PROJECT_ID/$IMAGE_NAME --platform managed --region $REGION --allow-unauthenticated"
                }
            }
        }
    }
}
