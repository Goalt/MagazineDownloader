# Bot for checking new releases of magazine "Хакер".
## Overview
Bot purpose is to get html page using BeutifulSoup, parse it and get url of last release. If release is differ from the one in "tmp" file bot send message (with url of new release) using telepot.
## Usage
### Conda
```shell
conda env create -f environment.yml
conda activate magasize_downloader_env
python main.py
```
Or for repeatedly start
```shell
watch -n 60 /root/miniconda3/envs/magasize_downloader_env/bin/python main.py
```
### Docker
```shell
bash docker/docker_build.sh
bash docker/docker_run.sh
```