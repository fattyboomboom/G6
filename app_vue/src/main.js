import '@babel/polyfill'
import 'mutationobserver-shim'
import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
//import axios from 'axios'
import App from './App.vue'
import NoteCards from './pages/notes/NotesCards.vue'
import BookResell from './pages/bookresell/BookListings.vue'
import FilterMenu from './globalcomponents/BookListingsFilter.vue'
import TestPage from './pages/tester/testPage.vue'
import DashBoard from './pages/dashboard/HomeView.vue'
import DisabilityPage from './pages/DRC/HelloWorld.vue'
import ExplorePage from './pages/explore/ExplorePage.vue'
import AboutPage from './pages/about/AboutView.vue'
import LoginPage from './pages/login/WelcomeView.vue'
import NavBar from './globalcomponents/NavBar.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import SuperUserDash from './pages/superuser/SuperUserDash.vue'


loadFonts()

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/notes', component: NoteCards,meta: { requiresAuth: true  }},
    { path: '/bookresell', component: BookResell, meta: { requiresAuth: true}},
    { path: '/testpage', component: TestPage, meta: { requiresAuth: true}},
    { path: '/dashboard', component: DashBoard, meta: { requiresAuth: true }},
    { path: '/DRC', component: DisabilityPage, meta: { requiresAuth: true }},
    { path: '/about', component:  AboutPage },
    { path: '/explore', component: ExplorePage, meta: { requiresAuth: true }},
    { path: '/', component: LoginPage},
    { path: '/superuser', component: SuperUserDash, meta: { requiresAuth: true}}
    //{ path: '/', component: TestLPM}
  ]
});

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')

  if (to.matched.some(record => record.meta.requiresAuth) && !token) {
    next('/')
  } else {
    next()
  }
})

export default router

createApp(App)
  .use(vuetify)
  .use(router)
  .component('note-cards', NoteCards)
  .component('filter-menu', FilterMenu)
  .component('nav-bar', NavBar)
  .mount('#app')

