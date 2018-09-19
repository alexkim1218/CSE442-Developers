<template>
  <div class="hello">
  Welcome to Developers

<html lang = "en">
  <head>
    <title>Login</title>
    <meta charset = "UTF-8" />
  </head>
  <body>
    <h1>Hi!</h1>
    <form>
      <fieldset>
        <legend>User Login</legend>
        <p>
          <label>User ID</label>
          <input type = "text"
                 id = "myText" />
        </p>
        <p>
          <label>Password</label>
          <input>
        </p>
        <button onclick="location.href='http://www.cse442developers.com'" type="button">
     login</button>
      </fieldset>
    </form>
  </body>
</html>

  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
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
