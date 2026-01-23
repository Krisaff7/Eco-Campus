<template>
  <div class="home-view">
    <!-- Hero Section -->
    <section class="hero">
      <div class="container hero-container">
        <div class="hero-tag">
          <span class="tag-icon">🍃</span> Covoiturage écologique pour étudiants
        </div>
        <h1 class="hero-title">
          Partagez vos trajets,<br />
          <span class="text-gradient">préservez la planète</span>
        </h1>
        <p class="hero-subtitle">
          Rejoignez la communauté ÉcoCampus et trouvez facilement des<br />
          covoiturages entre votre domicile et le campus.
        </p>
        <div class="hero-actions">
          <router-link to="/register" class="btn btn-primary btn-lg">
            Commencer maintenant <span class="btn-arrow">→</span>
          </router-link>
          <router-link to="/trajets" class="btn btn-outline btn-lg"> Explorer les trajets </router-link>
        </div>

        <!-- Stats Bar -->
        <div class="hero-stats">
          <div class="stat-item">
            <div class="stat-icon users">👥</div>
            <div class="stat-content">
              <span class="stat-number">500+</span>
              <span class="stat-label">Utilisateurs</span>
            </div>
          </div>
          <div class="stat-item">
            <div class="stat-icon paths">🕒</div>
            <div class="stat-content">
              <span class="stat-number">1000+</span>
              <span class="stat-label">Trajets/mois</span>
            </div>
          </div>
          <div class="stat-item">
            <div class="stat-icon co2">🍃</div>
            <div class="stat-content">
              <span class="stat-number">2.5t</span>
              <span class="stat-label">CO₂ économisé</span>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Background Decorative Elements -->
      <div class="hero-bg-blobs">
        <div class="blob blob-1"></div>
        <div class="blob blob-2"></div>
      </div>
    </section>

    <!-- Why Choose Sections -->
    <section class="features">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">Pourquoi choisir <span>ÉcoCampus</span> ?</h2>
          <p class="section-subtitle">Une solution complète pour organiser vos covoiturages quotidiens vers le campus.</p>
        </div>

        <div class="features-grid">
          <div class="feature-card">
            <div class="feature-icon ic-1">📍</div>
            <h3>Matching intelligent</h3>
            <p>Notre algorithme trouve les meilleurs covoiturages selon votre itinéraire et vos horaires.</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon ic-2">🕒</div>
            <h3>Trajets quotidiens</h3>
            <p>Programmez vos trajets réguliers et trouvez des covoitureurs avec les mêmes horaires.</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon ic-3">💬</div>
            <h3>Messagerie intégrée</h3>
            <p>Communiquez facilement avec conducteurs et passagers via notre chat instantané.</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon ic-4">🛡️</div>
            <h3>Sécurité garantie</h3>
            <p>Profils vérifiés et données personnelles protégées pour des trajets en confiance.</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon ic-5">⚡</div>
            <h3>Simple et rapide</h3>
            <p>Publiez une offre ou une demande en quelques secondes depuis votre mobile.</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon ic-6">💛</div>
            <h3>Écologique</h3>
            <p>Réduisez votre empreinte carbone en partageant vos trajets avec d'autres étudiants.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- How it works -->
    <section class="how-it-works">
      <div class="container">
        <h2 class="section-title text-center">Comment ça marche ?</h2>
        <p class="section-subtitle text-center">En 4 étapes simples, trouvez votre covoiturage idéal.</p>

        <div class="steps-container">
          <div class="step-item">
            <div class="step-icon-wrap">
              <div class="step-icon">👤</div>
              <span class="step-number">1</span>
            </div>
            <h4>Créez votre profil</h4>
            <p>Inscrivez-vous et indiquez si vous êtes conducteur ou passager.</p>
          </div>
          <div class="step-item">
            <div class="step-icon-wrap">
              <div class="step-icon">🔍</div>
              <span class="step-number">2</span>
            </div>
            <h4>Trouvez un trajet</h4>
            <p>Recherchez des trajets compatibles avec votre itinéraire.</p>
          </div>
          <div class="step-item">
            <div class="step-icon-wrap">
              <div class="step-icon">✅</div>
              <span class="step-number">3</span>
            </div>
            <h4>Confirmez</h4>
            <p>Contactez votre covoitureur et organisez le rendez-vous.</p>
          </div>
          <div class="step-item">
            <div class="step-icon-wrap">
              <div class="step-icon">🚗</div>
              <span class="step-number">4</span>
            </div>
            <h4>Voyagez ensemble</h4>
            <p>Partagez votre trajet et réduisez votre impact écologique.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="final-cta">
      <div class="container">
        <div class="cta-banner">
          <h2 class="cta-title">Prêt à rejoindre la communauté ?</h2>
          <p class="cta-subtitle">Inscrivez-vous gratuitement et commencez à partager vos trajets avec d'autres étudiants de votre campus.</p>
          <div class="cta-actions">
            <router-link to="/register" class="btn btn-white btn-lg">Créer mon compte <span class="btn-arrow">→</span></router-link>
            <router-link to="/trajets" class="btn btn-outline-white btn-lg">Voir les trajets</router-link>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
// Home page logic
</script>

<style scoped>
.home-view {
  overflow-x: hidden;
}

.text-center { text-align: center; }

/* Hero Section */
.hero {
  padding: 6rem 0 4rem;
  position: relative;
  text-align: center;
}

