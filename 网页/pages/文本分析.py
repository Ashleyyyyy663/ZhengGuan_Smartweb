import streamlit as st
import streamlit.components.v1 as components
import os


st.title("文本分析")
st.markdown(
    """
    <style>
    .css-hxt7ib { 
        display: none;
    }
    .block-container{
        padding-bottom:3rem;
        padding-right:3rem;
    }
    </style>
    
    """,
    unsafe_allow_html=True
)

base_path = os.path.join(os.path.dirname(__file__), "html")

with open(os.path.join(base_path, "词语相关图.html"), "r", encoding="utf-8") as file1:
    content1 = file1.read()
components.html(
    content1,
    height=800,  # 设置足够高度以避免内容裁剪
    scrolling=True,  # 启用滚动支持
    width=900
)  

col1, col2 = st.columns([2,1])

with open(os.path.join(base_path, "词云图.html"), "r", encoding="utf-8") as file2:
    content2 = file2.read()
with col1:
    components.html(content2, height=800,width=600)


with open(os.path.join(base_path, "论文年份.html"), "r", encoding="utf-8") as file3:
    content3 = file3.read()
with col2:
    components.html(content3, height=800,width=500)
