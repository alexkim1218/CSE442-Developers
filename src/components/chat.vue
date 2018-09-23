<template>
<div>

<h1> Messenger </h1>

  <h2>Chat Window</h2>

  <div class="user">
    <img src="../assets/avatar1.png" style="width:100%;">
    <p>Hey man. How are you?</p>
    <span class="text-left">Alex (You)</span>
    <span class="text-right">10:15AM</span>
  </div>

  <div class="user receiver">
    <img src="../assets/avatar2.png" alt="Avatar" class="receiver" style="width:100%;">
    <p>Sorry for late reply. I'm doing great. How about you?</p>
    <span class="text-left-receiver">12:01PM</span>
    <span class="text-right-receiver">Noomar</span>
  </div>

  <div class="user">
    <img src="../assets/avatar1.png" alt="Avatar" style="width:100%;">
    <p>Great! I just started my internship today.</p>
    <span class="text-left">Alex (You)</span>
    <span class="text-right">12:05PM</span>
  </div>

  <div class="user receiver">
    <img src="../assets/avatar2.png" alt="Avatar" class="receiver" style="width:100%;">
    <p>Congratulations! What kind of internship are you doing?</p>
    <span class="text-left-receiver">12:32PM</span>
    <span class="text-right-receiver">Noomar</span>
  </div>

  <div class="user">
    <img src="../assets/avatar1.png" alt="Avatar" style="width:100%;">
    <p>Thanks. It's just an engineering internship.</p>
    <span class="text-left">Alex (You)</span>
    <span class="text-right">12:35PM</span>
  </div>

  <div class="chat" id="form">
    <form class="form-box">
      <h3>Message</h3>
      <textarea placeholder="Type message" name="msg" required></textarea>
      <button type="submit" class="button">Send Message</button>
      <button type="button" class="button">Attach File</button>
      <router-link to="/home" tag="button" class="button">End Conversation</router-link>
    </form>
  </div>
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
.user {
    border: 2px solid #DEDEDE;
    background-color: #F1F1F1;
    border-radius: 5px;
    padding: 10px;
    margin: 10px 0;
}

/* Receiver's message box */
.receiver {
    color: #FFFFFF;
    border-color: #000CCC;
    background-color: #1E90FF;
}

/* Clean the message box */
.user::after {
    content: "";
    clear: both;
    display: table;
}

/* Sender's images on the left */
.user img {
    float: left;
    max-width: 60px;
    width: 100%;
    margin-right: 20px;
    border-radius: 50%;
}

/* Receiver's images on the right */
.user img.receiver {
    float: right;
    margin-left: 20px;
    margin-right:0;
}

/* Sender's name on the left */
.text-left {
    float: left;
    color: #999999;
}

/* Sender's message time on the right */
.text-right {
    float: right;
    color: #AAAAAA;
}

/* Receiver's name time on the left */
.text-left-receiver {
    float: left;
    color: #FFFFFF;
}

/* Receiver's name on the right */
.text-right-receiver {
    float: right;
    color: #FFFFFF;
}

/* Message input box */
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

/* Send & Attach File button layout */
.form-box .button {
    background-color: #008000;
    color: #FFFFFF;
    padding: 16px 20px;
    border: 2px solid #DEDEDE;
    border-radius: 5px;
    cursor: pointer;
    width: 32.9%;
    margin-bottom:10px;
    opacity: 0.8;
}

/* End Conversation button layout */
.form-box .end {
    background-color: #FF0000;
    color: #FFFFFF;
    padding: 16px 20px;
    border: 2px solid #DEDEDE;
    border-radius: 5px;
    cursor: pointer;
    width: 32.9%;
    margin-bottom:10px;
    opacity: 0.8;
}
</style>
