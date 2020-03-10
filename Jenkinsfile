pipeline {
  agent any
  stages {
    stage('on git commit run scan') {
      steps {
        git(url: 'https://github.com/lordsfantasy/python_cicd_test.git', branch: 'master', changelog: true)
        sh '''curl --location --request POST \'http://demo.strobes.co:8006/v1/sast_scan/bandit/config/203/start/4e32f937-f72d-4b09-a71d-4636788f2748/\' \\
--header \'Authorization: token 8f8671be78e21c439854bc35ca32d8dcfb0ef21d\''''
      }
    }

  }
}