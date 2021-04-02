<template>
  <div>
    <div id="login-wrapper">
      <div>
        <label for="username">Username</label>
        <input ref="username" id="username" type="text" name="username">
      </div>

      <div>
        <label for="password">Password</label>
        <input ref="password" id="password" type="text" name="password">
      </div>

      <button @click="login">Login</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  methods: {
    login () {
      fetch('http://localhost/api/login/',
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': this.getCsrfToken()
          },
          body: JSON.stringify({
            username: this.$refs.username.value,
            password: this.$refs.password.value
          })
        })
    },
    getCsrfToken () {
      console.log(document.cookie)
      const csrfCookieName = 'csrftoken'
      const value = `; ${document.cookie}`
      const parts = value.split(`; ${csrfCookieName}=`)
      if (parts.length === 2) return parts.pop().split(';').shift()
    }
  },
  mounted () {
    fetch('http://localhost/api/set-csrf/')
      .then(response => {
        console.log(response)
        this.getCsrfToken()
      })
  }
}
</script>

<style lang="scss">
#login-wrapper {
  margin-inline-start: auto;
  margin-inline-end: auto;
  max-width: 250px;
}
</style>
