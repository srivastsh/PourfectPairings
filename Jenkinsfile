pipeline {
    agent any

    environment {
        CLOUDSDK_CORE_DISABLE_PROMPTS = '1'
    }

    stages {
        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    withCredentials([file(credentialsId: 'PourfectPairingsFile', variable: 'GC_KEY')]) {
                        def keyfileContent = readFile("${GC_KEY}")
                        writeFile(file: "keyfile.json", text: keyfileContent)
                        sh "/Users/shagun/google-cloud-sdk/bin/gcloud auth activate-service-account --key-file keyfile.json"
                    }

                    sh "docker build -t gcr.io/pourfect-pairings/pourfect-pairings-backend:latest ."
                    sh "/Users/shagun/google-cloud-sdk/bin/gcloud docker -- push gcr.io/pourfect-pairings/pourfect-pairings-backend:latest"
                }
            }
        }

        stage('Deploy to Cloud Run') {
            steps {
                script {
                    sh "/Users/shagun/google-cloud-sdk/bin/gcloud run deploy pourfect-pairings-backend --image gcr.io/pourfect-pairings/pourfect-pairings-backend:latest --platform managed --region us-central1 --allow-unauthenticated --memory 1Gi"
                }
            }
        }
    }

    post {
        always {
            sh "rm -f keyfile.json"
        }
    }
}
