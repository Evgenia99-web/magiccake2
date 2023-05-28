<template>
    <h1>Profile</h1>
    <p v-if="user">
      Welcome back, {{ username }} {{ email }}
    </p>
  <div>
    <button @click="onLogout">Logout</button>
  </div>
</template>

<script>

export default {
  name: "Profile",
  data() {
    return {
      username: '',
      email: '',
    };
  },
  methods: {
      onLogout() {
        this.$store.dispatch('logout')
      }
    }
}
</script>

<style scoped>

</style>