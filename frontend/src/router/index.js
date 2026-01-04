import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('../views/HomeView.vue') // Placeholder
        },
        {
            path: '/register',
            name: 'register',
            component: () => import('../views/HomeView.vue') // Placeholder
        }
    ]
})

export default router
