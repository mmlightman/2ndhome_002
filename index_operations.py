# 04_index_operations.py

import faiss
import numpy as np

# Faissのインデックスを作成し、指定されたパスに保存する関数
def create_faiss_index(vectors, file_path):
    # ベクトルのリストをnumpy配列に変換
    vectors_np = np.vstack(vectors)
    
    # Faissインデックスを初期化
    index = faiss.IndexFlatL2(vectors_np.shape[1])
    
    # ベクトルをインデックスに追加
    index.add(vectors_np)

    # Faissインデックスを指定されたパスに保存
    faiss.write_index(index, file_path)
    
    return index

# ファイルからFaissのインデックスを読み込む関数
def load_index_from_file(file_path):
    return faiss.read_index(file_path)