# Operations

## Table of Contents
* [Prerequisites](#Prerequisites)
* [UFW](#UFW)
* [Nginx](#Nginx)
* [Systemd](#Systemd)
* [Release](#Release)

## Prerequisites

```shell
apt install certbot docker-compose git nginx python3-certbot-nginx ufw
cd /opt
git clone https://github.com/ursais/frepple-template frepple-template
```

## UFW

```shell
ufw allow ssh
ufw allow http
ufw allow https
ufw enable
```

## Nginx

* Create `/etc/nginx/sites-available/frepple.example.com` with:

```nginx
upstream frepple {
    server 127.0.0.1:8080;
}

server {
    listen 80;
    server_name frepple.example.com;

    location / {
        proxy_pass  http://frepple;
    }
}
```

* Enable, configure and start Nginx

```shell
cd /etc/nginx/sites-enabled
ln -s ../sites-available/frepple.example.com .
nginx -t
certbot
```

## Systemd

Create `/etc/systemd/system/frepple.service` with:

```unit file (systemd)
[Unit]
Description=FrePPLe container starter
After=docker.service network-online.target
Requires=docker.service network-online.target

[Service]
WorkingDirectory=/opt/frepple
Type=oneshot
RemainAfterExit=yes

ExecStartPre=-/usr/local/bin/docker-compose pull --quiet
ExecStart=/usr/local/bin/docker-compose -f docker-compose.yml up -d

ExecStop=/usr/local/bin/docker-compose -f docker-compose.yml down

ExecReload=/usr/local/bin/docker-compose pull --quiet
ExecReload=/usr/local/bin/docker-compose -f docker-compose.yml up -d

[Install]
WantedBy=multi-user.target
```

and run:
```shell
systemctl daemon-reload
systemctl enable frepple
service frepple start
```

## Release

Run:
```shell
cd /opt/frepple
git pull
service frepple restart
```
