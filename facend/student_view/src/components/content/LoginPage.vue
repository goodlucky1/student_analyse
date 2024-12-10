<template>
     <div class="login_main">
        <ul class="login_list">
            <li>
                <div class="login_title">登录</div>
            </li>
            <li>
                <div class="input-group input-group-sm mb-3 login_input">
                    <span class="input-group-text login_span" id="inputGroup-sizing-sm"><img class="login_img"
                            src="../../assets/img/icon/loginOrRegistry/user.svg" /></span>
                    <input type="text" class="form-control login" aria-label="Sizing example input"
                        aria-describedby="inputGroup-sizing-sm" placeholder="请输入用户名">
                </div>
            </li>
            <li>
                <div class="input-group input-group-sm mb-3 login_input">
                    <span class="input-group-text login_span" id="inputGroup-sizing-sm"><img class="login_img"
                            src="../../assets/img/icon/loginOrRegistry/password.svg" /></span>
                    <input type="text" class="form-control login" aria-label="Sizing example input"
                        aria-describedby="inputGroup-sizing-sm" placeholder="请输入密码">
                </div>
            </li>
            <li>
                <button type="button" class="btn btn-outline-primary login_btn">登录</button>
            </li>
        </ul>
    </div>

</template>
<script>
export default{
    name:"loginPage"
}



</script>
<style scoped>
      @import "/src/assets/css/login.css";

</style>