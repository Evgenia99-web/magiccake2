<template>
  <Header/>
  <div class="container cart">
    <h1 class="home_title">Корзина</h1>
  </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "Cart",
  components: {Footer, Header}
}
</script>

<style scoped>
.home_title{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 700;
  font-size: 64px;
  line-height: 78px;
  color: #4C9691;
  margin-top: 50px;
  margin-bottom: 75px;
  text-align: center;
}
</style>