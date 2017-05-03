node {
    def app = 'bench-6efd6'
    def timestamp = sh(script: 'date +%s', returnStdout: true).trim()
    checkout scm
    stage('Launch in k8s') {
        sh("kubectl create namespace tsung")
        sh("kubectl create -f k8s/gevent-deployment.yaml --namespace tsung")
        sh("kubectl create -f k8s/target-svc.yaml --namespace tsung")
        sh("kubectl create -f k8s/tsung-config.yaml --namespace tsung")
        sh("kubectl create -f k8s/tsung-master-svc.yaml --namespace tsung")
        sh("kubectl create -f k8s/tsung-slave-svc.yaml --namespace tsung")
        sh("kubectl create -f k8s/tsung-slave.yaml --namespace tsung")
        sh("kubectl create -f k8s/tsung-master.yaml --namespace tsung")
    }
    stage('Waiting for test') {
        sleep(90)
        sh("curl http://tsung-master-0.tsung-master.tsung.svc.cluster.local:8091/tsung.log > gevent.json")
        sh("kubectl delete -f k8s/gevent-deployment.yaml --namespace tsung")
        sh("kubectl create -f k8s/meinheld-deployment.yaml --namespace tsung")
        sh("kubectl delete -f k8s/tsung-master.yaml --namespace tsung")
        sh("kubectl create -f k8s/tsung-master.yaml --namespace tsung")
        sleep(90)
        sh("curl http://tsung-master-0.tsung-master.tsung.svc.cluster.local:8091/tsung.log > meinheld.json")
    }
    stage('Cleanup') {
        sh("kubectl delete -f k8s/tsung-master.yaml --namespace tsung")
        sh("kubectl delete -f k8s/tsung-slave.yaml --namespace tsung")
        sh("kubectl delete -f k8s/tsung-slave-svc.yaml --namespace tsung")
        sh("kubectl delete -f k8s/tsung-master-svc.yaml --namespace tsung")
        sh("kubectl delete -f k8s/tsung-config.yaml --namespace tsung")
        sh("kubectl delete -f k8s/target-svc.yaml --namespace tsung")
        sh("kubectl delete namespace tsung")
    }
    stage('Reporting') {
        sh("curl -X PUT -d @gevent.json https://${app}.firebaseio.com/stats/wsgi-server/${timestamp}/cases/gevent.json")
        sh("curl -X PUT -d @meinheld.json https://${app}.firebaseio.com/stats/wsgi-server/${timestamp}/cases/meinheld.json")
        sh("curl -X PUT -d 'true' https://${app}.firebaseio.com/tests/wsgi-server/${timestamp}/cases/gevent.json")
        sh("curl -X PUT -d 'true' https://${app}.firebaseio.com/tests/wsgi-server/${timestamp}/cases/meinheld.json")
        sh("curl -X PUT -d 'true' https://${app}.firebaseio.com/cases/wsgi-server/gevent/${timestamp}.json")
        sh("curl -X PUT -d 'true' https://${app}.firebaseio.com/suits/wsgi-server/tests/${timestamp}.json")
        sh("curl -X PUT -d '${timestamp}' https://${app}.firebaseio.com/suits/wsgi-server/latest.json")
    }
}
