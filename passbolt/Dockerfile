FROM passbolt/passbolt:latest

ENV APP_FULL_BASE_URL=https://pm.kizlarsoruyor.com
ENV DATASOURCES_DEFAULT_HOST="postgres"
ENV DATASOURCES_DEFAULT_DRIVER="Cake\Database\Driver\Postgres"
ENV DATASOURCES_DEFAULT_PORT="5432"
ENV DATASOURCES_DEFAULT_ENCODING="utf8"
ENV DATASOURCES_DEFAULT_USERNAME="admin"
ENV DATASOURCES_DEFAULT_PASSWORD="P4ssb0lt"
ENV DATASOURCES_DEFAULT_DATABASE="passboltdb"
ENV EMAIL_TRANSPORT_DEFAULT_HOST="smtp.domain.tld"
ENV EMAIL_TRANSPORT_DEFAULT_PORT="587"

RUN apt-get update
RUN apt-get install -y php-pgsql

EXPOSE 80 443
CMD [ "/docker-entrypoint.sh" ]

# docker-compose exec passbolt su -m -c "/usr/share/php/passbolt/bin/cake \
#                                 passbolt register_user \
#                                 -u your@email.com \
#                                 -f yourname \
#                                 -l surname \
#                                 -r admin" -s /bin/sh www-data

