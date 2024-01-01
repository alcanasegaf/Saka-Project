######## Kynan #######

FROM python:3.10

COPY installer.sh .

RUN bash installer.sh

# changing workdir
WORKDIR "/root/alcanasegaf"

# start the bot.
CMD ["python3", "-m", "Saka"]
