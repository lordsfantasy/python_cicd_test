pipeline {
  agent any
  stages {
    stage('on git commit run scan') {
      steps {
        git(url: 'https://github.com/lordsfantasy/python_cicd_test.git', branch: 'master', changelog: true)
        sh '''curl --location --request POST \'http://demo.strobes.co:8006/v1/sast_scan/bandit/config/205/start/f4b89c62-df5f-4717-bca4-2270b1c63a30/\' \\
--header \'Authorization: token 018023bbbdbf2c13a70061b067cf7234f8805165\''''
      }
    }

  }
}