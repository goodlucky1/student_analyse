<template>
    <ul class="list_ul">
        <li><router-link :to="{ name: 'main' }">首页</router-link></li>
        <li><router-link :to="{ name: 'login' }">登录</router-link></li>
        <li><router-link :to="{ name: 'registry' }">注册</router-link></li>
    </ul>
</template>
<script>
export default{
    name:"listMain"
}
</script>
<style>
    .list_ul{
        width: 30vw;
        position: absolute;
        left: -1vw;
        top: 11vh;

        list-style-type: none;
    }
    .list_ul li{
        width: 28vw;
        height: 10vh;
        margin-top: 1vh;
        border: 2px solid black;

        font-size: 20px;
        text-align: center;
        line-height: 10vh;
        
        box-shadow: 0 0 2vw black;
    }
</style>