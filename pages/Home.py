import time
import streamlit as st
from PIL import Image
import load_model
import create_dataset
import index_operations
import search
import clip

# モデルをロードする関数
def load_models():
    model = load_model.load_clip_model()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.device = device
    return model

# 画像のリストをロードする関数
def load_image_list(models):
    dataset = create_dataset.create_dataset_from_directory("C:/Users/0073001757/Desktop/VS CODE/20230913_スクレイピング演習/01_SUUMO_Scrayping_try/image_buy", models)
    # 画像のパスのバックスラッシュをフォワードスラッシュに変換
    corrected_path_list = [path.replace("\\", "/") for path in dataset['path_list']]
    return corrected_path_list

# Faissのインデックスをロードする関数
def load_index(path):
    return index_operations.load_index_from_file(path)

# テキストをベクトルに変換する関数
import torch

def text2vectors(text, model):
    # テキストをトークン化
    text_tokenized = clip.tokenize(text).to(model.device)
    
    # トークン化されたテキストをモデルに渡してエンコード
    with torch.no_grad():
        text_features = model.encode_text(text_tokenized)
        
    # 戻り値としてテキストの特徴を返す
    return text_features.cpu().numpy()

def main():
    # ページのレイアウトを設定
    st.set_page_config(layout="wide")

    # モデル、画像リスト、インデックスのロード
    with st.spinner('Loading...'):
        models = load_models()
        image_list = load_image_list(models)
        index = load_index('faiss_index.index')

    # ヘッダータイトルの表示
    st.title('2nd home Discovery Engine')

    # 5つのカラムを作成
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # 左のカラムに検索フォームを配置
    with col1:
        with st.form('text_form'):
            search_text = st.text_input('あなたの理想の家', '森の中のログハウス')
            button = st.form_submit_button('Search')

    # 検索ボタンが押されていない、または検索テキストが空の場合、処理を停止
    if not button or search_text == '':
        st.stop()

    # テキストをベクトルに変換
    t2v_start = time.time()
    query = text2vectors([search_text], models)

    # クエリを使ってインデックス検索を実行
    search_start = time.time()
    top_k = 5
    searched_indices = search.perform_search(search_text, models, index, image_list, top_k)
    search_end = time.time()

    # 検索結果からインデックスを取得し、画像のリストを取得
    searched_index = [idx for idx, score in searched_indices]
    results = [image_list[idx] for idx in searched_index]

    # 検索のタイミング情報を表示
    st.write('Text to Vector: {:.4f}[s]'.format(search_start - t2v_start))
    st.write('Search        : {:.4f}[s]'.format(search_end - search_start))

    # 検索結果の画像を5つのカラムに表示
    cols = [col2, col3, col4, col5, col1]
    for i, img_path in enumerate(results):
        with cols[i]:
            st.image(img_path, caption=img_path, use_column_width="always")

if __name__ == '__main__':
    main()