<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Home from './components/Home.vue'
import Conversation from './components/Conversation.vue'
import MessageItem from './components/MessageItem.vue'

// export default {
//   name: 'App',
//   // Here we register the components which
//   // we are going to use in the template
//   components: {
//     Home,
//     Conversation,
//     MessageItem
//   },
//   // This is going to be called 
//   //  when the component gets rendered
//   data: () => ({
//     messages: [
//       // {
//       //   'isMine': true,
//       //   'author': 'Me',
//       //   'text': 'Hello'
//       // },
//       // {
//       //   'isMine': false,
//       //   'author': 'GPT',
//       //   'text': 'Hello, can I help you?'
//       // }
//     ]
//   })
// }

</script>

<template>
  <RouterView />
  <!-- <Conversation /> -->
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
