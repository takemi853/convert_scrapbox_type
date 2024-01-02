# FROM python:3.11
# RUN pip install fastapi uvicorn spacy
# RUN python -m spacy download ja_core_news_sm
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# # ビルド用ステージ
# FROM python:3.11-alpine as builder

# # ビルド依存関係のインストール
# RUN apk add --no-cache build-base libffi-dev rust cargo

# # Pythonパッケージのインストール
# RUN pip install --no-cache-dir --user fastapi uvicorn spacy

# # spaCyの日本語モデルのダウンロード
# RUN python -m spacy download ja_core_news_sm

# # 実行用ステージ
# FROM python:3.11-alpine

# # ビルドステージから必要なファイルのコピー
# COPY --from=builder /root/.local /root/.local
# ENV PATH=/root/.local/bin:$PATH

# # アプリケーションコードのコピー
# COPY . .

# # アプリケーションの起動コマンド
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


# ビルド用ステージ
FROM python:3.11-alpine as builder

# 依存関係のインストール
RUN apk add --no-cache build-base libffi-dev rust cargo

# Pythonパッケージのホイールの作成
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir=/root/wheels -r requirements.txt
# spaCyの日本語モデルのダウンロード
RUN python -m spacy download ja_core_news_sm

# 実行用ステージ
FROM python:3.11-alpine
# ビルドステージからホイールのコピー
COPY --from=builder /root/wheels /root/wheels
# パッケージのインストール
RUN pip install --no-cache /root/wheels/* \
    && rm -rf /root/wheels

# 環境変数の設定
ENV PATH=/root/.local/bin:$PATH

# アプリケーションコードのコピー
COPY . .

# アプリケーションの起動コマンド
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

