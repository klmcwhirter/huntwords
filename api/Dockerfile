FROM python:3.12-alpine

RUN apk upgrade --no-cache

# Add non root user
RUN addgroup -S app && adduser app -S -G app

USER app:app

ENV PATH=$PATH:/home/app/.local/bin

COPY --chown=app:app ./huntwordsapi /huntwordsapi
COPY --chown=app:app ./requirements* ./

RUN python -m pip install --upgrade pip wheel && \
pip install -r requirements.txt

EXPOSE 3000

CMD ["python", "-m", "huntwordsapi"]

