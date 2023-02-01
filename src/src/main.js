import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import NoteCards from './pages/notes/NotesCards.vue'
import BookResell from './pages/bookresell/BookListings.vue'
import FilterMenu from './globalcomponents/BookListingsFilter.vue'
import TestPage from './pages/tester/testPage.vue'
import DashBoard from './pages/dashboard/HomeView.vue'
import DisabilityPage from './pages/DRC/HelloWorld.vue'
import AboutPage from './pages/about/AboutView.vue'
import LoginPage from './pages/login/WelcomeView.vue'
import NavBar from './globalcomponents/NavBar.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'

loadFonts()

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/notes', component: NoteCards },
    { path: '/bookresell', component: BookResell},
    { path: '/testpage', component: TestPage},
    { path: '/dashboard', component: DashBoard },
    { path: '/DRC', component: DisabilityPage },
    { path: '/aboutus', component:  AboutPage },
    { path: '/', component: LoginPage }
  ]
});


createApp(App)
  .use(vuetify)
  .use(router)
  .component('note-cards', NoteCards)
  .component('filter-menu', FilterMenu)
  .component('nav-bar', NavBar)
  .mount('#app')
