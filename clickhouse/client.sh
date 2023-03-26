#!/usr/bin/env sh

docker compose exec client clickhouse-client \
                --host server \
                --user metin \
                --password "metin123.$"
