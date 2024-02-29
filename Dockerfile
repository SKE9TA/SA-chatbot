FROM ghcr.io/chroma-core/chroma:latest
EXPOSE  8010
CMD ["chroma", "--host", "0.0.0.0", "--port", "8010"]
