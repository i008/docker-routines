#### 1) Multiple flask apps behind nginx proxy 

Use 0.0.0.0 as host-ip in flask (better use a manager like gunicorn to run your apps)
Remember to edit Nginx redirects to match names in docker-compose

```bash
docker-compose up --build
curl http://localhost://app1/hello
Hello from app1
curl http://localhost://app2/hello
Hello from app2  
```

#### docker-shortcuts:
```bash
#stop all containers
docker stop $(docker ps -a -q)

#remove all containers
docker rm $(docker ps -a -q)

# Delete all containers
docker rm $(docker ps -a -q)
# Delete all images
docker rmi $(docker images -q)
```
