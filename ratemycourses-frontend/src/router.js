import { createRouter, createWebHistory } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import AboutPage from './components/AboutPage.vue'

// Define the routes for your components
const routes = [
  {
    path: '/',
    name: 'Home',
    component: HelloWorld, // or another Home component if needed
  },
  {
    path: '/about',
    name: 'About',
    component: AboutPage, // Lazy-loaded component
  }
]

// Create the router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
