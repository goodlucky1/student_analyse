<template>
    <div class="base1_left">
        <div class="list_title">
            <list_title></list_title>
        </div>
        <div class="list_main">
            <List_main></List_main>
        </div>
    </div>
    <div class="base1_right">
        <div class="right_top"></div>
        <div class="right_bottom">
            <div class="main_content">
                <router-view></router-view>
            </div>
        </div>
    </div>
</template>
<script>
import List_main from '../base_component/list_main.vue';
import List_title from '../base_component/list_title.vue';
import LoginPage from '../content/LoginPage.vue';

export default{
    name:"base1",
    components:{
        LoginPage,
        List_title,
        List_main
    }
}
</script>
<style>
    
    .base1_left{
        width: 30vw;
        height: 100vh;
        background-color: blue;
        float: left;
        position: fixed;
    }
    .base1_left .list_title{
        position: relative;
    }
    .base1_right{
        width: 68vw;
        height: 100vh;
        float: right;
        position: relative;
        top: 0;
        right: 0;
    }
    .base1_right .right_top{
        width: 68vw;
        height: 15vh;
        background-color: red;
        position: fixed;
        right: 0;
        top: 0;
    }
    .base1_right .right_bottom{
        width: 68vw;
        height: 85vh;
        position: absolute;
        right: 0;
        top: 15vh;
        background-color: beige;
    }
    .base1_right .right_bottom .main_content{
        transform: scale(0.7);
        opacity: 0.85;
    }
</style>