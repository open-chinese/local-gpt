我给你一个Vue.js的.vue文件，里面包含了一个消息列表messages，和对应显示每一个message的component，还包含了一个input的组件，每次input发送的内容通过调用远程调用请求fetch api来获得回复，回复的内容也会添加到messages列表中，并显示出来。每次增加新的消息，列表都应该刷新到最底下。

我的Dialog.vue的内容如下，请帮我看看有没有bug，并帮我修正。

<script setup>
import MessageItem from './MessageItem.vue'

import { reactive } from 'vue';
import { ref } from 'vue';


const messages = ref([
      {
        'id': 0,
        'isMine': true,
        'role': 'user',
        'text': 'Hello',
        'avatar': '../assets/image/user-100.png'
      }
    ])

const inputValue = ref('');
const messageIndex = ref(0);
 

const sendRequest = async () => {
  try {
    console.log('Sending request with value:', inputValue.value);
    messageIndex.value += 1;

    messages.value.push({
        'id': messageIndex.value,
        'isMine': true,
        'role': 'user',
        'text': inputValue.value,
        'avatar': '../assets/image/user-100.png'
    })

    const raw = JSON.stringify({
      "query": inputValue.value
    });

    const response = await fetch('http://localhost:5050/answers', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
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
   }
   catch (error) {
     console.error('Error sending request:', error);
   }
 };
 
</script>

<template>
  <div class="chat_view">
  <MessageItem v-for='message in messages' 
               :text="message.text"
               :role="message.role"
               :avatar="message.avatar">
  </MessageItem>
  <input v-model="inputValue" @keyup.enter="sendRequest">
</div>

</template>


<style scoped>
input {
  min-height: 20px;
  max-height: 50px;
  box-sizing: border-box;
  padding: 10px;
  padding-left: 20px;
  margin-left: 20px;
  margin-right: 20px;
  width: 1040px;
  outline: none;
  transition: all 0.2s;
  border-radius: 8px;
}
 
input:not(:placeholder-shown) {
  min-height: 50px;
}

.chat_view {
  padding: 8px;
  border-radius: 4px;
  width: 1080px;
}
</style>
