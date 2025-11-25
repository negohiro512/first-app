import streamlit as st
import google.generativeai as genai

# ページ設定
st.set_page_config(page_title="業務プロセス分析AI", layout="wide")

# サイドバー：APIキー入力
st.sidebar.title("設定")
api_key = st.sidebar.text_input("Gemini APIキーを入力してください", type="password")

# メイン画面
st.title("業務プロセス分析AI")
st.markdown("内部監査のプロフェッショナルAIが、あなたの業務フローからリスクと統制を分析します。")

# 業務記述入力エリア
st.subheader("業務記述を入力してください")
business_process = st.text_area("業務フローの詳細をここに記述してください...", height=300)

# 分析開始ボタン
if st.button("分析開始", type="primary"):
    # バリデーション
    if not api_key:
        st.sidebar.error("サイドバーにAPIキーを入力してください")
        st.stop()
    
    if not business_process:
        st.warning("分析する業務フローを入力してください")
        st.stop()

    try:
        # Gemini API設定
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # プロンプト作成
        prompt = f"""
        あなたは内部監査のプロです。入力された業務フローを読み解き、想定される『リスク』と、それに対応する『コントロール（統制）』の案を、箇条書きで3つずつ挙げてください。

        【業務フロー】
        {business_process}
        """
        
        # AI生成実行
        with st.spinner("AIが業務フローを分析中..."):
            response = model.generate_content(prompt)
            
            # 結果表示
            st.success("分析が完了しました")
            st.markdown("### 分析結果")
            st.markdown(response.text)
            
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
        st.info("APIキーが正しいか、またはインターネット接続を確認してください。")
        

