const express = require('express');
const axios = require('axios');
const app = express();

// 启用跨域资源共享（CORS），让前端能够访问
const cors = require('cors');
app.use(cors());

app.use(express.static('public'));

// 获取 conversation_id 的函数
async function getConversationId() {
    const options = {
        'method': 'POST',
        'url': 'https://qianfan.baidubce.com/v2/app/conversation',
        'headers': {
            'Content-Type': 'application/json',
            'X-Appbuilder-Authorization': 'Bearer bce-v3/ALTAK-wHTCPq678QyUzev1iuaYu/fa292531edaa270804fea1a053bc9d1264fd5723'
        },
        data: JSON.stringify({
            "app_id": "3e32fc42-53b6-495d-a739-38b13c50ca6a"
        })
    };

    try {
        const response = await axios(options);
        console.log(response.data.conversation_id);
        return response.data.conversation_id;  // 返回 conversation_id
    } catch (error) {
        console.error('获取 conversation_id 失败:', error);
        throw error;
    }
}

app.get('/getAnswer', async (req, res) => {
    try {
        // 获取 conversation_id
        const conversationId = await getConversationId();

        const options = {
            'method': 'POST',
            'url': 'https://qianfan.baidubce.com/v2/app/conversation/runs',
            'headers': {
                'Content-Type': 'application/json',
                'X-Appbuilder-Authorization': 'Bearer bce-v3/ALTAK-wHTCPq678QyUzev1iuaYu/fa292531edaa270804fea1a053bc9d1264fd5723'
            },
            data: JSON.stringify({
                "app_id": "3e32fc42-53b6-495d-a739-38b13c50ca6a",
                "query": req.query.query || "你好",  // 从前端传递查询内容
                "conversation_id": conversationId,  // 使用获取到的 conversation_id
                "stream": false
            })
        };

        const response = await axios(options);
        res.json({ answer: response.data.answer });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: '请求失败' });
    }
});

// 启动服务器
app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
