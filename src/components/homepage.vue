<template>
<div>
<img class="photo" src="../assets/avatar1.png"/>
<h1> Noomar </h1>
  <p class="font">Friends          Image</p>
  <p class="number">42                0</p>
<router-link to="/chat" tag="button" class="button">Message</router-link>
<router-link to="/upload" tag="button" class="button">Upload</router-link>
<router-link to="/edit" tag="button" class="button">Edit</router-link>
<router-link to="/" tag="button" class="button">Sing Out</router-link>
<form class="form-box">
   <h3>Story</h3>
   <textarea placeholder="Whats on your mind" name="msg" required></textarea>
   <button type="submit" class="button">Share</button>
   <router-link to="/home" tag="button" class="button">Cancel</router-link>
  </form>
  </div>
</template>

<script>
export default {
  name: 'homepage',
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
.photo {
  width: 200px;
  height: 200px;
  margin-top: 20px;
  border-radius: 100px;
  border: 4px solid #fff;
}
.left
{
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
.font
{
margin-top: -15px;
font-size: 10pt;
color: #42b983;
}
.number
{
padding: 0px;
font-size: 14pt;
font-weight: bold;
font-family: 'Montserrat', sans-serif;
color: #aaa;
}
.form-box textarea {
    width: 96%;
    padding: 15px;
    margin: 5px 0 22px 0;
    border: 2px solid #DEDEDE;
    border-radius: 5px;
    background: #F1F1F1;
    resize: none;
    min-height: 50px;
    font-size: 11pt;
}
.button {
    background-color: #008000;
    color: #FFFFFF;
    padding: 16px 20px;
    border: 2px solid #DEDEDE;
    border-radius: 5px;
    cursor: pointer;
    width: 10%;
    margin-bottom:10px;
    opacity: 0.8;
}
</style>