.hero-container {
  position: relative;
  z-index: 10;
}

.hero-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: #ccfbf1;
  color: #0d9488;
  padding: 0.5rem 1rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 600;
  margin-bottom: 2rem;
}

.hero-title {
  font-size: 4rem;
  font-weight: 800;
  line-height: 1.1;
  color: #1e293b;
  margin-bottom: 1.5rem;
  letter-spacing: -0.02em;
}

.text-gradient {
  color: var(--primary);
}

.hero-subtitle {
  font-size: 1.25rem;
  color: var(--text-muted);
  margin-bottom: 3rem;
  line-height: 1.6;
}

.hero-actions {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
  margin-bottom: 6rem;
}

.btn-lg {
  padding: 0.875rem 2rem;
  font-size: 1.0625rem;
}

.btn-outline {
  background: white;
  border: 1px solid #e2e8f0;
  color: var(--text-main);
  box-shadow: var(--shadow-sm);
}

.btn-outline:hover {
  border-color: var(--primary);
  color: var(--primary);
}

.btn-arrow {
  margin-left: 0.5rem;
  transition: transform 0.2s;
}

.btn:hover .btn-arrow {
  transform: translateX(4px);
}

/* Stats */
.hero-stats {
  display: flex;
  justify-content: center;
  gap: 4rem;
  margin-top: 2rem;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  margin-bottom: 0.75rem;
}

.stat-icon.users { background: #e0f2fe; }
.stat-icon.paths { background: #dbeafe; }
.stat-icon.co2 { background: #fef3c7; }

.stat-number {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--text-main);
  display: block;
}

.stat-label {
  font-size: 0.875rem;
  color: var(--text-muted);
  font-weight: 500;
}

/* Blobs */
.hero-bg-blobs .blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  z-index: 1;
  opacity: 0.15;
}

.blob-1 {
  width: 400px;
  height: 400px;
  background: var(--primary);
  top: -100px;
  left: -100px;
}

.blob-2 {
  width: 300px;
  height: 300px;
  background: #3b82f6;
  bottom: 0px;
  right: -50px;
}

/* Features */
.features {
  padding: 8rem 0;
  background: white;
}

.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 800;
  color: #1e293b;
  margin-bottom: 1rem;
}

.section-title span {
  color: var(--primary);
}

.section-subtitle {
  font-size: 1.125rem;
  color: var(--text-muted);
  max-width: 600px;
  margin: 0 auto;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
}

.feature-card {
  padding: 2.5rem;
  border-radius: 20px;
  background: var(--bg-app);
  border: 1px solid #f1f5f9;
  transition: all 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-md);
  border-color: var(--primary-light);
}

.feature-icon {
  width: 54px;
  height: 54px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
}

.ic-1 { background: #e0f2fe; }
.ic-2 { background: #dbeafe; }
.ic-3 { background: #fef3c7; }
.ic-4 { background: #f1f5f9; }
.ic-5 { background: #eff6ff; }
.ic-6 { background: #fff7ed; }

.feature-card h3 {
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: #1e293b;
}

.feature-card p {
  color: var(--text-muted);
  line-height: 1.6;
}

/* How it works */
.how-it-works {
  padding: 8rem 0;
}

.steps-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
  margin-top: 5rem;
}

.step-item {
  text-align: center;
  position: relative;
}

.step-icon-wrap {
  width: 80px;
  height: 80px;
  margin: 0 auto 2rem;
  position: relative;
}

.step-icon {
  width: 100%;
  height: 100%;
  background: white;
  border: 2px solid #e2e8f0;
  border-radius: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  box-shadow: var(--shadow-sm);
}

.step-number {
  position: absolute;
  top: -8px;
  right: -8px;
  width: 28px;
  height: 28px;
  background: var(--primary);
  color: white;
  border-radius: 50%;
  font-weight: 700;
  font-size: 0.8125rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 4px solid var(--bg-app);
}

.step-item h4 {
  font-size: 1.125rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.step-item p {
  color: var(--text-muted);
  font-size: 0.9375rem;
}

/* Final CTA */
.final-cta {
  padding: 4rem 0 8rem;
}

.cta-banner {
  background: var(--primary);
  padding: 5rem 2rem;
  border-radius: 32px;
  text-align: center;
  color: white;
  box-shadow: 0 20px 40px -10px rgba(20, 184, 166, 0.4);
}

.cta-title {
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 1.5rem;
}

.cta-subtitle {
  font-size: 1.125rem;
  max-width: 600px;
  margin: 0 auto 3rem;
  opacity: 0.9;
}

.cta-actions {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
}

.btn-white {
  background: white;
  color: var(--primary);
}

.btn-white:hover {
  background: var(--bg-app);
  transform: translateY(-2px);
}

.btn-outline-white {
  background: transparent;
  border: 2px solid rgba(255, 255, 255, 0.3);
  color: white;
}

.btn-outline-white:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: white;
}

@media (max-width: 1024px) {
  .steps-container {
    grid-template-columns: repeat(2, 1fr);
    gap: 4rem 2rem;
  }
}

@media (max-width: 768px) {
  .hero-title { font-size: 2.5rem; }
  .hero-stats { flex-direction: column; gap: 2rem; }
  .cta-actions { flex-direction: column; }
  .hero-actions { flex-direction: column; }
}
</style>
