# huntwords

Hunt for words in a grid

![Hunt Words](ui/etc/huntwords.png)

## Usage

Just docker-compose. Upon startup the ui component will display the ports exposed.

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

URL|What
---|----
[http://host:8090/](http://host:8090/)|Hunt Words UI
[http://host:8099/](http://host:8099/)|Redis Commander

## Running

`docker-compose up`

In another shell:
`./etc/refresh_puzzleboards.sh`

refresh_puzzleboards.sh is designed to be able to scheduled via cron. This may be needed in case of regular power failures. Ask me how I know ...

## Raspberry Pi

The image for redis-commander on Docker Hub only supports amd64.

To get support for linux-arm64 the image must be created from source.

Do the following:

1. clone https://github.com/joeferner/redis-commander.git
1. From the root dir of the repo: `docker buuld -t rediscommander/redis-commander .`

This will register the image locally. From there repeat the steps in the Running section above.

Voila!
