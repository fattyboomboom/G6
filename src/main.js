import '@babel/polyfill'
import 'mutationobserver-shim'
import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import { createRouter, createWebHistory } from 'vue-router'

loadFonts()

import BookResellView from './views/BookResellView.vue'
import ProfileView from './views/ProfileView.vue'
import HomeView from './views/HomeView.vue'
import AboutViewVue from './views/AboutView.vue'
import WelcomeView from './views/WelcomeView.vue'
import NotesView from './views/NotesCards.vue'
import FilterMenu from './globalcomponents/ListingsFilter.vue'
import NavBarVue from './globalcomponents/NavBar.vue'
import ListingsFilter from './globalcomponents/ListingsFilter.vue'
import ExplorePage from './views/ExplorePage.vue'

import axios from "axios";

export default axios.create({
  baseURL: "http://localhost:3000",
  timeout: 1000
});


const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/bookresell', component:BookResellView },
    { path: '/home', component: HomeView },
    { path: '/about', component: AboutViewVue },
    { path: '/', component: WelcomeView },
    { path: '/notes', component: NotesView },
    { path: '/profile', component: ProfileView},
    { path: '/explore', component: ExplorePage}
  ]

});

createApp(App)
  .use(router)
  .use(vuetify)
  .component('filter-menu', FilterMenu)
  .component('nav-bar', NavBarVue) 
  .component('listings-filter', ListingsFilter)
  .mount('#app')