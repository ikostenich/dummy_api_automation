#!groovy


pipeline {
        docker {
            image 'dummy_api_automation'
            args '-e '
            }

        parameters {
            string(name: 'APP_ID', defaultValue: '627f60abb877aa976ca58d20', description: 'APP_ID api key used in requests headers')


        environment {
            APP_ID = "${params.APP_ID}"

        }

        stages {
                stage('Pre-build actions') {
                    steps {
                        sh """echo 'Starting Test Run'"""
                    }
                }
                stage('Run automated tests') {
                    steps {
                        sh '/bin/bash -c pytest'
                    }
                }
        }
}
