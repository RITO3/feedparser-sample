# feedparserサンプル

## 開発環境

Python 3.8.5
パッケージ管理 pipenv
開発環境 Visual Studio Code Remote Container
feedparser 5.2.1

## 環境構築メモ

pipenv初期化。

```shell
$ pipenv install
```

feedparserインストール。

```shell
$ pipenv install "feedparser~=5.2.1"
```

パッケージ一覧エクスポート。

```shell
$ pipenv shell
$ pip freeze > requirements.txt
```

## コマンド

```shell
$ pipenv install
```

スクリプト実行。
```shell
$ pipenv run start
```