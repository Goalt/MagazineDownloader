FROM continuumio/miniconda

RUN apt update
RUN apt install -y iputils-ping
RUN apt install -y etherwake
RUN apt install -y samba-common
RUN apt install -y sshpass
RUN apt install -y watch

COPY ./environment.yml environment.yml
RUN conda env create -f environment.yml

COPY ./main.py main.py
COPY ./secrets.py secrets.py
COPY ./htmlParser.py htmlParser.py
COPY ./tmp tmp

# CMD while true; do sleep 30; done;
CMD /opt/conda/envs/magazine_downloader_env/bin/python main.py
