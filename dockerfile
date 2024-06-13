FROM nvcr.io/nvidia/

LABEL maintainer="miras_zakaryanov"

ARG TZ
ARG USER
ARG UID
# when running docker run add arg --env-file .env

RUN groupadd -g ${UID} ${USER} && useradd -l -r -m -s /bin/bash -u ${UID} ${USER} -g ${USER}

#Install your required software
RUN apt update -y && \
    apt -y install ca-certificates tzdata software-properties-common cmake

USER ${USER}

WORKDIR /home/user_name/
COPY . .

RUN python3 -m venv venv && source venv/bin/activate

RUN python3 -m pip install --upgrade pip 
RUN pip3 install -U -r requirements.txt