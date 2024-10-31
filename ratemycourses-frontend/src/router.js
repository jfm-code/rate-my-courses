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
    path: '/:name/:id/reviews', //allows it to route to a component with parameters that are passed to be used in the destination component. example: http://localhost:3000/comp II/1234/reviews
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
