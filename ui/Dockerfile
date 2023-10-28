FROM node:20-alpine as build

WORKDIR /app
COPY . /app

RUN npm install && npm run build


FROM nginx:mainline-alpine
RUN apk upgrade --no-cache && \
rm -fr /etc/nginx/conf.d

COPY --from=build /app/dist /usr/share/nginx/html

COPY ./etc/nginx /etc/nginx
