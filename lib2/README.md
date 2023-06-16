# Папка второго задания по MLops 2023 spring

## Скрипт пайплайна
```
pipeline {
    agent any

    stages {
        stage('Installing libraries') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Data download') {
            steps {
                git credentialsId: 'github', url: 'https://github.com/Timelapse39/MLops_2023'
                dir ('data_default') {
                    sh 'curl -LJO https://raw.githubusercontent.com/Timelapse39/MLops_2023/main/static-files/ds_salaries.csv'
                }
            }
        }
        stage('Create data') {
            steps { 
                sh 'python3 data_creation.py'
            }
        }
        stage('Preprocessing') {
            steps {
                sh 'python3 model_preprocessing.py'
            }
        }
        stage('Preparation') {
            steps {
                sh 'python3 model_preparation.py'
            }
        }
        stage('Testing model') {
            steps {
                sh 'python3 model_testing.py'
            }
        }
    }
}
```
