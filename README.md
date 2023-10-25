# 2ndhome_002
最終発表用

load_model.py: CLIPモデルをロードするための関数を提供
create_dataset.py: 指定されたディレクトリの画像を使用してデータセットを作成。load_model.pyからCLIPモデル読み込み。
index_operations.py: 作成されたデータセットの特徴ベクトルを使用してFaissインデックスを作成および読み込む
search.py: Faissインデックスを利用してクエリに基づく画像検索を行う関数を提供
main.py: 上記の全てのモジュールを連携させて、ユーザーのクエリに応じて画像検索を実行するメインのスクリプト（python）
app.py: streamlitの実行スクリプト
