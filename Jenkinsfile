#!groovy


pipeline {
        agent any

        parameters {
            string(name: 'APP_ID', defaultValue: '627f60abb877aa976ca58d20', description: 'APP_ID api key used in requests headers')
            }

        environment {
            APP_ID = "${params.APP_ID}"

        }

        stages {
                stage('Build Docker image') {
                    steps {
                        sh """
                        docker build -t dummy_api_automation .
                        """
                    }
                }

                stage('Run automated tests') {
                    steps {
                        sh '''
                            docker run --env-file .env dummy_api_automation
                        '''
                    }
                }
            }
        }
