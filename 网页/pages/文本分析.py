import streamlit as st

# 设置页面标题和布局
st.set_page_config(page_title="文本分析", layout="wide")

st.title("文本分析")
st.write("这是主页内容")

# 嵌入自定义的JavaScript代码
html_code = """
<script src="https://agi-dev-platform-web.bj.bcebos.com/ai_apaas/embed/output/embedFullSDK.js?responseExpires=0"></script>
<script>
    window.onload = function() {
        setTimeout(function() {
            new EmbedLiteSDK({appId: '3e32fc42-53b6-495d-a739-38b13c50ca6a', code: 'embed3dx7ftgTSl8cQNPH6DsF'});
        }, 1000);  // 延迟1秒
    }
</script>
"""

# 使用st.components.v1.html来嵌入HTML和JS
st.components.v1.html(html_code, height=300)
