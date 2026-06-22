ARG TOMCAT_DOCKER_VERSION


FROM docker AS builder
ARG TLS_KEYSTORE_FILE
ARG TLS_KEYSTORE_PASS
ARG ALIAS
ARG HTTPS_PORT
ARG DB_DRIVER=org.mariadb.jdbc.Driver
ARG DB_SCHEMA=core
ARG DB_USER
ARG DB_PASS
ARG MARIADB_URI
ARG MONGO_HOST
ARG MONGO_PORT
ARG MONGO_CONN_TIMEOUT
ARG MONGO_SOCK_TIMEOUT
ARG MONGO_SVR_TIMEOUT

USER root
WORKDIR /workdir

COPY target/owaspSecurityShepherd.war ROOT.war
COPY target/docker/tomcat/$TLS_KEYSTORE_FILE $TLS_KEYSTORE_FILE
COPY docker/tomcat/serverxml.patch serverxml.patch
COPY docker/tomcat/webxml.patch webxml.patch

RUN sh -c 'printf "databaseConnectionURL=%s/\nDriverType=%s\ndatabaseSchema=%s\ndatabaseUsername=%s\ndatabasePassword=%s\ndatabaseOptions=useUnicode=true&character_set_server=utf8mb4\n" "$MARIADB_URI" "$DB_DRIVER" "$DB_SCHEMA" "$DB_USER" "$DB_PASS" > database.properties'
RUN sh -c 'printf "connectionHost=%s\nconnectionPort=%s\ndatabaseName=shepherdGames\nconnectTimeout=%s\nsocketTimeout=%s\nserverSelectionTimeout=%s" "$MONGO_HOST" "$MONGO_PORT" "$MONGO_CONN_TIMEOUT" "$MONGO_SOCK_TIMEOUT" "$MONGO_SVR_TIMEOUT" > mongo.properties'
RUN sh -c 'sed -i "s|TLS_KEYSTORE_FILE|$TLS_KEYSTORE_FILE|g; s|TLS_KEYSTORE_PASS|$TLS_KEYSTORE_PASS|g; s|ALIAS|$ALIAS|g; s|HTTPS_PORT|$HTTPS_PORT|g" serverxml.patch'

FROM tomcat:${TOMCAT_DOCKER_VERSION}
COPY --from=builder /workdir/ROOT.war /usr/local/tomcat/webapps/
COPY --from=builder /workdir/$TLS_KEYSTORE_FILE /usr/local/tomcat/conf/
COPY --from=builder /workdir/serverxml.patch /usr/local/tomcat/conf/
COPY --from=builder /workdir/webxml.patch /usr/local/tomcat/conf/
COPY --from=builder /workdir/database.properties /usr/local/tomcat/conf/
COPY --from=builder /workdir/mongo.properties /usr/local/tomcat/conf/

ENV RUN_USER tomcat
RUN apt-get -qq update && apt-get install -y patch libargon2-1
RUN adduser --system --group ${RUN_USER} --home ${CATALINA_HOME}
RUN chown -R ${RUN_USER}:${RUN_GROUP} $CATALINA_HOME
USER ${RUN_USER}

RUN rm -rf /usr/local/tomcat/webapps/ROOT
RUN patch /usr/local/tomcat/conf/server.xml /usr/local/tomcat/conf/serverxml.patch
RUN patch /usr/local/tomcat/conf/web.xml /usr/local/tomcat/conf/webxml.patch

EXPOSE 8080 8443
CMD ["catalina.sh", "run"]
