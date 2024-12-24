<template>
    <div class="header">
      <div class="icon">
        <el-icon v-if="isClose" @click="change"><Expand /></el-icon>
        <el-icon v-else @click="change"><Fold /></el-icon>
      </div>

      <div class="right">
        <div class="time">
          {{ time }}
        </div>
        <div class="line">|</div>
        <div class="loginout" @click="out">
          <el-icon><SwitchButton /></el-icon>
        </div>
      </div>
    </div>
    
  <div class="wrapper">
    <router-view></router-view>
  </div>
</template>

<script >
import { onMounted, ref } from 'vue';
import dayjs from 'dayjs';
import { useRouter } from 'vue-router';



export default{
  props:["isClose"],
  emits:["change"],
  setup(props,{emit}){
    let time=ref(null)
    const router=useRouter();
    const change=()=>{
      emit("change")
    }

    onMounted(()=>{
      time.value=dayjs(new Date()).format('YYYY-MM-DD HH:mm:ss')
    })

    const out=()=>{
      router.push("/login")
    }
    return{
      change,
      time,
      out
    }
  }
}

</script>

<style lang="less" scoped>
.header{
    height: 50px;
    line-height: 50px;
    background-color: #1e78bf;
    color: #fff;
    display: flex;
    .icon{
      font-size: 24px;
      flex: 1;
      i{
        cursor: pointer;
      }
    }
    .right{
      // float: right;
      padding-right: 20px;
      display: flex;
    
      .time{
        font-size: 12px;
      }
      .line{
        padding-left: 10px;
        padding-right: 10px;
      }
      .loginout{
        margin-top: 2px;
      }
    }
    }
.wrapper{
    margin: 10px;
   }
</style>