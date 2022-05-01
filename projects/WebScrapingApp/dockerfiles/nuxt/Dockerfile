FROM node:16.13.2-alpine

# ワーキングディレクトリの指定
WORKDIR /app

RUN mkdir frontend
RUN mkdir frontend/scraper
RUN cd frontend/scraper

# パッケージをコピー(このファイルだけ別にして先にインストールしたほうが良い)
COPY ./frontend/scraper/package.json ./

#依存関係をインストール
RUN apk update && \
    apk upgrade && \
    # yarn installの記載場所を移動
    yarn install

# npm モジュールをインストール
RUN npm install --quiet

# その他のファイルをコピー
COPY ./frontend/scraper/* ./

# このコマンドをしないといけないとwarnが出たので
RUN npm rebuild

# 本当はいらないが開発環境でvue-cliを使っていたのでそこに含まれているパッケージを使っているようでwarnが出たので入れる
RUN npm install vue-cli -g

# ビルドします
#RUN npm run build

# PORT3000で動かす
EXPOSE 3000

# 起動コマンド
#CMD ["yarn", "dev"]