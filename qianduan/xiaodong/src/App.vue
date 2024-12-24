<template>
  <router-view />
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
body.global-background {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  
  /* 背景图设置 */
  background-image: url(assets/xiaoshuai.jpg);
  background-size: cover;            /* 背景图按比例铺满 */
  background-position: center center; /* 背景图居中 */
  background-attachment: fixed;       /* 背景图固定在视口 */
  
  height: 100vh;                      /* 高度设置为视口高度 */
  width: 100%;                        /* 确保宽度占满整个页面 */
  overflow: hidden;                   /* 防止滚动条 */
}

</style>