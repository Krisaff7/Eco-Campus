<template>
  <div class="min-h-screen flex flex-col items-center justify-center bg-eco-light">
    <div class="flex space-x-4 mb-8">
      <a href="https://vite.dev" target="_blank">
        <img src="/vite.svg" class="w-24 h-24 hover:drop-shadow-xl transition" alt="Vite logo" />
      </a>
      <a href="https://vuejs.org/" target="_blank">
        <img src="../assets/vue.svg" class="w-24 h-24 hover:drop-shadow-[0_0_2em_#42b883aa] transition" alt="Vue logo" />
      </a>
    </div>
    
    <h1 class="text-5xl font-extrabold text-eco-green mb-4 tracking-tight">🌿 Eco-Campus</h1>
    <p class="text-xl text-eco-dark italic mb-8">Le covoiturage universitaire commence ici.</p>
    
    <div class="flex flex-col space-y-4 w-full max-w-xs">
      <router-link 
        to="/login"
        class="bg-eco-blue text-white px-8 py-3 rounded-xl font-semibold shadow-lg hover:bg-opacity-90 transform hover:-translate-y-0.5 transition text-center"
      >
        Se connecter
      </router-link>
      <router-link 
        to="/register"
        class="bg-white text-eco-green border-2 border-eco-green px-8 py-3 rounded-xl font-semibold hover:bg-eco-light transform hover:-translate-y-0.5 transition text-center"
      >
        Créer un compte
      </router-link>
    </div>
  </div>
</template>

<script setup>
// Home view logic will go here
</script>
