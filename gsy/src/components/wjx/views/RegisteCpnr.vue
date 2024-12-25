<template>
  <div class="auth-container">
    <div class="form-box">
      <h2 class="title">注册</h2>
      <form @submit.prevent="handleRegister">
        <div class="input-group">
          <label for="username">用户名</label>
          <input v-model="username" type="text" id="username" placeholder="请输入用户名" required />
        </div>
        <div class="input-group">
          <label for="password">密码</label>
          <input v-model="password" type="password" id="password" placeholder="请输入密码" required />
        </div>
        <div class="input-group">
          <label for="confirmPassword">确认密码</label>
          <input v-model="confirmPassword" type="password" id="confirmPassword" placeholder="确认密码" required />
        </div>
        <div class="input-group">
          <label for="email">邮箱</label>
          <input v-model="email" type="email" id="email" placeholder="请输入邮箱" required />
        </div>
        <div class="input-group">
          <label for="userRole">用户类型</label>
          <select id="userRole" v-model="userRole" :disabled="isSubmitting">
            <option value="管理员">管理员</option>
            <option value="普通用户">普通用户</option>
            <option value="未知用户">未知用户</option>
          </select>
        </div>
        <button type="submit" class="submit-btn" :disabled="isSubmitting">注册</button>
      </form>
      <p>已经有账户？<router-link to="/login">登录</router-link></p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ElMessage } from 'element-plus';

export default {
  mounted() {
    document.title = '用户注册';
    document.body.classList.add("global-background");
  },
  beforeUnmount() {
    document.body.classList.remove("global-background");
  },
  data() {
    return {
      username: '',
      password: '',
      confirmPassword: '',
      email: '',
      userRole: '普通用户', 
      isSubmitting: false, 
    };
  },
  methods: {
    async handleRegister() {
      if (this.password !== this.confirmPassword) {
        ElMessage.error("两次密码不一致");
        return;
      }
      this.isSubmitting = true; 

      try {
        const res = await axios.post("/api/registry", {
          username: this.username,
          password: this.password,
          email: this.email,
          userRole: this.userRole,
        });

        if (res.data.result === "success") {
          ElMessage.success("注册成功");
          this.$router.push("/login"); 
        } else {
          ElMessage.error("注册失败，请重试\n "+res.data);
        }
      } catch (error) {
        ElMessage.error("网络错误，请稍后再试");
      } finally {
        this.isSubmitting = false;
      }
    },
  },
};
</script>

<style scoped>
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-image: url("/src/assets/img/渐变背景.jpg");
  background-size: cover;
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  overflow: hidden;
}

.form-box {
  width: 90%;
  max-width: 400px;
  padding: 30px;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  text-align: center;
}

.title {
  margin-bottom: 20px;
  font-size: 28px;
  color: #4a4a4a;
  font-weight: bold;
}

.input-group {
  margin-bottom: 20px;
  display: flex;
  align-items: center;
}

.input-group label {
  width: 100px;
  text-align: right;
  margin-right: 15px; 
}

.input-group input,
.input-group select {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.submit-btn {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  background-color: #4db690d8;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-btn:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.submit-btn:hover:enabled {
  background-color: #68c5f0c3;
}

p {
  margin-top: 20px;
  color: #555;
}

.error-message {
  color: #f56c6c;
  margin-top: 15px;
  font-size: 14px;
}
</style>
