<template>
  <div class="hello">
  <form class="form-box">
     <h3>Upload</h3>
     <textarea placeholder="Write a Caption" name="msg" required></textarea>
     <button type="submit" class="button">Browse</button>
     <router-link to="/home" tag="button" class="button">Save</router-link>
     <router-link to="/home" tag="button" class="button">Cancel</router-link>
   </form>
   </div>
  </template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
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
