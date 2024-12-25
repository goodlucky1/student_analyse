<template>
<div class="contain">
  <div class="menu">
    <MyMenu :isClose="isClose"></MyMenu>
   
  </div>
  <div class="content" :class="{active:isClose}">
    <MyContent :isClose="isClose" @change="change"></MyContent>
  </div>
</div>
</template>

<script >
import { ref } from 'vue';
import MyContent from './MyContent.vue';
import MyMenu from './MyMenu.vue';




export default{
    components:{
        MyContent,
        MyMenu,
        
    },
    setup(){
        //定义变量
        let isClose= ref(false)

        const change=()=>{
            isClose.value=!isClose.value
        }
        return{
            isClose,
            change
        }
    }
}

</script>

<style lang="less" scoped>
@import '../assets/css/base.css';
    .menu{
        position: fixed;
        top: 0;
        left: 0;
        bottom: 0;
        background-color: #112f50;
    }
    .content{
        padding-left:200px ;
       
       
    }
    .active{
        padding-left: 64px;
    }
   
</style>
    
