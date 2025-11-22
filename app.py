import streamlit as st

st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
        text-align: center;
        color: #FF4B4B;
        font-weight: bold;
        margin-top: 20%;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="big-font">クエスト成功！<br>レベル2クリア！</p>', unsafe_allow_html=True)
st.balloons()
