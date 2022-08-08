# EXECUTE COMMAND FOR DOCKER MYSQL 8.0

# CREATE CONTAINER
sudo docker-compose up -d

# STOP CONTAINER
sudo docker stop oracle_11gxe

# START CONTAINER
sudo docker start oracle_11gxe

# DELETE CONTAINER (FOR DELETE DOCKER, IT DOES STOPPED CONTAINER)
sudo docker rm oracle_11gxe
