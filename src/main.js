import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import NoteCards from './pages/notes/NotesCards.vue'
import BookResell from './pages/bookresell/BookListings.vue'
import FilterMenu from './globalcomponents/BookListingsFilter.vue'
import TestPage from './pages/tester/testPage.vue'
import NavBar from './globalcomponents/NavBar.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'

loadFonts()

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/notes', component: NoteCards },
    { path: '/bookresell', component: BookResell},
    { path: '/testpage', component: TestPage}
  ]
});


createApp(App)
  .use(vuetify)
  .use(router)
  .component('note-cards', NoteCards)
  .component('filter-menu', FilterMenu)
  .component('nav-bar', NavBar)
  .mount('#app')
