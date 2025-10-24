# Using latest python image
FROM python:latest

# Setting time zone
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install apt packages(non-interractive)
RUN apt -y update \
	&& apt -y upgrade \
	&& apt install -y --no-install-recommends curl openjdk-21-jdk-headless build-essential git vim tig \
	&& mkdir -p /opt/antlr /work \
	&& apt clean \
	&& rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd --create-home --shell /bin/bash devuser \
	&& chown -R devuser:devuser /work /opt/antlr

USER devuser
ENV HOME=/home/devuser
WORKDIR /work

# Manage pip packages
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download ANTLR4 jar
ENV ANTLR_VERSION=4.13.2
ENV ANTLR_JAR=/opt/antlr/antlr-${ANTLR_VERSION}-complete.jar
RUN mkdir -p "$(dirname ${ANTLR_JAR})" \
	&& echo "Downloading ANTLR ${ANTLR_VERSION} ..." \
	&& curl -fsSL -o "${ANTLR_JAR}" "https://www.antlr.org/download/antlr-${ANTLR_VERSION}-complete.jar" \
	&& echo 'export CLASSPATH=".:/opt/antlr/antlr-${ANTLR_VERSION}-complete.jar:$CLASSPATH"' >> /home/devuser/.bashrc \
	&& echo 'export CLASSPATH=".:/opt/antlr/antlr-${ANTLR_VERSION}-complete.jar:$CLASSPATH"' >> /home/devuser/.profile

# Set as CLI command
ENV ANTLR_CMD=/home/devuser/bin/antlr4
ENV PATH="/home/devuser/bin:${PATH}"
RUN mkdir -p /home/devuser/bin \
	&& echo '#!/bin/bash' > ${ANTLR_CMD} \
	&& echo "java -jar ${ANTLR_JAR} \"\$@\"" >> ${ANTLR_CMD} \
	&& chmod +x ${ANTLR_CMD}

# Default shell
CMD ["bash"]
