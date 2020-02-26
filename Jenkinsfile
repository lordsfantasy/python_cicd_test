pipeline {
  agent any
  stages {
    stage('on git commit run scan') {
      steps {
        git(url: 'https://github.com/lordsfantasy/python_cicd_test.git', branch: 'master', changelog: true)
        sh '''task_id=$(curl --location --request POST \'http://demo.strobes.co:8006/v1/sast_scan/bandit/config/193/start/4ada15c3-d49c-44bc-96e5-ba3ba4d0580f/\' \\
--header \'Authorization: token 3bb0d1f4b975eaf6c9184e82639eb5747105fe24\' \\
--header \'Content-Type: application/json\' \\
--data-raw \'{
    "branch": "master"
}\' | jq -r \'.data.data.task_id\')  

echo \'$task_id\'
sleep 15s

'''
      }
    }

  }
}