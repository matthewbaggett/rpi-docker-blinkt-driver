FROM gone/python-arm
COPY .docker/service /etc/service
RUN chmod +x /etc/service/*/run
RUN pip install blinkt