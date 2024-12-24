<template>
  
  <base1></base1>
</template>

<script>
import base1 from './components/base/base1.vue';
import axios from 'axios';



export default {
  name: 'App',
  components: {
    base1
  }
}


axios.get('api')
.then(x=>{console.log(x)})
</script>

<style>
    @import '/src/assets/css/bootstrap.min.css';
</style>
