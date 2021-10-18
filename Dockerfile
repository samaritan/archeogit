FROM python:3.7-slim-bullseye

# Install Dependencies
RUN apt-get update && apt-get install -qq --no-install-recommends \
      git=1:2.30.* && \
    rm -rf /var/lib/apt/lists/*

# Setup Environment
WORKDIR /samaritan/archeogit

# Copy and Run archeogit
COPY LICENSE .
COPY VERSION .
COPY config.json .
COPY setup.py .
COPY archeogit archeogit/
RUN pip install --no-cache-dir --quiet --trusted-host pypi.python.org -e .

ENTRYPOINT ["archeogit"]
