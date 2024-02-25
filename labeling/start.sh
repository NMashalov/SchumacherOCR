docker run -it -p 8080:8080 \
    -v $(pwd)/data:/label-studio/data  \
    -v $(pwd)/files:/label-studio/files \
    --env LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true \
    --env LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=/label-studio/files \
    heartexlabs/label-studio:latest label-studio start