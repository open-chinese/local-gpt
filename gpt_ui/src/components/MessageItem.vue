<script setup>
defineProps(['text', 'role'])
</script>

<template>
  <div class="item">
    <i>
      <slot name="icon"></slot>
      <img v-if="role == 'user'" src="../assets/image/user-100.png" width="40" height="40" fill="currentColor"/>
      <img v-else src="../assets/image/gpt-100.png" width="40" height="40" fill="currentColor"/>
    </i>

    <div class="details">
      <h3>
        {{ role }}
        <!-- <slot name="heading"></slot> -->
      </h3>
      {{ text }}
      <!-- <slot></slot> -->
    </div>
  </div>

  <!-- <template #icon>
      <img src="../assets/image/gpt-100.png" width="40" height="40" fill="currentColor"/>
    </template>
  <template #heading>LocalGPT</template> -->

</template>

<style scoped>
.item {
  margin-top: 2rem;
  display: flex;
  position: relative;
  padding-left: 120px;
  padding-right: 120px;
  /* background-color: bisque; */
}

.details {
  flex: 1;
  margin-left: 1rem;

  /* padding-left: 10px;
  padding-right: 10px; */

  /* background-color: aquamarine; */
  width: 960px;

  white-space: pre-wrap; /* CSS3属性，支持换行、空格和自动换行 */
  word-wrap: break-word; /* 强制英文单词或URL地址的换行 */
}

i {
  display: flex;
  place-items: center;
  place-content: center;
  width: 32px;
  height: 32px;
  color: var(--color-text);
}

h3 {
  font-size: 1.2rem;
  font-weight: 500;
  margin-bottom: 0.4rem;
  color: var(--color-heading);
}

@media (min-width: 1024px) {
  .item {
    margin-top: 0;
    padding: 0.4rem 0 1rem calc(var(--section-gap) / 2);
  }

  
  i {
    /* 图像的位置 top: calc(50% - 25px);*/
    top: 4px;
    left: 20px;
    position: absolute;
    border: 1px solid var(--color-border);
    background: var(--color-background);
    border-radius: 8px;
    width: 50px;
    height: 50px;
  }

  .item:before {
    content: ' ';
    border-left: 1px solid var(--color-border);
    position: absolute;
    left: 0;
    bottom: calc(50% + 25px);
    height: calc(50% - 25px);
  }

  .item:after {
    content: ' ';
    border-left: 1px solid var(--color-border);
    position: absolute;
    left: 0;
    top: calc(50% + 25px);
    height: calc(50% - 25px);
  }

  .item:first-of-type:before {
    display: none;
  }

  .item:last-of-type:after {
    display: none;
  }
}
</style>
