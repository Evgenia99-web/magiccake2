<template>
  <Header/>
  <div class="container product_block">
    <img src="src/assets/prod6.png" class="product_img" alt="">
    <div class="product_info_block">
      <p class="product_title">Торт “Нежность облаков”</p>
      <p class="product_cat">Детский, День рождения</p>
      <p class="product_text">
        Минимальный заказ торта - 2 кг. Работа по индивидуальному дизайну.
        Возможно поменять количество ярусов и внешний вид. Любые надписи, изменения цветов и
        прочие мелкие правки - всё включено в стоимость. Вес торта рассчитывается 150 - 300 гр. на одного человека.
      </p>
      <p class="add_info">Для того, чтобы рассчитать примерную стоимость, выберете начинку и укажите нужный вес / количество.</p>
    </div>
  </div>
  <FillingSlider/>
  <Footer/>
</template>

<script>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import FillingSlider from "@/components/FillingSlider.vue";

export default {
  name: "ProductPage",
  components: {FillingSlider, Footer, Header}
}
</script>

<style scoped>
.product_block{display: flex; align-items: center; justify-content: space-between; margin-bottom: 38px;}
.product_img{border: 8px solid #8AABCE;border-radius: 50%; max-width: 400px; margin-right: 50px;}
.product_title{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 600;
  font-size: 50px;
  line-height: 78px;
  color: #8AABCE;
  margin-bottom: 11px;
}
.product_cat{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 300;
  font-size: 28px;
  line-height: 40px;
  color: #8AABCE;
  margin-bottom: 35px;
}
.product_text{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 500;
  font-size: 20px;
  line-height: 44px;
  color: #8AABCE;
  margin-bottom: 18px;
}
.add_info{
  font-family: 'Montserrat',serif;
  font-style: normal;
  font-weight: 300;
  font-size: 18px;
  line-height: 35px;
  color: #8AABCE;
}
</style>