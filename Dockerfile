FROM continuumio/miniconda:latest


RUN apt-get update && apt-get install --no-install-recommends --yes python3


COPY . /app

WORKDIR /app

RUN conda env update -f environment.yml && \
    rm -rf /tmp/* && conda clean --all --yes

RUN echo "source activate env" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH

ENTRYPOINT ["python3"]

CMD ["app.py"]