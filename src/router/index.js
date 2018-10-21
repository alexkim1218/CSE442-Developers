import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import homepage from '@/components/homepage'
import chat from '@/components/chat'
import edit from '@/components/edit'
import upload from '@/components/upload'
import signup from '@/components/signup'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/',
      name: 'signup',
      component: signup
    },
    {
      path: '/home',
      name: 'homepage',
      component: homepage
    },
    {
      path: '/upload',
      name: 'upload',
      component: upload
    },
    {
      path: '/edit',
      name: 'edit',
      component: edit
    },
    {
      path: '/chat',
      name: 'chat',
      component: chat
    }
  ]
})
