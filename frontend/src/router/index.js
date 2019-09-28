import Vue from 'vue'
import Router from 'vue-router'
import Preferences from '@/components/Preferences'
import Start from '@/components/Start'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Start',
      component: Start,
      props: true
    },
    {
      path: '/preferences',
      name: 'Preferences',
      component: Preferences,
      props: true
    }
  ]
})
