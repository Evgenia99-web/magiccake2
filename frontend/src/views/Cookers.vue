<template>
  <Header/>
  <div class="cookers_top">
    <img src="src/assets/left_hand.png" class="left_hand" alt="">
    <div class="container cookers_top_block">
      <h1 class="home_title">Кондитеры</h1>
      <p class="top_name">Топ кондитеров</p>
      <div class="top_block">
        <div class="second_place">
          <div class="photo_place">
            <img src="src/assets/olga.jpg" class="cook_photo" alt="">
            <p class="place">2</p>
          </div>
          <p class="cook_name">Шишова Ольга</p>
          <p class="cook_city">Москва</p>
        </div>
        <div class="first_place">
          <div class="photo_place">
            <img src="src/assets/polina.jpg" class="cook_photo" alt="">
            <p class="place">1</p>
          </div>
          <p class="cook_name">Филимонова Полина</p>
          <p class="cook_city">Москва</p>
        </div>
        <div class="third_place">
          <div class="photo_place">
            <img src="src/assets/nacty.jpg" class="cook_photo" alt="">
            <p class="place">3</p>
          </div>
          <p class="cook_name">Лазарева Анастасия</p>
          <p class="cook_city">Москва</p>
        </div>
      </div>
    </div>
    <div class="container cooker_list_block">
      <div class="cooker_filter">
        <form @submit="" class="filter_form">
          <div class="form_block_item">
                <label for="city">Город</label>
                <input v-model="city" type="text" id="city" placeholder="Введите город"/>
          </div>
          <button class="search_btn">Найти</button>
        </form>
      </div>
      <div class="cooker_list">
        <div class="cooker_item">
          <div class="rating">
            <img src="src/assets/heart.png" class="heart_img" alt="">
            <p class="count">5.0</p>
          </div>
          <img src="src/assets/polina.jpg" class="cooker_photo" alt="">
          <p class="cooker_name">Филимонова Полина</p>
          <router-link to="cooker_page" class="go_to">Перейти</router-link>
        </div>
        <div class="cooker_item">
          <div class="rating">
            <img src="src/assets/heart.png" class="heart_img" alt="">
            <p class="count">4.8</p>
          </div>
          <img src="src/assets/olga.jpg" class="cooker_photo" alt="">
          <p class="cooker_name">Шишова Ольга</p>
          <router-link to="#" class="go_to">Перейти</router-link>
        </div>
        <div class="cooker_item">
          <div class="rating">
            <img src="src/assets/heart.png" class="heart_img" alt="">
            <p class="count">4.9</p>
          </div>
          <img src="src/assets/nacty.jpg" class="cooker_photo" alt="">
          <p class="cooker_name">Лазарева Анастасия</p>
          <router-link to="#" class="go_to">Перейти</router-link>
        </div>
      </div>
    </div>
    <img src="src/assets/right_hand.png" class="right_hand" alt="">
  </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import axios from "axios";
import Home from "@/views/Home.vue";

export default {
  name: "cookers",
  components: {Home, Footer, Header},
  data(){
    return{
      city: "",
      items:[]
    }
  },
  mounted() {
    this.fetchItems();

  },
  methods: {
    fetchItems() {
      axios.get("http://localhost:8000/api/cookers/all").then(response => {
        this.items = response.data;
      });
    },

  }
}
</script>

<style scoped>
.home_title{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 700;
  font-size: 64px;
  line-height: 78px;
  color: #B16FBC;
  margin-top: 100px;
  margin-bottom: 45px;
  text-align: center;
}
.cookers_top{ position: relative;}
.right_hand{position: absolute; right: 0; top: -80px;  width: 390px;}
.left_hand{position: absolute;  left: 0; top: -80px; width: 390px;}
.top_block{display: flex; justify-content: center; align-items: center; text-align: center;}
.top_name{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 500;
  font-size: 36px;
  line-height: 44px;
  color: #B16FBC;
  text-align: center;
  margin-bottom: 60px;
}
.second_place .cook_photo, .third_place .cook_photo{ width: 166px;}
.first_place .cook_photo{  width: 235px;}
.first_place{ margin: 0 100px;}
.cook_photo{border-radius: 50%; border: 3px solid #B16FBC;}
.photo_place{position: relative;  margin-bottom: 20px;}
.place{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 900;
  font-size: 52px;
  line-height: 63px;
  color: #FFFFFF;
  position: absolute;  padding: 1px 18px; border-radius: 50%; right: -20px; bottom: 20px;}
.second_place .place{background-color: #808080;}
.first_place .place{background-color: #FFD700;     font-size: 77px;    padding: 9px 25px;}
.third_place .place{background-color: #CD7F32; right: -10px;}
.cook_name, .cook_city{
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 600;
  font-size: 20px;
  line-height: 24px;
  color: #B16FBC;
  margin-bottom: 10px;
}
.cook_city{
  font-weight: 300;
  font-size: 21px;
  line-height: 26px;
  color: #E232FF;
}
.form_block_item{width: 320px; text-align: left; margin-bottom: 7px;}
.form_block_item label{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 500;
  font-size: 16px;
  line-height: 20px;
  color: #D5A3DD;
  margin-bottom: 6px;
  margin-left: 30px;
}
.form_block_item input, .form_block_item select{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 300;
  font-size: 16px;
  line-height: 20px;
  color: #D5A3DD;
  background: rgba(255, 255, 255, 0.46);
  border: 2px solid #B16FBC;
  border-radius: 25px;
  width: 100%;
  padding: 13px 27px;
}
.search_btn{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 20px;
  color: #FFFFFF;
  padding: 15px 35px;
  margin-top: 15px;
  background: #B16FBC;
  border-radius: 25px;
  border: none;
  margin-left: 20px;
}
.filter_form{display: flex; align-items: center;}
.cookers_top_block{margin-bottom: 100px;}
.cooker_list{margin-top: 60px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;}
.cooker_item{max-width: 350px; position: relative; height: 350px; text-align: center; margin-right: 20px;}
.cooker_item:after{
  content: "";
	display: block;
	width: 100%;
	height: 100%;
	position: absolute;
	bottom: 0;
	left: 0;
	background: transparent;
  background-image: linear-gradient(0deg, #E4C6E9 0%, rgba(228, 198, 233, 0) 104.29%);
}
.cooker_photo{ width: 100%; height: 100%;}
.rating{position: relative; position: absolute; top: 10px; right: 10px; z-index: 1;}
.count{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 600;
  font-size: 25px;
  line-height: 30px;
  text-align: center;
  color: #FFFFFF;
  position: absolute;
  top: 15px;
  left: 24%;
}
.cooker_name{
  position: absolute;
  bottom: 15px;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  text-align: center;
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 600;
  font-size: 25px;
  line-height: 30px;
  text-align: center;
  color: #B16FBC;
  z-index: 1;
}
.go_to{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 700;
  font-size: 19px;
  line-height: 23px;
  color: #FFFFFF;
  background: #B16FBC;
  border-radius: 25px;
  padding: 10px 27px;
  position: absolute;
  bottom: 140px;
  z-index: 1;
  left: 95px;
  display: none;
}
.cooker_item:hover .go_to{display: block;}
</style>