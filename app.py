import streamlit as st
import requests

colab_url = "https://1e82-35-230-163-92.ngrok-free.app/process"

st.title("対話アプリ")
st.text("会話内容を入れてください。")

# 会話内容入力フォーム
text_input = st.text_input('Input')

st.write(f"Debug: text_input = '{text_input}'")

if text_input.strip():
    data = {"text": text_input}
    try:
        response = requests.post(colab_url, json=data)
        print(response.status_code)
        print(data)
        if response.status_code == 200:
            result = response.json()
            st.write(f"モデル: {result['response']}")
        else:
            st.error("Colab サーバーでエラーが発生しました！")
    except requests.exceptions.RequestException as e:
        st.error(f"通信エラー: {e}")
else:
    st.warning("入力してください！")