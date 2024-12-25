<template>
    <nav aria-label="Page navigation">
      <ul class="pagination">
        <li class="page-item" :class="{ disabled: current === 1 }">
          <button class="page-link" @click="goToPage(1)">首页</button>
        </li>
        <li class="page-item" :class="{ disabled: current === 1 }">
          <button class="page-link" @click="goToPage(current - 1)">上一页</button>
        </li>
        <li class="page-item" :class="{ disabled: current === total }">
          <button class="page-link" @click="goToPage(current + 1)">下一页</button>
        </li>
        <li class="page-item" :class="{ disabled: current === total }">
          <button class="page-link" @click="goToPage(total)">尾页</button>
        </li>
      </ul>
    </nav>
  </template>
  
  <script>
  export default {
    name:"dzy_s",
    props: {
      current: Number,
      total: Number,
      pageSize: Number,
    },
    methods: {
      goToPage(page) {
        if (page < 1 || page > this.total) return;
        this.$emit('change', page);
      },
    },
  };
  </script>
