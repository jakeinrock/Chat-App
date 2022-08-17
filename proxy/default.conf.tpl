upstream daphne_server {
    server daphne:9000;
}


server {
    listen ${LISTEN_PORT};
    server_name localhost;
    client_max_body_size 10M;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass          ${APP_HOST}:${APP_PORT};
        include             /etc/nginx/uwsgi_params;

    }

    location /ws/ {
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-for $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        proxy_pass http://daphne_server;
    }
}