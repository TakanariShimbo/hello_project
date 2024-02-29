
# 環境構築の手順

```
# 仮想環境作成
conda create -n python310_hello python=3.10 -y

# 仮想環境のアクティベート
conda activate python310_hello

# ライブラリのインストール
pip install -r requirements.txt
```

# 初期設定
.env_sample を .env として複製し、SOMETHING_KEYを適切にセットしてください。

# 実行方法
```
streamlit run hello.py
```