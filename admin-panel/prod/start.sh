#!/bin/sh

for i in $(env | grep REPLACE_)
do
  key=$(echo "$i" | cut -d '=' -f 1)
  value=$(echo "$i" | cut -d '=' -f 2-)
  echo "$key=$value"

  # Заменяем ТОЛЬКО в файлах, содержащих "env" в имени
  find /usr/share/nginx/html -type f -name '*env*.js' \
    -exec sed -i "s|${key}|${value}|g" '{}' +

  # Заменяем в HTML-файлах
  find /usr/share/nginx/html -type f -name '*.html' \
    -exec sed -i "s|${key}|${value}|g" '{}' +
done

nginx -g 'daemon off;'