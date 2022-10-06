# prometheus-learn
Learning prometheus

### Made using:
* ![Prometheus](https://img.shields.io/badge/Prometheus-E6522C.svg?style=for-the-badge&logo=Prometheus&logoColor=white)
* ![Grafana](https://img.shields.io/badge/Grafana-F46800.svg?style=for-the-badge&logo=Grafana&logoColor=white)
* ![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
* ![Docker](https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white)

### Summary:

By running ``` docker composer up ```
docker launches prometheus, grafana, pythonApp and all exporters in different containers.

Everything is connected to prometheus.

Custom alerts:
* Node exporter is down (CRITICAL)
* Python app is down (CRITICAL)
* Python app latency above 5 seconds (CRITICAL)
* Python app latency above 2 seconds (WARNING)

Alerts are sent to an email (turned off)

To test allerts you can manualy close one container or open python app (localhost:8000) few times. (latency is set to 5 seconds)

Custom rules:
* job:node_cpu_seconds:avg_idle
* job:node_cpu_seconds:avg_not_idle

Grafana has 3 dashboards imported to look at everything.

### EXPORTERS AND INTEGRATIONS:
* node-exporter
* blackbox-exporter
* pushgateway
* pythonApp
* alert manager



### Following:
* https://udemy.com/course/prometheus-course/
