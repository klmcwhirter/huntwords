FROM node:20-alpine AS build

WORKDIR /app

COPY package-lock.json package.json /app/
RUN npm install

COPY favicon.ico index.html postcss.config.* tailwind.config.* tsconfig.* vite.config.* /app/
COPY src/ /app/src/
RUN npm run build


FROM nginx:mainline-alpine
RUN apk upgrade --no-cache
RUN rm -fr /etc/nginx/conf.d

WORKDIR /

COPY --from=build /app/dist usr/share/nginx/html

COPY ./etc/nginx /etc/nginx
COPY ./etc/docker-entrypoint.d/*.sh /docker-entrypoint.d
