pipeline {
    agent any
    environment {
        GCLOUD_PROJECT = 'pourfect-pairings'
        SERVICE_NAME = 'pourfect-pairings-backend'
    }
    stages {
        stage('Clean Workspace') {
            steps {
                deleteDir()
                checkout scm
            }
        }
        stage('List Workspace Contents') {
            steps {
                sh 'ls -la'
            }
        }
        stage('Build and Push Docker Image') {
            steps {
                script {
                    withCredentials([file(credentialsId: 'google-cloud-key', variable: 'GC_KEY')]) {
                        writeFile file: 'keyfile.json', text: readFile(GC_KEY)
                        sh '/Users/shagun/google-cloud-sdk/bin/gcloud auth activate-service-account --key-file keyfile.json'
                    }
                    sh 'docker build -t gcr.io/${GCLOUD_PROJECT}/${SERVICE_NAME}:latest .'
                    sh '/Users/shagun/google-cloud-sdk/bin/gcloud docker -- push gcr.io/${GCLOUD_PROJECT}/${SERVICE_NAME}:latest'
                }
            }
        }
        stage('Deploy to Cloud Run') {
            steps {
                script {
                    sh '/Users/shagun/google-cloud-sdk/bin/gcloud run deploy ${SERVICE_NAME} --image gcr.io/${GCLOUD_PROJECT}/${SERVICE_NAME}:latest --platform managed --region us-central1 --allow-unauthenticated --project ${GCLOUD_PROJECT}'
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
