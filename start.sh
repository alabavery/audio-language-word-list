docker run \
    --name word-list \
    -v $1:"/target_directory_mount" \
    -e LANGUAGE=$2 \
    alaverydev/audio-language/word-list