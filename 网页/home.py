import streamlit as st
import importlib

# 设置页面标题和布局
st.set_page_config(page_title="智慧政管平台",layout="wide")

st.markdown(f"<h1 style='color: rgb(86,110,230);'>智慧政管平台</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    /* 隐藏侧边栏拖动手柄 */
    .css-hxt7ib {  /* 这个类名可能会更新 */
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)