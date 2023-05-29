import { createApp } from 'vue'
import App from './App.vue'
import './assets/main.css'
import axios from 'axios';
import router from './router';
import store from './store';

axios.defaults.baseURL = 'http://127.0.0.1:8000/api';

const token = localStorage.getItem('token');
if (token) {
  axios.defaults.headers.common.Authorization = `Token ${token}`;
  store.commit('setToken', token);
}
store.dispatch("AutoLogin");
createApp(App).use(router).use(store).mount('#app');

