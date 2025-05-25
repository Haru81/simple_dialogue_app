import streamlit as st
import requests

colab_url = "https://fea6-34-83-131-80.ngrok-free.app/process"

st.title("対話アプリ")
st.text("会話内容を入れてください。")

# 会話内容入力フォーム
text_input = st.text_input('Input')

if text_input.strip():
    data = {"text": text_input}
    try:
        response = requests.post(colab_url, json=data)
        print(f"status code: {response.status_code}\ndata: {data}")
        if response.status_code == 200:
            result = response.json()
            st.write(f"モデル: {result['response']}")
        elif response.status_code == 404:
            st.error("Colabサーバーが起動していないか接続できません")
        else:
            st.error("Colab サーバーでエラーが発生しました！")
    except requests.exceptions.RequestException as e:
        st.error(f"通信エラー: {e}")
else:
    st.warning("入力してください！")