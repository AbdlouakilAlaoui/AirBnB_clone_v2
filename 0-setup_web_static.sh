#!/usr/bin/env bash

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

echo "<html>
<head>
</head>
<body>
Holberton School
</body>
</html>" 
| sudo tee /data/web_static/releases/test/index.html

if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
nginx_config="/etc/nginx/sites-available/default"
sudo sed -i '/^server {/a \ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $nginx_config
sudo systemctl restart nginx
