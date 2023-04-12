<template>
 
  <!-- This nav drawer is set to permanent. will always be available on every screen size. -->
  <v-navigation-drawer expand-on-hover rail color="#e0e1dd"  permanent="">
    <v-list>
      <v-list-item
        prepend-avatar="https://static.vecteezy.com/system/resources/thumbnails/009/292/244/small/default-avatar-icon-of-social-media-user-vector.jpg"
        title="UserName"
        subtitle="email"
      ></v-list-item>
    </v-list>
    <v-divider color="white"></v-divider>
    <v-list density="compact" nav>
      <v-list-item prepend-icon="mdi-home" title="Home" value="home" to="/home">
      </v-list-item>
      <v-list-item
        prepend-icon="mdi-domain"
        title="Explore"
        value="explore"
        to="/explore"
      ></v-list-item>
      <v-list-item
        prepend-icon="mdi-tag"
        title="Book Resell"
        value="resell"
        to="/bookresell"
      ></v-list-item>
      <v-list-item
        prepend-icon="mdi-pen"
        title="Study"
        value="study"
      ></v-list-item>
      <v-list-item
        prepend-icon="mdi-note"
        title="Notes"
        value="notes"
        to="/notes"
      ></v-list-item>
      <v-divider color="white"></v-divider>
      <v-list-item
        prepend-icon="mdi-logout"
        title="Sign Out"
        value="signOut"
        to="/"
        @click="logout"
      ></v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
// import { ref } from 'vue';
// import { auth } from '@/firebase'
export default {

  name: "NavBar",
  // setup(){
  //   const displayName = ref(auth.currentUser.displayName);
  //   const userEmail= ref(auth.currentUser.email);

  //  return{userEmail, displayName};
  // },
  methods: {logout() {
      // Remove the token from the local storage
      localStorage.removeItem('token')
      // Navigate back to the login page
      this.$router.push('/')
    }},

    
};
</script>

<style scoped>
.v-list-item {
  color: #166088;
}
</style>