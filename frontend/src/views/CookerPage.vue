<template>
  <Header/>
    <div class="container cooker_page">
      <div class="cooker_info">
        <div class="cooker_ava">
          <div class="rating">
            <img src="src/assets/heart.png" class="heart_img" alt="">
            <p class="count">5.0</p>
          </div>
          <img src="src/assets/polina.jpg" class="cooker_photo" alt="">
        </div>
        <div class="cooker_info_text">
          <p class="cooker_name">Филимонова Полина</p>
          <p class="cooker_location">Россия, Москва</p>
          <p class="cooker_descript">Я - Полина Филимонова, Топ-кондитер и основатель самой большой кондитерской онлайн
            школы в России и СНГ "Pauline School", которую выбрали уже более 100 000 учеников по всему миру! Когда-то,
            как и все, я начала с простых десертов на своей кухне, а сейчас создаю настоящие кондитерские шедевры.
            И знаю, это получится у каждого.</p>
        </div>
      </div>
      <div class="tabs_filter">
        <div class="nav_tabs">
          <div class="nav_tabs_item nil" @click="setActive('tab-1')" :class="{ 'active active1' : isActive('tab-1'), 'pl' : isActive('tab-4'), 'pl2' : isActive('tab-2'), 'pl3' : isActive('tab-3')}">Товары</div>
          <div class="nav_tabs_item" @click="setActive('tab-2')" :class="{ 'active active2' : isActive('tab-2')}">Публикации</div>
          <div class="nav_tabs_item" @click="setActive('tab-3')" :class="{ 'active active3' : isActive('tab-3')}">Отзывы</div>
          <div class="nav_tabs_item nir" @click="setActive('tab-4')" :class="{ 'active active4' : isActive('tab-4'), 'pr' : isActive('tab-1'), 'pr2' : isActive('tab-2'), 'pr3' : isActive('tab-3')}">Рецепты</div>
      </div>
        <div class="tabs_content">
          <div class="tab tab1" v-show="isActive('tab-1')">
            <div class="cooker_filter">
              <form @submit="" class="filter_form">
                <div class="form_block_item">
                      <label for="category">Категория товара</label>
                      <select v-model="category" type="text" id="category"/>
                </div>
                <div class="form_block_item">
                      <label for="type">Тип товара</label>
                      <select v-model="type" type="text" id="type"/>
                </div>
                <button class="search_btn">Найти</button>
              </form>
            </div>
            <div class="tab_list">
              <div class="tab_list_item">
                <img src="src/assets/prod1.png" class="prod_img" alt="">
                <router-link to="product_page" class="go_to">Перейти</router-link>
              </div>
              <div class="tab_list_item">
                <img src="src/assets/prod2.png" class="prod_img" alt="">
                <router-link to="#" class="go_to">Перейти</router-link>
              </div>
              <div class="tab_list_item">
                <img src="src/assets/prod3.png" class="prod_img" alt="">
                <router-link to="#" class="go_to">Перейти</router-link>
              </div>
              <div class="tab_list_item">
                <img src="src/assets/prod4.png" class="prod_img" alt="">
                <router-link to="#" class="go_to">Перейти</router-link>
              </div>
              <div class="tab_list_item">
                <img src="src/assets/prod5.png" class="prod_img" alt="">
                <router-link to="#" class="go_to">Перейти</router-link>
              </div>
              <div class="tab_list_item">
                <img src="src/assets/prod6.png" class="prod_img" alt="">
                <router-link to="#" class="go_to">Перейти</router-link>
              </div>
            </div>
          </div>
          <div class="tab tab1" v-show="isActive('tab-2')">
            <div class="tab_list">
              <div class="tab_list_item">
                <img src="src/assets/post1.png" class="prod_img" alt="">
                <router-link to="#" class="go_to">Перейти</router-link>
              </div>
              <div class="tab_list_item">
                <img src="src/assets/post2.png" class="prod_img" alt="">
                <router-link to="#" class="go_to">Перейти</router-link>
              </div>
              <div class="tab_list_item">
                <img src="src/assets/post3.png" class="prod_img" alt="">
                <router-link to="#" class="go_to">Перейти</router-link>
              </div>
              <div class="tab_list_item">
                <img src="src/assets/post4.png" class="prod_img" alt="">
                <router-link to="#" class="go_to">Перейти</router-link>
              </div>
              <div class="tab_list_item">
                <img src="src/assets/post5.png" class="prod_img" alt="">
                <router-link to="#" class="go_to">Перейти</router-link>
              </div>
              <div class="tab_list_item">
                <img src="src/assets/post6.png" class="prod_img" alt="">
                <router-link to="#" class="go_to">Перейти</router-link>
              </div>
            </div>
          </div>
          <div class="tab tab1" v-show="isActive('tab-3')">
            <div class="feedback_list">
              <div class="feedback_list_item" v-for="feed in feedbacks">
                <div class="feedback_header">
                  <div class="feedback_person">
                    <img :src="feed.avatar" class="feedback_img" alt="">
                    <p class="feedback_name">{{feed.author}}</p>
                  </div>
                  <p class="feedback_rating">Оценка: {{feed.rating}}</p>
                  <p class="feedback_date">{{feed.date}}</p>
                </div>
                <p class="feedback_text">{{feed.text}}</p>
              </div>
            </div>
          </div>
          <div class="tab tab1" v-show="isActive('tab-4')">
            <div class="cooker_filter">
              <form @submit="" class="filter_form">
                <div class="form_block_item">
                      <label for="category">Категория товара</label>
                      <select v-model="category" type="text" id="category"/>
                </div>
                <div class="form_block_item">
                      <label for="type">Тип товара</label>
                      <select v-model="type" type="text" id="type"/>
                </div>
                <button class="search_btn">Найти</button>
              </form>
            </div>
            <div class="tab_list">
              <div class="tab_list_item" v-for="recipe in recipes" :key="recipe.id">
                <img :src="recipe.image" class="prod_img" alt="">
                <router-link to="#" class="go_to">Перейти</router-link>
	            </div>
            </div>
          </div>
      </div>
    </div>
    </div>
  <Footer/>
