# 01_utils.py

import os
from PIL import Image
from torchvision import transforms

# 共通の前処理関数を定義
def preprocess_image(image_path):
    # 画像の前処理の手順を定義する
    # 1. 画像を224x224にリサイズ
    # 2. 画像の中央を224x224でクロップ
    # 3. 画像をTensorに変換
    # 4. 画像の色情報を正規化
    preprocess = transforms.Compose([
        transforms.Resize(224),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize((0.48145466, 0.4578275, 0.40821073), (0.26862954, 0.26130258, 0.27577711)),
    ])
    
    # 画像をロードし、RGBに変換
    image = Image.open(image_path).convert('RGB')
    
    # 上で定義した前処理手順を適用
    return preprocess(image).unsqueeze(0)

# 指定ディレクトリ内の画像ファイルを取得する関数
def get_image_files_from_directory(directory):
    # サポートしている画像ファイルの拡張子を定義
    extensions = ['.jpg', '.jpeg', '.png']
    # 指定したディレクトリ内のファイルをチェックし、画像ファイルのみをリストに追加
    return [os.path.join(directory, f) for f in os.listdir(directory) if any(f.endswith(ext) for ext in extensions)]