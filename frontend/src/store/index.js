import { createStore } from 'vuex';
import axios from 'axios';
import router from "@/router";

export default createStore({
  state: {
    idToken: null,
    userId: null,
    user: null
  },
  mutations: {
    authUser (state, userData) {
      state.idToken = userData.token
      state.userId = userData.userId
    },
    clearAuth (state) {
    state.idToken = null
    state.userId = null
  }
  },
  actions: {
    signup ({commit}, authData) {
    axios.post('/register/', {
      username: authData.username,
      email: authData.email,
      first_name: authData.first_name,
      last_name: authData.last_name,
      password: authData.password,
      is_cooker:authData.is_cooker,
      is_customer:authData.is_customer,
    })
    .then(res => {
      console.log(res)
      commit('authUser', {
        token: res.data.idToken,
        userId: res.data.localId
      })
      localStorage.setItem('token', res.data.idToken)
      localStorage.setItem('userId', res.data.localId)
      router.push("/")
    })
    .catch(error => console.log(error))
  },
    login ({commit}, authData) {
    axios.post('/login/', {
      username: authData.username,
      password: authData.password,
    })
    .then(res => {
      console.log(res)
      commit('authUser', {
        token: res.data.idToken,
        userId: res.data.localId
      })
      localStorage.setItem('token', res.data.idToken)
      localStorage.setItem('userId', res.data.localId)
      router.push("/dashboard")
    })
    .catch(error => console.log(error))
    },
    AutoLogin ({commit}) {
      const token = localStorage.getItem('token')
      if (!token) {
        return
      }
      const userId = localStorage.getItem('userId')
      commit('authUser', {
        idToken: token,
        userId: userId
      })
    },
  },
  getters: {
    user (state) {
      return state.user
    },
    ifAuthenticated (state) {
      return state.idToken !== null
    }
  }
})
