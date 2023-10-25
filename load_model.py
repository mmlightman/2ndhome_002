# 02_load_model.py

import torch
import clip

# CLIPモデルをロードする関数を定義
def load_clip_model():
    # GPUが利用可能な場合は"cuda"を、それ以外の場合は"cpu"を使用する
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # CLIPモデルと、使用しないテキストトークナイザをロード
    model, _ = clip.load("ViT-B/32", device=device)
    return model