</template>

<script>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";


export default {
  name: "CookerPage",
  components: {Footer, Header},
  data: () => ({
    activeTab: 'tab-1',
    type: "",
    category: "",
    recipes: [
      {
        id:1,
        image: "src/assets/rec1.png"},
      {
        id:2,
        image: "src/assets/rec2.png"},
      {
        id:3,
        image: "src/assets/rec3.png"},
      {
        id:4,
        image: "src/assets/rec4.png"},
      {
        id:5,
        image: "src/assets/rec5.png"},
      {
        id:6,
        image: "src/assets/rec6.png"},
    ],
    feedbacks:[
        {
        author: 'Саева Кристина',
        rating: '5',
        avatar: 'src/assets/author1.jpg',
        date: '01.05.2023',
        text: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus.'
      },
        {
        author: 'Красилова Анна',
        rating: '5',
        avatar: 'src/assets/author2.jpg',
        date: '30.04.2023',
        text: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus.'
      },
        {
        author: 'Кузьминых Ольга',
        rating: '5',
        avatar: 'src/assets/author3.jpg',
        date: '01.05.2023',
        text: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus.'
      },
        {
        author: 'Лавреньтева Инна',
        rating: '5',
        avatar: 'src/assets/author4.jpg',
        date: '28.04.2023',
        text: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus.'
      },
        {
        author: 'Алехина Вероника',
        rating: '4',
        avatar: 'src/assets/author5.jpg',
        date: '02.05.2023',
        text: 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus.'
      },
    ]
  }),
  methods : {
    setActive(tab) {
      this.activeTab = tab
    },
    isActive(tab) {
      return this.activeTab === tab;
    },
  }
}
</script>

