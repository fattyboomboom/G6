import { createRouter, createWebHistory } from 'vue-router'
//import HomeView from '@/views/HomeView.vue'


const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: DashView
  },
  {
    path: '/notes',
    name: 'notes',
    component: NotesView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/bookresell',
    name: 'bookresell',
    component: ResellView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router