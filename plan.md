# Plan de Développement Eco-Campus

## 🎯 Vue d'ensemble

Ce document liste tous les éléments à créer pour l'application Eco-Campus, organisés par Frontend et Backend.

---

## 🎨 FRONTEND (Vue.js)

### 📄 Pages à créer (`src/views/`)

#### Authentification (4 pages)
- [ ] `LoginView.vue` - Connexion (Email/Téléphone)
- [ ] `RegisterView.vue` - Inscription multi-étapes
- [ ] `ForgotPasswordView.vue` - Réinitialisation mot de passe
- [x] `HomeView.vue` - Page d'accueil ✅

#### Application principale (6 pages)
- [ ] `DashboardView.vue` - Tableau de bord adaptatif
- [ ] `ProfileView.vue` - Profil utilisateur
- [ ] `TripsListView.vue` - Liste des trajets
- [ ] `TripDetailView.vue` - Détails d'un trajet
- [ ] `PublishTripView.vue` - Publier offre/demande
- [ ] `MyTripsView.vue` - Mes trajets
- [ ] `MessagesView.vue` - Messagerie

**Total : 10 pages (1/10 fait)**

---

### 🧩 Composants à créer (`src/components/`)

#### Navigation (2)
- [ ] `Navbar.vue` - Barre de navigation
- [ ] `NotificationBadge.vue` - Badge notifications

#### Authentification (2)
- [ ] `RoleSelector.vue` - Choix Conducteur/Passager
- [ ] `ProgressIndicator.vue` - Indicateur d'étapes

#### Trajets (3)
- [ ] `TripCard.vue` - Carte de trajet
- [ ] `TripFilters.vue` - Filtres de recherche
- [ ] `VehicleForm.vue` - Formulaire véhicule

#### Messagerie (3)
- [ ] `ConversationList.vue` - Liste conversations
- [ ] `ChatWindow.vue` - Fenêtre de chat
- [ ] `MessageBubble.vue` - Bulle de message

#### Utilitaires (1)
- [ ] `LoadingSpinner.vue` - Indicateur chargement

**Total : 11 composants (0/11 fait)**

---

### 💾 Stores Pinia à créer (`src/stores/`)

- [x] `auth.js` - Authentification ✅
- [ ] `trips.js` - Gestion trajets
- [ ] `messages.js` - Messagerie

**Total : 3 stores (1/3 fait)**

---

### 🔌 Services API à créer (`src/services/`)

- [x] `api.js` - Configuration Axios ✅
- [ ] `authService.js` - Auth endpoints
- [ ] `tripService.js` - Trajets endpoints
- [ ] `messageService.js` - Messages endpoints

**Total : 4 services (1/4 fait)**

---

### 🛣️ Router à mettre à jour

- [ ] Ajouter toutes les routes (publiques + protégées)
- [ ] Configurer les guards d'authentification

---

## ⚙️ BACKEND (Django)

### 🗄️ Modèles (Déjà créés ✅)

- [x] `User` - Utilisateur personnalisé
- [x] `Profile` - Profil utilisateur
- [x] `Vehicle` - Véhicule
- [x] `Offer` - Offre de trajet
- [x] `Request` - Demande de trajet
- [x] `Conversation` - Conversation
- [x] `Message` - Message

**Total : 7 modèles (7/7 fait) ✅**

---

### 🔧 API Endpoints à créer

#### Authentification (`users/`)
- [ ] `POST /api/users/register/` - Inscription
- [ ] `POST /api/users/login/` - Connexion
- [ ] `POST /api/users/logout/` - Déconnexion
- [ ] `POST /api/users/reset-password/` - Reset mot de passe
- [ ] `GET /api/users/profile/` - Récupérer profil
- [ ] `PUT /api/users/profile/` - Modifier profil

#### Trajets (`carpools/`)
- [ ] `GET /api/carpools/offers/` - Liste offres
- [ ] `POST /api/carpools/offers/` - Créer offre
- [ ] `GET /api/carpools/offers/:id/` - Détails offre
- [ ] `GET /api/carpools/requests/` - Liste demandes
- [ ] `POST /api/carpools/requests/` - Créer demande
- [ ] `GET /api/carpools/search/` - Rechercher trajets

#### Messagerie (`messaging/`)
- [ ] `GET /api/messaging/conversations/` - Liste conversations
- [ ] `POST /api/messaging/conversations/` - Créer conversation
- [ ] `GET /api/messaging/conversations/:id/messages/` - Messages
- [ ] `POST /api/messaging/messages/` - Envoyer message

**Total : 16 endpoints (0/16 fait)**

---

### 📝 Serializers à créer

- [ ] `UserSerializer`
- [ ] `ProfileSerializer`
- [ ] `VehicleSerializer`
- [ ] `OfferSerializer`
- [ ] `RequestSerializer`
- [ ] `ConversationSerializer`
- [ ] `MessageSerializer`

**Total : 7 serializers (0/7 fait)**

---

### 🎮 Views/ViewSets à créer

- [ ] `AuthViewSet` - Authentification
- [ ] `ProfileViewSet` - Profil
- [ ] `OfferViewSet` - Offres
- [ ] `RequestViewSet` - Demandes
- [ ] `ConversationViewSet` - Conversations
- [ ] `MessageViewSet` - Messages

**Total : 6 viewsets (0/6 fait)**

---

## 📊 Résumé Global

### Frontend
- Pages : 1/10 ✅
- Composants : 0/11
- Stores : 1/3 ✅
- Services : 1/4 ✅

### Backend
- Modèles : 7/7 ✅✅✅
- Endpoints : 0/16
- Serializers : 0/7
- ViewSets : 0/6

---

## 🚀 Ordre de Développement Recommandé

### Phase 1 : Authentification
**Backend** : Serializers + ViewSets + Endpoints Auth
**Frontend** : LoginView, RegisterView, RoleSelector, authService

### Phase 2 : Dashboard & Navigation
**Frontend** : DashboardView, Navbar, NotificationBadge

### Phase 3 : Gestion des Trajets
**Backend** : Serializers + ViewSets + Endpoints Trajets
**Frontend** : TripsListView, TripCard, PublishTripView, tripService

### Phase 4 : Profil
**Backend** : Endpoints Profil/Véhicule
**Frontend** : ProfileView, VehicleForm

### Phase 5 : Messagerie
**Backend** : Serializers + ViewSets + Endpoints Messages
**Frontend** : MessagesView, ChatWindow, MessageBubble, messageService

---

> [!NOTE]
> Ce fichier sera mis à jour au fur et à mesure de l'avancement du projet.
