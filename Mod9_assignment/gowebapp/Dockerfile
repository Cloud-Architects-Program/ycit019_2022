FROM golang:1.16.4

LABEL maintainer "student@mcgill.ca"
LABEL gowebapp "v1"

EXPOSE 80

ENV GO111MODULE=auto
ENV GOPATH=/go

#TODO --- add an environment variable declaration for a default DB_PASSWORD of "rootpasswd"
#https://docs.docker.com/engine/reference/builder/#env

COPY /code $GOPATH/src/gowebapp/
WORKDIR $GOPATH/src/gowebapp/
RUN go get && go install

#TODO --- add a volume declaration for the container configuration path we
# want to mount at runtime from the host file system:
# $GOPATH/src/gowebapp/config
#https://docs.docker.com/engine/reference/builder/#volume

ENTRYPOINT $GOPATH/bin/gowebapp
