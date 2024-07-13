
ARG PYTHON_BASE=3.12-alpine

FROM python:$PYTHON_BASE

# Add non root user
RUN addgroup -S app && adduser app -S -G app

USER app:app

WORKDIR /app

ENV PATH=$PATH:/home/app/.local/bin

# install PDM
RUN pip install -U pdm

# disable update check
ENV PDM_CHECK_UPDATE=false

# copy files
COPY  --chown=app:app huntwordsapi/ /app/huntwordsapi/
COPY  --chown=app:app pyproject.toml pdm.lock /app/

# install project dependencies, run tests, clean up
RUN <<EOF
pdm install --check --no-editable

pdm run pytest

pdm cache clear

pdm run python -m ensurepip --default-pip
pip cache purge
EOF

EXPOSE 3000

CMD ["pdm", "run", "start"]
