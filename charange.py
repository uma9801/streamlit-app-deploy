# 仮想環境の作成コマンド python -m venv env
# 仮想環境の起動コマンド Windows: env\Scripts\activate.bat
# インストール済みパッケージの確認コマンド pip list
# アプリの起動コマンド streamlit run {ファイル名}py
# streamlitのインストールコマンド pip install streamlit
# 仮想環境の停止コマンド Ctrl + C
# 以下、GiHubリポジトリへのアップロード手順
# PC仮想環境内にインストールされているパッケージ情報をrequirements.txtに出力
# コマンド: pip freeze > requirements.txt
# GitHubリポジトリにソースコードをアップロードするための手順
# 1.git add .
# 2.git commit -m "first commit."
# 3.git push -u origin main
# Streamlit Community Cloudへのデプロイ手順
# Streamlit Community Cloudにログイン URL: https://share.streamlit.io/signup
# Create a new appをクリック
# Deploy a public app from GitHubを選択
import streamlit as st

st.title("初めての自作アプリ feat.VSCode")

st.write("これは私の最初のStreamlitアプリです。") 
st.write("#### 和暦⇔西暦変換アプリ")
st.write("動作モード1: 和暦から西暦への変換")
st.write("動作モード2: 西暦から和暦への変換")

selected_item = st.radio(
    "変換モードを選択してください",
    ("和暦から西暦", "西暦から和暦")
)
st.divider()

if selected_item == "和暦から西暦":
    st.write("和暦から西暦への変換を行います。")
    year = st.number_input("和暦の年を入力してください", min_value=1, max_value=9999, value=7)
    era = st.selectbox("和暦の元号を選択してください", ["令和", "平成", "昭和", "大正", "明治"])
    
    if era == "令和":
        western_year = year + 2018
    elif era == "平成":
        western_year = year + 1988
    elif era == "昭和":
        western_year = year + 1925
    elif era == "大正":
        western_year = year + 1911
    else:  # 明治
        western_year = year + 1867
    
    st.write(f"西暦 {western_year} 年です。")
elif selected_item == "西暦から和暦":
    st.write("西暦から和暦への変換を行います。")
    year = st.number_input("西暦の年を入力してください", min_value=1, max_value=9999, value=2025)
    
    if year >= 2019:
        era = "令和"
        era_year = year - 2018
    elif year >= 1989:
        era = "平成"
        era_year = year - 1988
    elif year >= 1926:
        era = "昭和"
        era_year = year - 1925
    elif year >= 1912:
        era = "大正"
        era_year = year - 1911
    else:
        era = "明治"
        era_year = year - 1867

    st.write(f"和暦 {era} {era_year} 年です。")