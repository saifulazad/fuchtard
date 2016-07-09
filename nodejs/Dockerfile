FROM node:6.3

MAINTAINER robox

ENV NODEJS_WORKDIR=/usr/web/nodejs

RUN mkdir -p $NODEJS_WORKDIR
WORKDIR $NODEJS_WORKDIR

ADD package.json /tmp/package.json
RUN cd /tmp && npm install
RUN cp -a /tmp/node_modules ./

ADD package.json ./
ADD webpack.config.js ./
ADD assets/ ./assets/

RUN mkdir -p ../webpack_bundles

RUN ls -la

RUN npm run build

ENTRYPOINT ["npm"]
CMD ["run", "build"]