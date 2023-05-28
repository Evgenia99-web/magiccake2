<template>
  <p class="step_name container">Выберете начинку:</p>
  <div class="prod_tabs">
    <div class="nav_tabs">
    <swiper
      :modules="modules"
        :slides-per-view="6"
        :space-between="25"
        :loop="true"
        :navigation="{
          prevEl: prev,
          nextEl: next,
        }">
        <swiper-slide v-for="fil in swiperTextFilling" :key="fil.id">
          <div class="nav_tabs_item" @click="setActive(fil.id, fil.price, fil.name)" :class="{ 'active active1' : isActive(fil.id)}">
            <img :src="fil.image" class="fil_img" alt="">
            <p class="fil_name">{{fil.name}}</p>
          </div>
        </swiper-slide>
    </swiper>
    </div>
    <div ref="prev" class="swiper-button-prev"><img src="src/assets/Arrow_left.png" class="arrow_left" alt=""></div>
    <div ref="next" class="swiper-button-next"><img src="src/assets/Arrow_right.png" class="arrow_right" alt=""></div>
    <div class="tabs_content">
        <div class="tab tab1" v-for="fil in swiperTextFilling" :key="fil.id" v-show="isActive(fil.id)">
            <p class="fil_descript">{{fil.text}}</p>
        </div>
      </div>
  </div>
  <div class="container summary_block">
    <div class="weight_block">
      <p class="step_name">Укажите нужный вес торта:</p>
      <form class="form_weight">
        <input v-model="weight" id="weight" type="number" step="0.100" min="2" placeholder="Введите вес торта в кг">
        <label for="weight">Вы можете указывать вес торта с шагом в 0.2 кг.<br> Минимальный вес торта - 2 кг!</label>
      </form>
    </div>
    <div class="price_block">
      <p class="step_name">Примерная стоимость торта за {{weight}} кг:</p>
      <div class="price_info_block">
        <p class="product_info">
          Торт “Нежность облаков” <br>
          Начинка: {{filling}}
        </p>
        <p class="product_sum">{{sum}} Р</p>
      </div>
      <button class="form_btn">Добавить в корзину</button>
    </div>
  </div>
</template>

<script>
import {Swiper, SwiperSlide} from "swiper/vue";
import SwiperCore, {Autoplay, Navigation} from "swiper";
import 'swiper/swiper-bundle.css'
import 'swiper/swiper.css'
import {ref} from "vue";

