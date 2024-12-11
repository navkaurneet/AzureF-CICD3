pipeline {
    agent any
/*
    environment {
        // Azure credentials
        AZURE_CLIENT_ID = credentials('azure-client-id')
        AZURE_CLIENT_SECRET = credentials('azure-client-secret')
        AZURE_TENANT_ID = credentials('azure-tenant-id')
        RESOURCE_GROUP = 'your-resource-group-name'  // Replace with your Azure resource group name
        FUNCTION_APP_NAME = 'your-function-app-name'  // Replace with your Azure Function App name
    }
*/
    stages {
        stage('Checkout') {
            steps {
                script {
                    echo 'Checking out the repository...'
                    // Clone public repository without credentials
                    git url: 'https://github.com/navkaurneet/AzureF-CICD3.git'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    sh 'pytest tests/'  // Assuming you have a tests directory and pytest set up
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying to Azure...'
                    sh """
                        az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID
                        zip -r function.zip . 
                        az functionapp deployment source config-zip --resource-group $RESOURCE_GROUP --name $FUNCTION_APP_NAME --src function.zip
                    """
                }
            }
        }
    }
}
