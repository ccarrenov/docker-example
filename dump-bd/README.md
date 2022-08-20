# EXECUTE COMMAND FOR DOCKER MYSQL 8.0

# CREATE CONTAINER
sudo docker-compose up -d

# STOP CONTAINER
sudo docker stop dump-bd-container

# START CONTAINER
sudo docker start dump-bd-container

# DELETE CONTAINER (FOR DELETE DOCKER, IT DOES STOPPED CONTAINER)
sudo docker rm dump-bd-container

# LOGS
sudo docker logs -f dump-bd-container
