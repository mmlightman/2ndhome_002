# main.py

# 必要なモジュールや関数をインポート
import create_dataset
import load_model
import index_operations
import search

if __name__ == "__main__":
    # 画像ファイルの格納ディレクトリを指定
    directory = "C:/Users/0073001757/Desktop/VS CODE/20230913_スクレイピング演習/01_SUUMO_Scrayping_try/image_buy"

    # モデルのロード
    models = load_model.load_clip_model()

    # 画像データセットの作成
    dataset = create_dataset.create_dataset_from_directory(directory, models)
    image_list = dataset['path_list']  # 画像のパスリスト
    vectors = dataset['vectors']  # 画像の特徴ベクトル

    # Faissインデックスの作成
    index_path = "faiss_index.index"
    index_operations.create_faiss_index(vectors, index_path)

    # Faissインデックスの読み込み
    index = index_operations.load_index_from_file(index_path)

    # クエリの入力
    query_text = input("Please enter a keyword or phrase to search for relevant images: ")

    # 画像検索の実行
    top_k = 5  # 上位5件の画像を取得
    search_results = search.perform_search(query_text, models, index, image_list, top_k)  # indexを渡すように変更
    
    # 検索結果の表示
    print("Top matches:")
    for idx, score in search_results:
        print(f"Image Path: {image_list[idx]}")
        #スコアも付ける場合        print(f"Image Path: {image_list[idx]}, Similarity Score: {score}")