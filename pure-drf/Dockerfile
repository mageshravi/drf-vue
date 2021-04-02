FROM python:3.9.2-slim-buster
ENV PYTHONUNBUFFERED 1

ARG USERNAME=webinative
# replace with your actual UID and GID if not the default 1000
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

# create user
RUN groupadd --gid $USER_GID ${USERNAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} \
    && mkdir -p /home/${USERNAME}/.vscode-server \
    && chown ${USER_UID}:${USER_GID} /home/${USERNAME}/.vscode-server \
    && mkdir -p /home/${USERNAME}/code \
    && chown ${USER_UID}:${USER_GID} /home/${USERNAME}/code \
    # [optional] add sudo support. omit if you don't need to install software after connecting.
    && apt-get update && apt-get install -y sudo \
    && echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME}

# git and psycopg2 dependencies
# RUN apt-get install -y git gcc libpq-dev

USER ${USERNAME}
WORKDIR /home/${USERNAME}/code
COPY pip-requirements /home/${USERNAME}/code/
RUN sudo pip install -r pip-requirements
# RUN sudo apt-get remove -y gcc libpq-dev

# not switching back to root
