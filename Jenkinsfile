pipeline {
  agent any
  stages {
    stage('on git commit run scan') {
      steps {
        git(url: 'https://github.com/lordsfantasy/python_cicd_test.git', branch: 'master', changelog: true)
        sh '''curl --location --request POST \'http://demo.strobes.co:8006/v1/sast_scan/bandit/config/202/start/32d10e4c-9f49-484d-8db3-03c94873ab15/\' \\
--header \'Authorization: token 9d1d5deed3703dccfdcdaaabbc0b8f0342be0e3f\''''
      }
    }

  }
}