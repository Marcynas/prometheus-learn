docker run \
    -p 9090:9090 \
    -v /Users/martynastvaska/Documents/Prometheus/prometheus-learn/prometheus.yaml:/etc/prometheus/prometheus.yml \
    prom/prometheus
    