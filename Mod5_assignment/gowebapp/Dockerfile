#TODO --- Define this image to inherit from the "golang" base image. Use version `1.15.11` or lower for `golang`
#https://hub.docker.com/_/golang/
#https://docs.docker.com/engine/reference/builder/#from


#TODO Set a label corresponding to the MAINTAINER field you could use, so that it wil be visible from docker inspect with the other labels.
#MAINTAINER should be you student e-mail.

#TODO --- Define a version label for this image
#https://docs.docker.com/engine/reference/builder/#label

EXPOSE 80

ENV GOPATH=/go

#TODO --- Copy source code in the local /code directory into $GOPATH/src/gowebapp
#https://docs.docker.com/engine/reference/builder/#copy

WORKDIR $GOPATH/src/gowebapp/

RUN go get && go install

#TODO --- Define an entrypoint for this image which executes the compiled application in $GOPATH/bin/gowebapp when the container starts
#https://docs.docker.com/engine/reference/builder/#entrypoint