import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import About from "@/views/About.vue";
import Registration from "@/views/Registration.vue";
import Auth from "@/views/Auth.vue";
import Cookers from "@/views/Cookers.vue";
import CookerPage from "@/views/CookerPage.vue";
import ProductPage from "@/views/ProductPage.vue";
import Cart from "@/views/Cart.vue";
import Profile from "@/views/userCab/Profile.vue";
import store from "@/store";

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
        {
        path: '/about',
        name: 'About',
        component: About
    },
    {
        path: '/auth',
        name: 'Auth',
        component: Auth
    },
     {
        path: '/registration',
        name: 'Registration',
        component: Registration
    },
     {
        path: '/cookers',
        name: 'Cookers',
        component: Cookers
    },
     {
        path: '/cooker_page',
        name: 'CookerPage',
        component: CookerPage
    },
    {
        path: '/product_page',
        name: 'ProductPage',
        component: ProductPage
    },
    {
        path: '/cart',
        name: 'Cart',
        component: Cart
    },
    {
        path: '/profile',
        name: 'Profile',
        component: Profile,
        beforeEnter (to, from, next) {
            if (store.state.idToken) {
              next()
            }
            else {
              next('auth')
            }
        }
    },

]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;