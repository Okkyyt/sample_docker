### DockerにPython環境環境
## pythonのdockerイメージをインストール
```
docker pull python
```

## 実行コマンド
```
docker run -v ${PWD}:/usr/src/app -w /usr/src/app/ python pyhon hello.py
```