<style scoped>
.cooker_info{display: flex; justify-content: space-between; align-items: center;}
.cooker_ava{position: relative;  margin-right: 100px;}
.cooker_photo{border: 8px solid #8AABCE;border-radius: 50%; max-width: 400px;}
.rating{position: relative; position: absolute; top: 10px; right: 10px; z-index: 1;}
.heart_img{width: 100px;}
.count{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 600;
  font-size: 35px;
  line-height: 30px;
  text-align: center;
  color: #FFFFFF;
  position: absolute;
  top: 25px;
  left: 24%;
}
.cooker_name{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 600;
  font-size: 64px;
  line-height: 78px;
  color: #8AABCE;
  margin-bottom: 10px;
}
.cooker_location{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 300;
  font-size: 33px;
  line-height: 40px;
  color: #8AABCE;
  margin-bottom: 40px;
}
.cooker_descript{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 500;
  font-size: 20px;
  line-height: 44px;
  color: #8AABCE;
}
.tabs_filter{margin-top: 30px;}
.nav_tabs{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 400;
  font-size: 25px;
  line-height: 37px;
  text-align: center;
  color: #8AABCE;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 2px solid #8AABCE;
  border-radius: 25px 25px 0px 0px;
}
.nav_tabs_item{border-left: 1px solid #8AABCE; border-right: 1px solid #8AABCE; padding: 22px 98px; cursor: pointer;}
.active{color: #FFFFFF;}
.active1{
  background: #8AABCE;
  border-radius: 23px 0px 0px 0px;
  padding: 22px 81px;
}
.active2, .active3{
  background: #8AABCE;
  border-radius: 0px;
  padding: 22px 81px;
}
.active4{
  background: #8AABCE;
  border-radius: 0px 23px 0px 0px;
  padding: 22px 81px;
}
.nil{border-left: none;}
.nir{border-right: none;}
.filter_form, .tab_list{display: flex; align-items: center; justify-content: space-between; margin-top: 30px;}
.form_block_item{width: 450px; text-align: left; margin-bottom: 7px;}
.form_block_item label{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 500;
  font-size: 16px;
  line-height: 20px;
  color: #CBD5DF;
  margin-bottom: 6px;
  margin-left: 30px;
}
.form_block_item select{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 300;
  font-size: 16px;
  line-height: 20px;
  color: #8AABCE;
  background: rgba(255, 255, 255, 0.46);
  border: 2px solid #8AABCE;
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
  padding: 16px 85px;
  margin-top: 15px;
  background: #8AABCE;
  border-radius: 25px;
  border: none;
  margin-left: 20px;
}
.tab_list_item{max-width: 400px; max-height: 400px; position: relative; cursor: pointer; margin-bottom: 20px;}
.tab_list{flex-wrap: wrap;}
.prod_img{width: 100%; height: 100%;}
.go_to{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 700;
  font-size: 19px;
  line-height: 23px;
  color: #FFFFFF;
  background: #3290FF;
  border-radius: 25px;
  padding: 10px 27px;
  position: absolute;
  bottom: 45%;
  z-index: 1;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  text-align: center;
  max-width: 250px;
  display: none;
}
.tab_list_item:after{
  content: "";
	display: none;
	width: 100%;
	height: 100%;
	position: absolute;
	top: 0;
	left: 0;
  background: rgba(57, 129, 215, 0.66);
}
.tab_list_item:hover .go_to{display: block;}
.tab_list_item:hover:after{display: block;}
.feedback_list{margin-top: 40px;}
.feedback_list_item{  padding: 32px 42px;  background: #F2F8FF; border-radius: 25px; margin-bottom: 27px;}
.feedback_header{display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;}
.feedback_person{display: flex; align-items: center;}
.feedback_img{ width: 76px; border-radius: 50%; border: 3px solid #3981D7; margin-right: 18px;}
.feedback_name{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 700;
  font-size: 20px;
  line-height: 24px;
  color: #3981D7;
  max-width: 100px;
}
.feedback_rating{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 500;
  font-size: 20px;
  line-height: 24px;
  color: #F3AB6F;
}
.feedback_date{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 17px;
  color: #808080;
}
.feedback_text{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 300;
  font-size: 17px;
  line-height: 27px;
  color: #808080;
}
</style>