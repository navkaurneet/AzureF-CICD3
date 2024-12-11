pipeline {
    agent any
/*    environment {
        AZURE_CLIENT_ID = credentials('azure-client-id')
        AZURE_CLIENT_SECRET = credentials('azure-client-secret')
        AZURE_TENANT_ID = credentials('4ddd393a-e98a-4404-841f-c4becdd925a5')
        RESOURCE_GROUP = 'nav_cicd'
        FUNCTION_APP_NAME = 'nav-python-function-app'
    }
*/
    stages {
        stage('Checkout') {
            steps {
                // Cloning the GitHub repository with credentials
                git(
                    branch: 'main',
                    url: 'https://github.com/navkaurneet/AzureF-CICD3.git',
                    credentialsId: 'GitHub1'
                )
            }
        }
        stage('Build') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    // Navigate to the 'function' directory and install dependencies
                    bat 'pip install -r function/requirements.txt' 
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    // Run tests from the 'tests' directory
                    bat 'python -m unittest discover -s tests'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying to Azure...'
                    // Azure CLI command to deploy the function app
                    bat """
                        az login --service-principal -u %AZURE_CLIENT_ID% -p %AZURE_CLIENT_SECRET% --tenant %AZURE_TENANT_ID%
                        zip -r function.zip function/  // Zip the function app folder
                        az functionapp deployment source config-zip --resource-group %RESOURCE_GROUP% --name %FUNCTION_APP_NAME% --src function.zip
                    """
                }
            }
        }
    }
}
