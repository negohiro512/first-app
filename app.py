import streamlit as st
import pandas as pd
import plotly.express as px

# 画面タイトル
st.title("データ分析ダッシュボード")

# CSVファイルのアップロード機能
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")

if uploaded_file is not None:
    try:
        # Pandasで読み込み
        df = pd.read_csv(uploaded_file)
        
        # データの中身（表）を表示
        st.subheader("データプレビュー")
        st.dataframe(df)
        
        # 数値データのカラムを抽出
        numeric_cols = df.select_dtypes(include=['float', 'int']).columns.tolist()
        
        if len(numeric_cols) >= 2:
            st.subheader("散布図 (Scatter Plot)")
            
            # ユーザーに軸を選択させる
            col1, col2 = st.columns(2)
            with col1:
                x_axis = st.selectbox("X軸を選択", numeric_cols, index=0)
            with col2:
                y_axis = st.selectbox("Y軸を選択", numeric_cols, index=1)
            
            # 散布図を描画
            fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
            st.plotly_chart(fig)
        elif len(numeric_cols) == 1:
             st.warning("散布図を描画するには、少なくとも2つの数値列が必要です。")
        else:
            st.warning("数値データが含まれていないため、散布図を描画できません。")
            
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
else:
    st.info("CSVファイルをアップロードすると、ここにデータとグラフが表示されます。")
