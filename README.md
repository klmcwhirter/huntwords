# huntwords

Hunt for words in a grid

![Hunt Words](ui/etc/huntwords.png)

## Usage

Run `docker compose up` or `pdm run up`. Upon startup the ui component will display the ports exposed.

```
ui_1               | -- ------------------------------------------------------------
ui_1               | -- SUMMARY
ui_1               | -- ------------------------------------------------------------
ui_1               | --
ui_1               | SCRIPT: /docker-entrypoint.d/99-metrics.sh
ui_1               | nginx version: nginx/1.25.3
ui_1               | NGINX:
ui_1               | EXPOSED_UI_PORT: 8090
ui_1               | EXPOSED_REDISCMD_PORT: 8099
```

Visit the following urls as mentioned in the output above.

| URL                                    | What            |
| -------------------------------------- | --------------- |
| [http://host:8090/](http://host:8090/) | Hunt Words UI   |
| [http://host:8099/](http://host:8099/) | Redis Commander |

## Running

`docker compose up` or `pdm run up`

In another shell:
`./etc/refresh_puzzleboards.sh` or `pdm run refresh`

> refresh_puzzleboards.sh is designed to be able to be scheduled via cron. This may be needed in case of regular power failures. Ask me how I know ...

## Raspberry Pi

The image for redis-commander on ghcr.io now supports linux/amd64, linux/arm/v7, and linux/arm64.

It is no longer needed to be created from source.
