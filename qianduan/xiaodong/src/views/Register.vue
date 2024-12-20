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
        <button type="submit" class="submit-btn">注册</button>
      </form>
      <p>已经有账户？<router-link to="/">登录</router-link></p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  mounted() {
    // 设置全局背景
    document.body.classList.add("global-background");
  },
  beforeDestroy() {
    // 清除全局背景样式
    document.body.classList.remove("global-background");
  },
  data() {
    return {
      username: '',
      password: '',
      confirmPassword: '',
    };
  },
  methods: {
    async handleRegister() {
      // 检查密码是否匹配
      if (this.password !== this.confirmPassword) {
        alert('密码不匹配！');
        return;
      }

      try {
        // 发送注册请求到后端
        const response = await axios.post('http://localhost:3000/api/register', {
          username: this.username,
          password: this.password,
        });

        // 注册成功后的处理
        if (response.data.success) {
          alert('注册成功！');
          this.$router.push('/'); // 跳转到登录页面
        } else {
          alert('注册失败：' + response.data.message);
        }
      } catch (error) {
        console.error('注册请求出错：', error);
        alert('注册失败，请稍后再试');
      }
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
}

/* 表单框样式 */
.form-box {
  width: 90%;
  max-width: 400px;
  padding: 30px;
  background: rgba(255, 255, 255, 0.8);
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

.submit-btn:hover {
  background-color: #5149b2;
}

p {
  margin-top: 20px;
  color: #555;
}
</style>
