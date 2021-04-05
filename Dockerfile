FROM andersenlabapps/ivar:1.3.1

RUN useradd -ms /bin/bash ivar

USER ivar

WORKDIR /home/ivar

COPY ./references /home/ivar/references

COPY ./ivarSupport /home/ivar/ivarSupport

COPY ./*.py /home/ivar

ENV PYTHONUNBUFFERED=1

CMD python3 /home/ivar/main.py