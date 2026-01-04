import { defineStore } from 'pinia'
import api from '../services/api'

export const useAuthStore = defineStore('auth', {
    state: () => ({
        user: null,
        token: localStorage.getItem('token') || null,
        loading: false,
        error: null
    }),

    getters: {
        isAuthenticated: (state) => !!state.token,
        userRole: (state) => state.user?.role
    },

    actions: {
        async login(credentials) {
            this.loading = true
            try {
                const response = await api.post('users/login/', credentials)
                this.user = response.data.user
                this.token = response.data.token
                localStorage.setItem('token', this.token)
                return true
            } catch (err) {
                this.error = err.response?.data?.message || 'Login failed'
                return false
            } finally {
                this.loading = false
            }
        },

        logout() {
            this.user = null
            this.token = null
            localStorage.removeItem('token')
        }
    }
})
