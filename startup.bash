# variables
ENV_BUCKET=env-bucket-jan24

sudo apt update -y
sudo apt upgrade -y

# Docker install
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update -y

sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# boot up project
git clone https://github.com/PyaePhyoKanto/DummyDjangoReactML.git
cd DummyDjangoReactML
gsutil cp gs://$ENV_BUCKET/.env .env
gsutil cp gs://$ENV_BUCKET/react-env/.env my-react-app/.env
sudo docker compose up -d --build
sudo docker exec -it dummydjangoreactml-web-1 python manage.py migrate

# react build maybe useful later
sudo docker cp dummydjangoreactml-nginx-1:/usr/share/nginx/html react_build