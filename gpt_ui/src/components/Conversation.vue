<script setup>
import MessageItem from './MessageItem.vue'

import { reactive } from 'vue';
import { ref } from 'vue';


const messages = ref([
      // {
      //   'id': 0,
      //   'isMine': true,
      //   'role': 'user',
      //   'text': 'Hello',
      //   'avatar': '../assets/image/user-100.png'
      // }
    ])

const inputValue = ref('');
const messageIndex = ref(0);
 

const sendRequest = async () => {
  try {
    // 发送请求的逻辑
    console.log('Sending request with value:', inputValue.value);
    messageIndex.value += 1;


    const query = inputValue.value;

    const requestMessage = {
        'id': messageIndex.value,
        'isMine': true,
        'role': 'user',
        'text': query,
        'avatar': '../assets/image/user-100.png'
    }

    messages.value.push(requestMessage)
    inputValue.value = '';




    const gptInputRequests = [
        {
          "role": "system",
          "content": "假设你的名字叫程景，你的个人信息如下\n：程景，小名小景，英文名叫Jason，男，19岁，身高180cm，体重70公斤，武汉大学计算机系大一新生，兴趣爱好是看电影、钢琴、打篮球。我是你的室友，名字叫小黑，在微信上和你聊天。\n请结合人设完成对话，要求尽量简短、自然。"
        },
        {
          "role": "user",
          "content": "[小黑]" + query
        },
        {
          "role": "assistant",
          "content": "[程景]"
        }
      ]

    const raw = JSON.stringify({
      "top_p": 0.95,
      "messages": gptInputRequests,
      "stop_words": [
        "。"
      ],
      "max_tokens": 40,
      "frequency_penalty": 0,
      "timeout": 30,
      "n": 1,
      "temperature": 1,
      "presence_penalty": 0
    });



    const response = await fetch('http://localhost:5050/gpt/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        "Access-Control-Allow-Origin": "*"
      },
      // body: JSON.stringify({ message: inputValue.value })
      body: raw
    });

    const data = await response.json();
    if (data != null && "candidates" in data)
    {
      const responseText = data["candidates"][0]

      messageIndex.value += 1;

      messages.value.push({
        'id': messageIndex.value,
        'isMine': false,
        'role': 'gpt',
        'text': responseText,
        'avatar': '../assets/image/gpt-100.png'
    })
    }


    
    // await nextTick();
    document.querySelector('.chat_view').scrollTop = document.querySelector('.chat_view').scrollHeight;






   }
   catch (error) {
     console.error('Error sending request:', error);
   }
 };
 
 
 
</script>

<template>
  <!-- <MessageItem text="!!!!!!!!!">
    <template #icon>
      <img src="../assets/image/gpt-100.png" width="40" height="40" fill="currentColor"/>
    </template>
    <template #heading>LocalGPT</template>

    Hello, what is your name
  </MessageItem>

  <MessageItem>
    <template #icon>
      <img src="../assets/image/user-100.png" width="40" height="40" fill="currentColor"/>
    </template>
    <template #heading>Me</template>
    Hello, my name is Li.
  </MessageItem> -->

  <!-- <MessageItem v-for='message in messages'
               :key='message.id'
               :class='message'
               :dark='message.isMine'
               :text='message.text'
               :author='message.author'
  /> -->



  <div class="chat_view">
  <MessageItem v-for='message in messages' 
               :text="message.text"
               :role="message.role"
               :avatar="message.avatar">
    <!-- <template #icon>
      <img src="../assets/image/gpt-100.png" width="40" height="40" fill="currentColor"/>
    </template>
    <template #heading>LocalGPT</template> -->

    <!-- {{ message.text }} -->
  </MessageItem>


  <!-- 使用v-for，然后再template中加入{{ variable }}也可以 -->
  <!-- here is the list view -->
  <!-- <MessageItem v-for='message in messages'>
    <template #icon>
      <img src="../assets/image/gpt-100.png" width="40" height="40" fill="currentColor"/>
    </template>
    <template #heading>LocalGPT</template>

    {{ message.text }}
  </MessageItem> -->


  <input v-model="inputValue" @keyup.enter="sendRequest">
</div>

</template>


<style scoped>
/* input {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
} */

input {
  min-height: 20px; /* 最小高度 */
  max-height: 50px; /* 最大高度 */
  box-sizing: border-box; /* 防止内边距和边框增加总高度 */
  padding: 10px; /* 内边距 */
  padding-left: 20px;
  margin-left: 20px;
  margin-right: 20px;
  width: 1040px;
  /*width: 100%; /* 宽度 */
  outline: none; /* 去除点击input时的默认边框 */
  transition: all 0.2s; /* 平滑的动画过渡效果 */
  border-radius: 8px;
}
 
/* 在输入时，input的高度会根据内容自适应增长，达到max-height后停止增长 */
input:not(:placeholder-shown) {
  min-height: 50px;
}

.chat_view {
  padding: 8px;
  /* border: 1px solid blue; */
  border-radius: 4px;
  width: 1080px;
}
</style>