SwiperCore.use([Navigation]);
export default {
  name: "FillingSlider",
  components: { Swiper, SwiperSlide},
  data(){
    return{
      activeTab: 'tab-1',
      weight: '',
      price: '',
      filling: '',
    }
  },
  setup(){
    const prev = ref(null);
    const next = ref(null);
    const swiperTextFilling = ref([
      {
        id: 'tab-1',
        price: 1850,
        name: 'Сникерс',
        image: 'src/assets/fil1.png',
        text: 'Насыщенные шоколадные коржи, чередующиеся нежными взбитыми сливками и шоколадным ганашем, создают неповторимый вкус. Наличие арахиса и соленной карамели, отличающаяся несовместимым вкусом сладкого и соленного, образует незабываемый изысканный вкус.'
      },
      {
        id: 'tab-2',
        price: 1650,
        name: 'Банан - шоколад',
        image: 'src/assets/fil2.jpg',
        text: 'Насыщенные шоколадные коржи, чередующиеся нежными взбитыми сливками и кусочками банана, создают неповторимый вкус.'
      },
      {
        id: 'tab-3',
        price: 1650,
        name: 'Черный лес',
        image: 'src/assets/fil3.jpg',
        text: 'Воздушный шоколадный бисквит с нежным сметанным кремом и свежих ягод вишни украсит любой праздничный стол, и придется по вкусу каждому.'
      },
      {
        id: 'tab-4',
        price: 1900,
        name: 'Фисташка - малина',
        image: 'src/assets/fil4.jpg',
        text: 'В основе — фисташковый белковый бисквит, воздушный, легкий, тающий во рту — с добавлением натуральной пасты из фисташек. Растертые орешки лучше «доносят» вкус. Его дополняет фисташковый творожный крем. Кроме того, что эти орешки вкусны, они очень полезны.'
      },
      {
        id: 'tab-5',
        price: 1650,
        name: 'Манго - косос',
        image: 'src/assets/fil5.png',
        text: 'Нежнейший бисквит, смешанный с фруктами и кокосовым кремом, делает этот десерт изысканным. Он в меру сладкий, а сочетание экзотического манго и кокоса дарит легкость вкуса. '
      },
      {
        id: 'tab-6',
        price: 1650,
        name: 'Банан - карамень',
        image: 'src/assets/fil6.jpg',
        text: 'Влажные, сочные ванильные коржи, пропитанные сливочным сиропом + свежие бананы политые домашней карамелью в нежных объятиях кремчиза. Это просто банановый взрыв!'
      },
      {
        id: 'tab-7',
        price: 1650,
        name: 'Шоколад - апельсин',
        image: 'src/assets/fil7.png',
        text: 'Коржи брауни на темном бельгийском шоколад, взбитый шоколадный ганаш, сочная серединка из свежей мякоти апельсина, проваренной с веточкой розмарина для пикантности.'
      },
      {
        id: 'tab-8',
        price: 1650,
        name: 'Малиновый бриз',
        image: 'src/assets/fil8.png',
        text: 'Невероятно легкий летний тортик с ягодной кислинкой. В нем сочетается сладость бисквита, нежность сливочного крема и кислинка малины.'
      },
    ]);
    return {modules: [Navigation], swiperTextFilling, prev, next,}
  },
  methods : {
    setActive(tab, price, filling) {
      this.activeTab = tab
      this.price = price
      this.filling = filling
    },
    isActive(tab) {
      return this.activeTab === tab;
    }
  },
  computed:{
    sum : function (){
      return Math.round(this.weight * this.price)
    }
  }
}
</script>

<style scoped>
.form_weight{ width: 450px;}
.form_weight input{
  width: 100%;
  font-weight: 300;
  font-size: 16px;
  line-height: 25px;
  color: #7394B8;
  border: 3px solid #7394B8;
  border-radius: 35px;
  padding: 7px 24px;
  margin-bottom: 6px;
}
.form_weight label{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 300;
  font-size: 14px;
  line-height: 23px;
  color: #7394B8;
}
.form_btn{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 400;
  font-size: 24px;
  line-height: 44px;
  color: #FFFFFF;
  border: none;
  background: #8AABCE;
  border-radius: 25px;
  padding: 10px 100px;
  margin-top: 28px;
  cursor: pointer;
}
.step_name{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 700;
  font-size: 30px;
  line-height: 44px;
  color: #7394B8;
  margin-bottom: 30px;
}
.summary_block{display: flex;align-items: start; justify-content: space-between;}
.prod_tabs{margin: 30px 120px;}
.nav_tabs_item{cursor: pointer;}
.fil_img{width: 190px; border-radius: 25px; height: 90px;}
.fil_name{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 400;
  font-size: 17px;
  line-height: 30px;
  text-align: center;
  color: #5280B1;
}
.active .fil_img{border: 3px solid #5280B1;}
.active .fil_name{font-weight: 600;}
.nav_tabs{margin-bottom: 35px;}
.tab{background-color: rgba(138, 171, 206, 0.21); padding: 15px 30px;}
.fil_descript{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 500;
  font-size: 16px;
  line-height: 36px;
  color: #5280B1;
}
.swiper-button-prev:after{content: '';}
.swiper-button-next:after{content: '';}
.swiper-button-next, .swiper-button-prev{top: 45px;}
.swiper-button-prev{margin-left: -65px;}
.swiper-button-next{margin-right: -65px;}
.price_block{text-align: right;}
.price_info_block{ display: flex; align-items: center; justify-content: space-between;}
.product_info{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 500;
  font-size: 22px;
  line-height: 44px;
  color: #7394B8;
}
.product_sum{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 600;
  font-size: 32px;
  line-height: 44px;
  text-align: right;
  color: #7394B8;
}
</style>