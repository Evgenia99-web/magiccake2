<template>
  <div class="regist_page">
    <HomeHeader/>
    <div class="regist_block container">
      <img src="src/assets/girl_donat.png" class="welcome_img" alt="">
      <div class="regist_block_form">
        <h2 class="regist_title">Регистрация</h2>
        <div class="regist_form_block">
          <form @submit.prevent="register">
            <div class="input_block">
              <div class="role_choose">
                <p class="role_block_title">Выберете роль {{currentRole.name, currentRole.isCooker, currentRole.isCustomer}}</p>
                <div class="role_inputs">
                  <div class="role_input">
                    <input type="radio" id="customerRole" v-model="currentRole" v-bind:value="{name:'customer', isCustomer:1, isCooker:0}" name="customerRole" checked>
                    <label for="customerRole">Заказчик</label>
                  </div>
                  <div class="role_input">
                    <input type="radio" id="cookerRole" v-model="currentRole" v-bind:value="{name:'cooker',isCustomer:0, isCooker:1}" name="cookerRole">
                    <label for="cookerRole">Кондитер</label>
                  </div>
                </div>
              </div>
              <div class="form_block_item">
                <label for="lastName">Фамилия</label>
                <input v-model="lastName" type="text" id="lastName" placeholder="Введите фамилию"/>
              </div>
              <div class="form_block_item">
                <label for="firstName">Имя</label>
                <input v-model="firstName" type="text" id="firstName" placeholder="Введите имя"/>
              </div>
              <div class="form_block_item">
                <label for="email">Email</label>
                <input v-model="email" type="email" id="email" placeholder="Введите email"/>
              </div>
              <div class="form_block_item">
                <label for="username">Логин</label>
                <input v-model="username" type="text" id="username" placeholder="Введите логин"/>
              </div>
              <div class="form_block_item">
                <label for="password">Пароль</label>
                <input v-model="password" type="password" id="password" placeholder="Введите пароль"/>
              </div>
              <div class="form_block_item">
                <label for="confirmPassword">Повторите пароль</label>
                <input v-model="passwordConfirm" type="password" id="confirmPassword" placeholder="Введите пароль"/>
              </div>
            </div>
            <button type="submit" class="auth_btn">Зарегистрироваться</button>
          </form>
          <span class="not_yet">У вас уже есть аккаунт? <router-link to="Auth">Войти</router-link></span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import HomeHeader from "@/components/HomeHeader.vue";

export default {
  name: "Registration",
  components: {HomeHeader},
  data() {
    return{
      email: '',
      password: '',
      passwordConfirm: '',
      firstName: '',
      lastName: '',
      username: '',
      currentRole: {}
    };
  },
  methods: {
    register () {
      const formData = {
        email: this.email,
        password: this.password,
        username: this.username,
        first_name: this.firstName,
        last_name: this.lastName,
        is_cooker: this.currentRole.isCooker,
        is_customer:this.currentRole.isCustomer
      }
      this.$store.dispatch('signup', formData)
    },
  }
}
</script>

<style scoped>
header{  margin-top: 0; margin-bottom: 20px}
.regist_page{
  background: url("src/assets/bg_regist.png") no-repeat center;
  background-size: cover;
  height: 100vh;
  padding-top: 35px;
}
.regist_block{display: flex; justify-content: space-between; align-items: center;}
.welcome_img{ width: 550px;}
.regist_title{
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 700;
  font-size: 40px;
  line-height: 59px;
  color: #FFFFFF;
  text-align: center;
  margin-bottom: 20px;
}
.regist_form_block{text-align: center;}
.input_block{width: 680px; display: flex; flex-wrap: wrap; justify-content: space-between;}
.form_block_item{width: 320px; text-align: left; margin-bottom: 7px;}
.form_block_item label, label, .role_block_title{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 500;
  font-size: 16px;
  line-height: 20px;
  color: #7394B8;
  margin-bottom: 6px;
  margin-left: 30px;
}
.role_block_title{color: #FFFFFF; margin-left: 0; font-weight: 600;}
.form_block_item input, .form_block_item select{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 300;
  font-size: 16px;
  line-height: 20px;
  color: #8AABCE;
  background: rgba(255, 255, 255, 0.46);
  border: 2px solid #7394B8;
  border-radius: 25px;
  width: 100%;
  padding: 13px 27px;
}
.auth_btn{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 20px;
  color: #FFFFFF;
  padding: 12px 27px;
  margin-top: 10px;
  margin-bottom: 30px;
  background: #8AABCE;
  border-radius: 25px;
  border: none;
}
.not_yet{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 20px;
  color: #5280B1;
}
.role_choose{ width: 100%;}
.role_inputs{display: flex; justify-content: space-around;}
</style>