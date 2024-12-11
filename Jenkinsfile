pipeline {
    agent any
/*    environment {
        // Define any necessary environment variables here
        AZURE_CLIENT_ID = credentials('azure-client-id')
        AZURE_CLIENT_SECRET = credentials('azure-client-secret')
        AZURE_TENANT_ID = credentials('azure-tenant-id')
        RESOURCE_GROUP = 'your-resource-group-name'
        FUNCTION_APP_NAME = 'your-function-app-name'
    }
*/
    stages {
        stage('Checkout') {
            steps {
                // Cloning the GitHub repository with credentials
                git(
                    branch: 'main',  // Change to the branch you want to use (e.g., 'main')
                    url: 'https://github.com/navkaurneet/AzureF-CICD3.git',
                    credentialsId: 'GitHub1'
                )
            }
        }
        stage('Build') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    sh 'pip install -r function/requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    sh 'pytest tests/test_function.py/'  
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying to Azure...'
                    sh """
                        az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID
                        zip -r function.zip .  // Package the application
                        az functionapp deployment source config-zip --resource-group $RESOURCE_GROUP --name $FUNCTION_APP_NAME --src function.zip
                    """
                }
            }
        }
    }
}
