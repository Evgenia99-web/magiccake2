<template>
  <header>
    <div class="container header">
      <div class="left_side">
        <div class="nav_left_side">
          <router-link :to="{name: 'Home'}" class="nav_item">Главная</router-link>
          <router-link :to="{name: 'About'}" class="nav_item">О портале</router-link>
          <router-link :to="{name: 'Cookers'}" class="nav_item">Кондитеры</router-link>
        </div>
        <div class="left_side_name">
          <p class="main_name left_name">MAGIC</p>
        </div>
      </div>
      <div class="logo_center">
        <router-link :to="{name: 'Home'}">
          <img src="src/assets/logo.png" class="logo green" alt="логотип Magoc Cake">
        </router-link>
      </div>
      <div class="right_side">
        <div class="right_side_name">
          <p class="main_name right_name">CAKE</p>
        </div>
        <div class="nav_right_side">
          <router-link :to="{name: 'Home'}" class="nav_item">Рецепты</router-link>
          <router-link :to="{name: 'Home'}" class="nav_item">Публикации</router-link>
        </div>
        <div class="profiles_block">
          <router-link v-if='!auth' :to="{name: 'Auth'}" class="profile">
            <img src="src/assets/profile.png" class="profile_icon_gray" alt="Профиль">
          </router-link>
          <router-link v-if='auth' :to="{name: 'Profile'}" class="profile">
            <img src="src/assets/user_auth_green.png" class="profile_icon_gray" alt="Профиль">
          </router-link>
          <router-link :to="{name: 'Cart'}" class="cart">
            <img src="src/assets/cart.png" class="cart_icon_gray" alt="Корзина">
          </router-link>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: "Header",
  computed: {
      auth () {
        return this.$store.getters.ifAuthenticated
      }
    },
}
</script>

<style scoped>
.header, .left_side, .right_side, .profiles_block{
  display: flex;
  justify-content: space-between;
  align-items: center;
}
header{width: 100%;  margin-top: 35px;  margin-bottom: 50px;z-index: 2;}
.left_side, .right_side{
  width: 550px;
  border-bottom: 1px solid #69BEB8;
  padding-bottom: 18px;
}
.nav_item{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 400;
  font-size: 18px;
  line-height: 20px;
  color: #808080;
  margin-right: 41px;
}
.cart{  margin-left: 20px;}
.logo_center{  margin: 0 23px;}
.main_name{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 44px;
  color: #808080;
}
.profile_icon_gray{max-width: 35px;}
</style>