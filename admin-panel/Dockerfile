FROM node:22-alpine AS build
WORKDIR /app

COPY package*.json ./
RUN --mount=type=cache,target=/root/.npm npm ci

COPY . .

RUN npm run build \
 && find dist -type f -name "*.map" -delete \
 && find dist -type f -name "*.js"  -print0 | xargs -0 sed -i 's|//# sourceMappingURL=.*$||' \
 && find dist -type f -name "*.css" -print0 | xargs -0 sed -i 's|/\*# sourceMappingURL=[^*]*\*/||g'

FROM nginx:stable-alpine
EXPOSE 3000

COPY --from=build /app/dist /usr/share/nginx/html
COPY ./prod/nginx.conf /etc/nginx/conf.d/default.conf

WORKDIR /app
COPY prod/start.sh .
RUN chmod +x start.sh
CMD ["sh", "./start.sh"]