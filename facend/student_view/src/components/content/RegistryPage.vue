<template>
    <div class="registry_main">
        <ul class="registry_list">
            <li>
                <div class="registry_title">注册</div>
            </li>
            <li>
                <div class="input-group input-group-sm mb-3 registry_input">
                    <span class="input-group-text registry_span" id="inputGroup-sizing-sm"><img class="registry_img"
                            src="../../assets/img/icon/loginOrRegistry/user.svg" /></span>
                    <input type="text" class="form-control registry" aria-label="Sizing example input"
                        aria-describedby="inputGroup-sizing-sm" v-model="username" placeholder="请输入用户名">
                </div>
            </li>
            <li>
                <div class="input-group input-group-sm mb-3 registry_input">
                    <span class="input-group-text registry_span" id="inputGroup-sizing-sm"><img class="registry_img"
                            src="../../assets/img/icon/loginOrRegistry/password.svg" /></span>
                    <input type="text" class="form-control registry" aria-label="Sizing example input"
                        aria-describedby="inputGroup-sizing-sm" v-model="password" placeholder="请输入密码">
                </div>
            </li>
            <li>
                <div class="input-group input-group-sm mb-3 registry_input">
                    <span class="input-group-text registry_span" id="inputGroup-sizing-sm"><img class="registry_img"
                            src="../../assets/img/icon/loginOrRegistry/email.svg" /></span>
                    <input type="text" class="form-control registry" aria-label="Sizing example input"
                        aria-describedby="inputGroup-sizing-sm" v-model="email" placeholder="请输入邮箱">
                </div>
            </li>
            <li>
                <div class="input-group mb-3 registry_input">
                    <select class="form-select" aria-label="Default select example" v-model="userRole">
                        <option value="管理员" selected>管理员</option>
                        <option value="普通用户">普通用户</option>
                        <option value="未知用户">未知用户</option>
                    </select>
                </div>
            </li>
            <li>
                <button type="button" class="btn btn-outline-primary registry_btn" @click="post()">注册</button>
            </li>
        </ul>

        <ul>
            <li>

            </li>
        </ul>
    </div>
</template>
<script>
import axios from 'axios';

export default{
    name:"registryPage",
    data(){
        return{
            email:"",
            username:"",
            password:"",
            userRole:"管理员"
        }
    },
    methods:{
        get(){

        },
        post() {

            console.log(this.email)
            axios.post("api/registry", 
            {email:this.email,username:this.username,password:this.password,userRole:this.userRole},
            {headers:{'Content-Type':'application/json'}}
        )
                .then(x => {
                    console.log(x)
                    if (x.data.result == "success") {
                        this.$router.push("/login");
                    }
                })
                .catch(x => {
                    console.log(x)
                })

                

        }
        
    }
}

 




</script>
<style scoped >
   @import '/src/assets/css/registry.css';
</style>