# csv2postgres
```Python based csv to postgres data migration```

## This project demonstrates how to setup a postgres server using docker and use alchemy DRM.

### Requirements
    [Docker](https://docs.docker.com/install/)
    [Python3]
    [Python3-pip]
    Python packages
        ```
        pip3 install sqlalchemy
        pip3 install psycopg2
        ```
    
## Setup
    1. Create a postgres server container by running the ```postgres-setup.sh```.
        ```
        You can customize postgres-setup.sh script.
        docker run --name postgresql -itd --restart always \
            --publish <port>:5432 \
            --env 'DB_USER=<user>' --env 'DB_PASS=<password>' \
            --volume /srv/docker/postgresql:/var/lib/postgresql \
            sameersbn/postgresql:9.6-2
        ```
    2. Create your tables by creating sqlalchemy drm based python models. Refer Contacts.py.
        ```Run contacts.py for this sample project.```
    3.Read the csv and upload the data to the database. Refer csv2postgres.py.
        ``` Run csv2postgres.py for this sample project```

