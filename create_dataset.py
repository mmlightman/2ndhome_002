# 03_create_dataset.py

import torch
from utils import preprocess_image, get_image_files_from_directory

# 指定したディレクトリからデータセットを作成する関数を定義
def create_dataset_from_directory(directory, clip_model):
    # 指定したディレクトリ内の画像ファイルのリストを取得
    image_files = get_image_files_from_directory(directory)
    
    vectors = []
    image_path_list = []
    
    for image_path in image_files:
        # 画像を前処理
        image = preprocess_image(image_path)
        
        # CLIPモデルを使用して画像をベクトルに変換
        with torch.no_grad():
            vector = clip_model.encode_image(image)
            vectors.append(vector.squeeze(0))
            image_path_list.append(image_path)
            
    # 画像のパスとそのベクトルを返す
    return {
        'path_list': image_path_list,
        'vectors': vectors
    }