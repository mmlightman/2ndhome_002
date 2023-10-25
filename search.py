#05 search.py
from utils import preprocess_image
import torch
import faiss  
from clip import tokenize  # CLIPのトークナイザをインポート

# クエリ画像を使用してFaissインデックスで最も類似する画像を検索する関数
def search_similar_images(query_image_path, clip_model, index, image_path_list, top_k=5):
    # クエリ画像を前処理
    query_image = preprocess_image(query_image_path)
    
    # クエリ画像をベクトルに変換
    with torch.no_grad():
        query_vector = clip_model.encode_image(query_image)
    
    # ベクトルをnumpy配列に変換
    query_vector_np = query_vector.cpu().numpy()
    
    # インデックスを使用して最も類似する画像のIDと距離を取得
    distances, indices = index.search(query_vector_np, top_k)
    
    # 最も類似する画像のパスをリストとして返す
    return [image_path_list[i] for i in indices[0]]

# テキストクエリを使用してFaissインデックスで最も類似する画像を検索する関数
def perform_search(query_text, clip_model, index, image_path_list, top_k=5):
    
    # クエリテキストをトークナイザを使用してトークン化
    text_tokens = tokenize([query_text])  # トークナイズ
    
    # エンコード
    with torch.no_grad():
        query_vector = clip_model.encode_text(text_tokens)
    
    # ベクトルをnumpy配列に変換
    query_vector_np = query_vector.cpu().numpy()
    
    # インデックスを使用して最も類似する画像のIDと距離を取得
    distances, indices = index.search(query_vector_np, top_k)
    
    # インデックスと距離を返す
    return list(zip(indices[0], distances[0]))