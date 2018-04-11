FROM ubuntu:17.10
WORKDIR /
ADD ./dist/* /app/
RUN chmod +x /app/srvapp
EXPOSE 8888
ENTRYPOINT ./app/srvapp