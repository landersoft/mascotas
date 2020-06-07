import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ListGato from '@/components/Gato/ListGato'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/gatos',
      name: 'ListGato',
      component: ListGato
    },

  ],
  mode: 'history'
})
