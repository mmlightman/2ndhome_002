# pages/About.py
import streamlit as st

def app():
    # ページのレイアウトを設定
    st.set_page_config(layout="wide")
    
    # ヘッダータイトルの表示
    st.title('Detail')
    
    # トップの写真とテキスト
    st.image("C:/Users/0073001757/Desktop/VS CODE/20230913_スクレイピング演習/01_SUUMO_Scrayping_try/image_buy/image_page1_item2_0.jpeg", use_column_width=True)
    st.write("# YOUR PERFECT HEALING")

    # グリッドのレイアウト部分
    st.write("## SMART OFFERS")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("path_to_image1.jpg", use_column_width=True)
    with col2:
        st.image("path_to_image2.jpg", use_column_width=True)
    with col3:
        st.image("path_to_image3.jpg", use_column_width=True)
    with col4:
        st.image("path_to_image4.jpg", use_column_width=True)

    st.image("path_to_middle_image.jpg", use_column_width=True)
    st.write("# Healthy Entertainment")
