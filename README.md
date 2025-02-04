# huntwords

Hunt for words in a grid of letters

![Hunt Words](ui/etc/huntwords.png)

## Usage

Run `docker compose up` or `lets up`. Upon startup the ui component will display the ports exposed.

```
ui_1               | -- ------------------------------------------------------------
ui_1               | -- SUMMARY
ui_1               | -- ------------------------------------------------------------
ui_1               | --
ui_1               | SCRIPT: /docker-entrypoint.d/99-metrics.sh
ui_1               | nginx version: nginx/1.25.3
ui_1               | NGINX:
ui_1               | ui: http://localhost:8090
ui_1               | redis-commander: http://localhost:8099
```

Visit the following urls as mentioned in the output above.

| URL                                    | What            |
| -------------------------------------- | --------------- |
| [http://localhost:8090/](http://localhost:8090/) | Hunt Words UI   |
| [http://localhost:8099/](http://localhost:8099/) | Redis Commander |

Click on one of the links of defined puzzles on the left and then click on a letter in the grid to *find* one of the words from the list on the right.

If nothing happens when you click on a letter, that is a sign that letter is used by more than one words (free hint).

Clicking on a word in the list will cause that word to be highlighted in the grid. But, only ask for a hint if you are really stuck. You only get 5 hints per game!

## Running

`docker compose up` or `lets up`

In another shell:
`./etc/refresh_puzzleboards.sh` or `lets refresh`

> refresh_puzzleboards.sh is designed to be able to be scheduled via cron. This may be needed in case of regular power failures. Ask me how I know ...

When done, hit CTRL-C and then `lets down`.

## Raspberry Pi
Huntwords is deployed onto a Raspberry Pi 4B using `docker compose`.

Also, in times past, `redis-commander` was not readily available as a published docker image and would need to be created from source.

> The image for redis-commander on ghcr.io now supports linux/amd64, linux/arm/v7, and linux/arm64.

It is no longer needed to be created from source.

## Dev Container
I have begun to make use of devcontainers as outlined in [klmcwhirter/oci-shared-images](https://github.com/klmcwhirter/oci-shared-images).

This project is a little different than the other projects with which I started: Huntwords is deployed onto a Raspberry Pi 4B using `docker compose`.

So, the devcontainer is not intended to replace docker compose but instead to enable a container-first developer experience (DX).
