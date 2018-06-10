docker run \
--name mydb \
-p 5432:5432 \
-v /etc/postgresql:/etc/postgresql \
-v /var/log/postgresql:/var/log/postgresql \
-v /var/lib/postgresql:/var/lib/postgresql \
-e POSTGRES_PASSWORD=admin \
-d postgres