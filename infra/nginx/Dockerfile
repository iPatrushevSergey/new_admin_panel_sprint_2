FROM nginx:latest

COPY nginx.conf /etc/nginx/
COPY admin_panel.conf /etc/nginx/conf.d/
COPY index.html /var/html/

CMD ["nginx"]