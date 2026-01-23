<template>
  <div class="app-wrapper">
    <!-- Header / Navigation -->
    <header class="header">
      <div class="container nav-container">
        <router-link to="/" class="logo">
          <div class="logo-icon">
            <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2L2 7L12 12L22 7L12 2Z" fill="#14b8a6" />
              <path d="M2 17L12 22L22 17" stroke="#14b8a6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M2 12L12 17L22 12" stroke="#14b8a6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
          </div>
          <span class="logo-text">Éco<span>Campus</span></span>
        </router-link>

        <nav class="nav-links">
          <router-link to="/trajets" class="nav-link">
            <span class="nav-icon">🔍</span> Trajets
          </router-link>
          <router-link to="/mes-trajets" class="nav-link">
            <span class="nav-icon">🚗</span> Mes trajets
          </router-link>
          <router-link to="/messages" class="nav-link">
            <span class="nav-icon">💬</span> Messages
          </router-link>
          <router-link to="/profil" class="nav-link">
            <span class="nav-icon">👤</span> Profil
          </router-link>
        </nav>

        <div class="nav-auth">
          <router-link to="/login" class="btn btn-text">Connexion</router-link>
          <router-link to="/register" class="btn btn-primary">S'inscrire</router-link>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="main-content">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>

    <!-- Footer -->
    <footer class="footer">
      <div class="container footer-content">
        <div class="footer-info">
          <div class="logo">
            <div class="logo-icon">
              <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 2L2 7L12 12L22 7L12 2Z" fill="#14b8a6" />
                <path d="M2 17L12 22L22 17" stroke="#14b8a6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                <path d="M2 12L12 17L22 12" stroke="#14b8a6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
              </svg>
            </div>
            <span class="logo-text">Éco<span>Campus</span></span>
          </div>
          <p class="footer-desc">
            La plateforme de covoiturage écologique pour les étudiants. 
            Partagez vos trajets et réduisez votre empreinte carbone.
          </p>
        </div>

        <div class="footer-links">
          <div class="footer-group">
            <h4>Navigation</h4>
            <router-link to="/">Accueil</router-link>
            <router-link to="/trajets">Trajets</router-link>
            <router-link to="/publier">Publier</router-link>
            <router-link to="/messages">Messages</router-link>
          </div>
          <div class="footer-group">
            <h4>Compte</h4>
            <router-link to="/login">Connexion</router-link>
            <router-link to="/register">Inscription</router-link>
            <router-link to="/profil">Mon profil</router-link>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 ÉcoCampus. Tous droits réservés.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
// Global layout logic if needed
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

:root {
  --primary: #14b8a6;
  --primary-dark: #0d9488;
  --primary-light: #ccfbf1;
  --text-main: #0f172a;
  --text-muted: #64748b;
  --bg-app: #f8fafc;
  --white: #ffffff;
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --container-width: 1200px;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', sans-serif;
  background-color: var(--bg-app);
  color: var(--text-main);
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

.app-wrapper {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.container {
  max-width: var(--container-width);
  margin: 0 auto;
  padding: 0 1.5rem;
}

/* Header */
.header {
  background: var(--white);
  border-bottom: 1px solid #f1f5f9;
  position: sticky;
  top: 0;
  z-index: 100;
  height: 72px;
  display: flex;
  align-items: center;
}

.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

.logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  text-decoration: none;
}

.logo-icon {
  width: 32px;
  height: 32px;
}

.logo-text {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--text-main);
}

.logo-text span {
  color: var(--primary);
}

.nav-links {
  display: flex;
  gap: 1.5rem;
}

.nav-link {
  text-decoration: none;
  color: var(--text-main);
  font-weight: 500;
  font-size: 0.9375rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: color 0.2s;
}

.nav-link:hover {
  color: var(--primary);
}

.nav-auth {
  display: flex;
  gap: 1rem;
  align-items: center;
}

/* Buttons */
.btn {
  padding: 0.625rem 1.25rem;
  border-radius: 9999px;
  font-weight: 600;
  font-size: 0.9375rem;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.2s;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: none;
}

.btn-primary {
  background: var(--primary);
  color: var(--white);
  box-shadow: 0 4px 6px -1px rgba(20, 184, 166, 0.2);
}

.btn-primary:hover {
  background: var(--primary-dark);
  transform: translateY(-1px);
}

.btn-text {
  color: var(--text-main);
}

.btn-text:hover {
  color: var(--primary);
}

/* Main Content */
.main-content {
  flex-grow: 1;
}

/* Footer */
.footer {
  background: var(--white);
  padding-top: 4rem;
  border-top: 1px solid #f1f5f9;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  margin-bottom: 4rem;
}

.footer-info {
  max-width: 320px;
}

.footer-desc {
  margin-top: 1rem;
  color: var(--text-muted);
  font-size: 0.9375rem;
}

.footer-links {
  display: flex;
  gap: 4rem;
}

.footer-group h4 {
  margin-bottom: 1.5rem;
  font-size: 1rem;
  font-weight: 600;
}

.footer-group a {
  display: block;
  text-decoration: none;
  color: var(--text-muted);
  margin-bottom: 0.75rem;
  font-size: 0.9375rem;
  transition: color 0.2s;
}

.footer-group a:hover {
  color: var(--primary);
}

.footer-bottom {
  border-top: 1px solid #f1f5f9;
  padding: 1.5rem 0;
  text-align: center;
  color: var(--text-muted);
  font-size: 0.875rem;
}

/* Transitions */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

@media (max-width: 1024px) {
  .nav-links {
    display: none; /* Mobile navigation would go here */
  }
}
</style>
