# Python WSGI Server Benchmark

We run [Tsung](http://tsung.erlang-projects.org/) in [Kubernetes](https://kubernetes.io/)
to load testing several popular Python WSGI servers to understand the performance of
Python servers under high load. [This repo](https://github.com/kubeup/tsung-in-kubernetes)
described the detailed testing environment.

All the tests are done through [Jenkins](https://jenkins.io/) job and you can find the
test results in [this spreadsheet](https://docs.google.com/spreadsheets/d/1_JkF5EEnj6Llq3tIoB2nMkjjFWzVthvxD7D-ExD-nhM/edit?usp=sharing).
If you wanted to add more target projects to the list or to improve the test cases,
feel free to send a PR. You'll find the updated test results after we run the Jenkins
job periodically.

## Target projects

Currently we test these Python WSGI servers:

- [gevent](http://www.gevent.org/)
- [Meinheld](http://meinheld.org/)
- [bjoern](https://github.com/jonashaag/bjoern)
- [Gunicorn](http://gunicorn.org/)
- [uWSGI](https://uwsgi-docs.readthedocs.io)

## Test cases

We run these test cases

- [Ping-Pong test](https://github.com/kubeup/python-wsgi-benchmark/blob/master/app/simple.py#L1)

## Test methods

For each test target, we run load testing for 90 seconds. For the first 60 seconds,
5 new virtual users got spawned every second. Each virtual user will connect to the
target server and fire http GET request for 10000 times.

Tsung will dump test stats every 10 seconds. We will gather all the dumped stats
for analysis and plotting.

## Test results

We found Bjoern has the highest QPS at around 10,000/s which is quite impressive.
You could find the detailed test results at [here](https://docs.google.com/spreadsheets/d/1_JkF5EEnj6Llq3tIoB2nMkjjFWzVthvxD7D-ExD-nhM/edit?usp=sharing).

<p align="center">
  <img src="https://raw.githubusercontent.com/kubeup/python-wsgi-benchmark/master/docs/request-mean.png"></image>
  <img src="https://raw.githubusercontent.com/kubeup/python-wsgi-benchmark/master/docs/request-value.png"></image>
</p>
