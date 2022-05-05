# NotePad Deployment with Docker CLI on Docker Engine

**Step 1**  Build gowebapp Docker image locally

```
#TODO  Build image `<your-github-user>/gowebapp:v1
```

**Step 2** Build gowebapp-mysql Docker image locally

```
#TODO  Build image  <your-github-user>/gowebapp-mysql:v1
```

**Step 3**  Launch `backend` container

```
#TODO Launch `backend` container in background
#TODO Use this settings: `--name gowebapp-mysql` `--hostname gowebapp-mysql` 
#TODO Include following Env Variable in the command: `MYSQL_ROOT_PASSWORD=rootpasswd`
```


**Step 4**  Launch `frontend` container

```
#TODO Launch `frontend` container in background
#TODO Use this settings: `--name gowebapp` `--hostname gowebapp` 
#TODO Map the container port 80  - to port 8080 on the host machine
```

**Step 5** Inspect the MySQL database

Let's connect to the backend MySQL database container and run some queries to
ensure that application persistence is working properly:

```
#TODO docker xxx
```

**Step 6** Cleanup running applications 
```
### TODO docker xxx
```
