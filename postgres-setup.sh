docker run --name postgresql -itd --restart always \
    --publish 5432:5432 \
    --env 'DB_USER=admin' --env 'DB_PASS=admin' \
    --volume /srv/docker/postgresql:/var/lib/postgresql \
    sameersbn/postgresql:9.6-2