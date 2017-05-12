node {
    def app = 'bench-6efd6'
    def cases = ['gevent', 'meinheld', 'bjoern', 'gunicorn-sync', 'gunicorn-gevent', 'gunicorn-meinheld', 'uwsgi', 'uwsgi-gevent']
    def timestamp = sh(script: 'date +%s', returnStdout: true).trim()
    checkout scm
    stage('Launch in k8s') {
        sh("kubectl create namespace tsung")
        sh("kubectl create -f k8s/target-svc.yaml --namespace tsung")
        sh("kubectl create -f k8s/tsung-config.yaml --namespace tsung")
        sh("kubectl create -f k8s/tsung-master-svc.yaml --namespace tsung")
        sh("kubectl create -f k8s/tsung-slave-svc.yaml --namespace tsung")
        sh("kubectl create -f k8s/tsung-slave.yaml --namespace tsung")
    }
    stage('Waiting for test') {
        for (int i = 0; i < cases.size(); i++) {
            runTest(cases.get(i))
        }
    }
    stage('Cleanup') {
        sh("kubectl delete -f k8s/tsung-slave.yaml --namespace tsung")
        sh("kubectl delete -f k8s/tsung-slave-svc.yaml --namespace tsung")
        sh("kubectl delete -f k8s/tsung-master-svc.yaml --namespace tsung")
        sh("kubectl delete -f k8s/tsung-config.yaml --namespace tsung")
        sh("kubectl delete -f k8s/target-svc.yaml --namespace tsung")
        sh("kubectl delete namespace tsung")
    }
    stage('Reporting') {
        for (int i = 0; i < cases.size(); i++) {
            reportTest(app, timestamp, cases.get(i))
        }
        sh("curl -X PUT -d 'true' https://${app}.firebaseio.com/suits/wsgi-server/tests/${timestamp}.json")
        sh("curl -X PUT -d '${timestamp}' https://${app}.firebaseio.com/suits/wsgi-server/latest.json")
    }
}

def runTest(current) {
    sh("kubectl create -f k8s/${current}-deployment.yaml --namespace tsung")
    sleep(60)
    sh("kubectl create -f k8s/tsung-master.yaml --namespace tsung")
    sleep(90)
    sh("curl http://tsung-master-0.tsung-master.tsung.svc.cluster.local:8091/tsung.log > ${current}.json")
    sh("kubectl delete -f k8s/${current}-deployment.yaml --namespace tsung")
    sh("kubectl delete -f k8s/tsung-master.yaml --namespace tsung")
}

def reportTest(app, timestamp, current) {
    sh("curl -X PUT -d @${current}.json https://${app}.firebaseio.com/stats/wsgi-server/${timestamp}/cases/${current}.json")
    sh("curl -X PUT -d 'true' https://${app}.firebaseio.com/tests/wsgi-server/${timestamp}/cases/${current}.json")
    sh("curl -X PUT -d 'true' https://${app}.firebaseio.com/cases/wsgi-server/${current}/${timestamp}.json")
}
