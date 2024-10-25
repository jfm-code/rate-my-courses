import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from './components/LandingPage.vue'
import ReviewPage from './components/ReviewPage.vue'

// Define the routes for your components
const routes = [
  {
    path: '/',
    name: 'Home',
    component: LandingPage,
  },
  {
    path: '/course',
    name: 'Review',
    component: ReviewPage,
  }
]

// Create the router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
