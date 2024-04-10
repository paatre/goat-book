docker build -t superlists . && docker run \
  -p 8888:8888 \
  --mount type=bind,source=./src/db.sqlite3,target=/src/db.sqlite3 \
  -it superlists
