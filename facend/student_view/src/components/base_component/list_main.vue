<template>
    <ul class="list_ul">
        <li><router-link class="list_link" :to="{ name: 'main' }">首页</router-link></li>
        <li><router-link class="list_link" :to="{ name: 'login' }">登录</router-link></li>
        <li><router-link class="list_link" :to="{ name: 'registry' }">注册</router-link></li>
    </ul>
</template>
<script>
export default{
    name:"listMain"
}
</script>
<style>
    .list_ul{
        width: 20vw;
        position: absolute;
        left: 0.1vw;
        top: 11vh;

        list-style-type: none;

        padding: 0;
    }
    .list_ul li{
        width: 18vw;
        height: 8vh;
        margin-top: 1vh;
        border: 2px solid black;

        background-color: black;

        font-size: 20px;
        text-align: center;
        line-height: 8vh;
        
        box-shadow: 0 0 2vw black;
    }
    .list_link{
        color: whitesmoke;
        text-decoration: none;
    }
</style>