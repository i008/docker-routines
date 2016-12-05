- Use 0.0.0.0 as host-ip in flask (better use a manager like gunicorn to run your apps)
- Remember to edit Nginx redirects to match names in docker-compose

```bash
curl http://localhost://app1/hello 
Hello from app1                                                                                                            curl curl http://localhost://app2/hello  
Hello from app2                                                                                                               
```
