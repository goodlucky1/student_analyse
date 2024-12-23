<template>
  <div class="auth-container">
    <div class="form-box">
      <h2 class="title">注册</h2>
      <form @submit.prevent="handleRegister">
        <div class="input-group">
          <label for="username">用户名</label>
          <input v-model="username" type="text" id="username" placeholder="请输入用户名" required :disabled="isSubmitting" />
        </div>
        <div class="input-group">
          <label for="password">密码</label>
          <input v-model="password" type="password" id="password" placeholder="请输入密码" required :disabled="isSubmitting" />
        </div>
        <div class="input-group">
          <label for="confirmPassword">确认密码</label>
          <input v-model="confirmPassword" type="password" id="confirmPassword" placeholder="确认密码" required :disabled="isSubmitting" />
        </div>
        <div class="input-group">
          <label for="email">邮箱</label>
          <input v-model="email" type="email" id="email" placeholder="请输入邮箱" required :disabled="isSubmitting" />
        </div>
        <div class="input-group">
          <label for="userRole">用户类型</label>
          <select id="userRole" v-model="userRole" :disabled="isSubmitting">
            <option value="管理员">管理员</option>
            <option value="普通用户">普通用户</option>
            <option value="未知用户">未知用户</option>
          </select>
        </div>
        <button type="submit" class="submit-btn" :disabled="isSubmitting">{{ isSubmitting ? '注册中...' : '注册' }}</button>
      </form>
      <p>已经有账户？<router-link to="/">登录</router-link></p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ElMessage } from 'element-plus';

export default {
  mounted() {
    document.body.classList.add("global-background");
  },
  beforeDestroy() {
    document.body.classList.remove("global-background");
  },
  data() {
    return {
      username: '',
      password: '',
      confirmPassword: '',
      email: '',
      userRole: '',
      isSubmitting: false,
    };
  },
  methods: {
    async handleRegister() {
      if (this.password != this.confirmPassword) {
        ElMessage.error("两次密码不一致")
        return
      }
      axios.post("api/registry",
        {
          username: this.username,
          password: this.password,
          email: this.email,
          userRole:this.userRole
        }
      ).then(res => {
        console.log(res)
        if(res.data.result=="success"){
          ElMessage.success("成功")
          this.$router.push("/")
          return
        }
        ElMessage.error("注册失败")
      })
      .catch(res=>{
        console.log(res)
        ElMessage.error("ERROR")
      })
       
    },
  },
};
</script>

<style scoped>
/* 居中容器 */
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(to bottom right, #6c63ff, #e0e7ff);
}

/* 表单框样式 */
.form-box {
  width: 90%;
  max-width: 400px;
  padding: 30px;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.title {
  margin-bottom: 20px;
  font-size: 28px;
  color: #333;
  font-weight: bold;
  text-align: center;
}

.input-group {
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
}

.input-group label {
  margin-bottom: 5px;
  font-size: 14px;
  color: #555;
}

.input-group input,
.input-group select {
  padding: 12px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 8px;
  transition: border-color 0.3s;
}

.input-group input:focus,
.input-group select:focus {
  border-color: #6c63ff;
  outline: none;
}

.submit-btn {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  background-color: #6c63ff;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-btn:disabled {
  background-color: #aaa;
  cursor: not-allowed;
}

.submit-btn:hover:enabled {
  background-color: #5149b2;
}

p {
  margin-top: 20px;
  font-size: 14px;
  color: #555;
}
</style>
