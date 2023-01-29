import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import NoteCards from './pages/notes/NotesCards.vue'
import BookResell from './pages/bookresell/BookListings.vue'
import FilterNotes from './globalcomponents/FilterNotes.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'

loadFonts()

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/notes', component: NoteCards },
    { path: '/bookresell', component: BookResell}
  ]
});


createApp(App)
  .use(vuetify)
  .use(router)
  .mount('#app')
  .component('note-cards', NoteCards)
  .component('filter-notes', FilterNotes)
