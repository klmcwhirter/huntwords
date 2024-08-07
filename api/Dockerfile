
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

# copy project files to prepare for setup
COPY  --chown=app:app pyproject.toml pdm.lock /app/

# create .venv, install project dependencies, clean up
RUN <<EOF
pdm create

pdm cache clear

pdm run python -m ensurepip --default-pip
pip cache purge
EOF

# copy files
COPY  --chown=app:app huntwordsapi/ /app/huntwordsapi/

# run tests
RUN pdm run pytest

EXPOSE 3000

CMD ["pdm", "run", "start"]
