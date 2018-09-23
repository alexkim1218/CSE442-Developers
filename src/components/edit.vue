<template>
  <div class="hello">
Edit Profile
  <h1>General Information</h1>
    <form>
        <p>
        <label>First Name</label>
          <input type = "text"
                  v-model="username"
                 id = "username" />
        </p>
        <p>
          <label>Last Name</label>
          <input type = "text" />
        </p>
        <p>
          <label>Email ID</label>
            <input type = "text" />
        </p>
        <p>
          <label>Date of Birth</label>
          <input type = "text" />
        </p>
        <p>
          <label>Education</label>
            <input type = "text" />
        </p>
        <router-link to="/home" tag="button" class="button">Save</router-link>
        <router-link to="/home" tag="button" class="button">Cancel</router-link>
    </form>

  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      username: '',
      password: ''
    }
  },
  methods: {
    authenticate () {
      if (this.username === 'user' && this.password === 'pwd') {
        this.$router.push({ path: '/home' })
      } else { alert('Wrong Password') }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,h2,p {
  font-weight: normal;
  }
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
