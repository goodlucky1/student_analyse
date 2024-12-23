<template>
  <div class="auth-container">
    <div class="form-box">
      <h2 class="title">登录</h2>
      <form @submit.prevent="handleLogin">
        <div class="input-group">
          <label for="username">用户名</label>
          <input v-model="username" type="text" id="username" placeholder="请输入用户名" required :disabled="isSubmitting" />
        </div>
        <div class="input-group">
          <label for="password">密码</label>
          <input v-model="password" type="password" id="password" placeholder="请输入密码" required :disabled="isSubmitting" />
        </div>
        <button type="submit" class="submit-btn" :disabled="isSubmitting">登录</button>
      </form>
      <p>没有账户？<router-link to="/register">注册</router-link></p>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ElMessage } from 'element-plus';

export default {
  mounted() {
    document.title = '用户登录'; // 修改页面标题
    document.body.classList.add("global-background");
  },
  data() {
    return {
      username: '',
      password: '',
      errorMessage: '',  // 用于存储错误信息
      isSubmitting: false, // 是否正在提交
    };
  },
  methods: {
    async handleLogin() {
      // 清空之前的错误信息
      this.errorMessage = '';
      this.isSubmitting = true; // 设置为提交中，禁用表单

      // 简单的表单验证
      if (!this.username || !this.password) {
        this.errorMessage = '用户名和密码不能为空';
        this.isSubmitting = false;
        return;
      }

      try {
        // 发送登录请求到后端
        const response = await axios.post('http://localhost:3000/api/login', {
          username: this.username,
          password: this.password,
        });

        // 登录成功后的处理
        if (response.data.success) {
          ElMessage.success('登录成功');
          this.$router.push("/home"); // 登录成功跳转到首页
        } else {
          // 登录失败的处理
          this.errorMessage = response.data.message || '登录失败，请检查用户名和密码';
          ElMessage.error(this.errorMessage);
        }
      } catch (error) {
        console.error('登录请求出错：', error);
        this.errorMessage = '登录请求失败，请稍后再试';
        ElMessage.error(this.errorMessage);
      } finally {
        this.isSubmitting = false; // 请求完成，恢复表单
      }
    }
  }
};
</script>

<style scoped>
/* 居中容器 */
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

/* 表单框样式 */
.form-box {
  width: 90%;
  max-width: 400px;
  padding: 30px;
  background: rgba(255, 255, 255, 0.9); /* 半透明背景 */
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
  align-items: center; /* 垂直居中对齐 */
}

.input-group label {
  width: 100px;
  text-align: right;
  margin-right: 15px; /* 标签和输入框之间的间距 */
}

.input-group input {
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
  background-color: #6c63ff;
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
  background-color: #5149b2;
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
