<template>
    <el-menu
    default-active="/home"
    class="el-menu-vertical-demo el_menu"
    :collapse="isClose"
     active-text-color="#ffd04b"
    background-color="#112f50"
    text-color="#fff"
    router
  >
  <el-menu-item><template #title><span>学生管理系统</span></template></el-menu-item>
  <el-menu-item index="/home">
    <el-icon><HomeFilled /></el-icon>
    <span>系统首页</span>
    </el-menu-item>
    <el-sub-menu>
      <template #title>
        <el-icon><Grid /></el-icon>
        <span>信息管理</span>
      </template>
      <el-menu-item-group>
        <el-menu-item index="/info">用户信息</el-menu-item>
      </el-menu-item-group>
    
    </el-sub-menu>
    <el-sub-menu>
      <template #title>
        <el-icon><Calendar /></el-icon>
        <span>课程管理</span>
      </template>
      <el-menu-item-group>
        <el-menu-item index="/course">班级信息</el-menu-item>
      </el-menu-item-group>
    
    </el-sub-menu>
    <el-sub-menu>
      <template #title>
        <el-icon><DocumentChecked /></el-icon>
        <span>成绩管理</span>
      </template>
      <el-menu-item-group>
        <el-menu-item index="/score">成绩信息</el-menu-item>
      </el-menu-item-group>
    
    </el-sub-menu>

  </el-menu>
</template>

<script >

import { ref } from 'vue';
import { useRoute } from 'vue-router';
export default{
    props:["isClose"],
    setup(){
        const isCollapse= ref(false)
        const route=useRoute()
        console.log(route)
        return{
            isCollapse,
            route
        }
    }
}

</script>

<style lang="less" scoped>


.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
.el_menu{
    border-right:none ;
}
</style>
