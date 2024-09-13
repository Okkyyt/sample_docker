### Dcokerfile にコンテナ化するためのコマンドを書く

```
FROM
RUN
COPY
CMD
```

### Docker イメージのビルド

```
docker build -t <イメージ名> .
```

### コンテナの起動

```
docker run -p 8000:8000 <イメージ名>
```

### 起動しているコンテナの確認

```
docker ps
```

### 起動しているコンテナの停止

```
docker stop <コンテナID>
```
