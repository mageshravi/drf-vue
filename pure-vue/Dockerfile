FROM node:14.16.0-buster-slim

# nodejs image has a pre-defined user "node" with uid and gid set to 1000
ARG USERNAME=node

USER ${USERNAME}
RUN mkdir -p /home/${USERNAME}/.vscode-server \
    && mkdir -p /home/${USERNAME}/code

WORKDIR /home/${USERNAME}/code
COPY package*.json /home/${USERNAME}/code/
RUN npm install
COPY . /home/${USERNAME}/code/
