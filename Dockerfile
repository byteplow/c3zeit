FROM alpine:latest

RUN apk add pjsua flite python3

ENV TZ=UTC-1

RUN echo "* * * * * date '+It is %I:%M %p.' | flite -o /output.wav" > /etc/crontabs/root

RUN flite -t "1 2 3 4 5 6 7 8" -o /output.wav

CMD crond && pjsua --null-audio --id=sip:$NUM@voip.eventphone.de --registrar=sip:voip.eventphone.de --realm=voip.eventphone.de --username=$NUM --password=$PW --snd-auto-close=1 --jb-max-size=1 --auto-play --play-file=/output.wav --auto-answer=200
