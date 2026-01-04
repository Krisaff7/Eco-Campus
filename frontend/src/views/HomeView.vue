<template>
  <div class="home-container">
    <div class="logos">
      <a href="https://vite.dev" target="_blank">
        <img src="/vite.svg" class="logo" alt="Vite logo" />
      </a>
      <a href="https://vuejs.org/" target="_blank">
        <img src="../assets/vue.svg" class="logo vue-logo" alt="Vue logo" />
      </a>
    </div>
    
    <h1 class="title">🌿 Eco-Campus</h1>
    <p class="subtitle">Le covoiturage universitaire commence ici.</p>
    
    <div class="actions">
      <router-link to="/login" class="btn btn-primary">
        Se connecter
      </router-link>
      <router-link to="/register" class="btn btn-outline">
        Créer un compte
      </router-link>
    </div>
  </div>
</template>

<script setup>
// Home view logic will go here
</script>

<style scoped>
.home-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: var(--eco-light);
}

.logos {
  display: flex;
  gap: 2rem;
  margin-bottom: 3rem;
}

.logo {
  width: 100px;
  height: 100px;
  transition: filter 0.3s ease;
}

.logo:hover {
  filter: drop-shadow(0 0 2em rgba(100, 108, 255, 0.5));
}

.vue-logo:hover {
  filter: drop-shadow(0 0 2em rgba(66, 184, 131, 0.5));
}

.title {
  font-size: 3rem;
  font-weight: 800;
  color: var(--eco-green);
  margin-bottom: 1rem;
  letter-spacing: -0.02em;
}

.subtitle {
  font-size: 1.25rem;
  color: var(--eco-dark);
  font-style: italic;
  margin-bottom: 2rem;
}

.actions {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 100%;
  max-width: 300px;
}
</style>
