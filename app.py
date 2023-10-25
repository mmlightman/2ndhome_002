import streamlit as st
from pages import Home, About

def main():
    # ナビゲーションの選択
    selected = st.sidebar.radio("Navigate", ["Home", "About"])
    
    # それぞれのページを呼び出す
    if selected == "Home":
        # ここにホームページのコードや関数の呼び出しを書く
        pass
    elif selected == "About":
        About.app()

if __name__ == '__main__':
    main()