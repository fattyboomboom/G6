<template>
 
  <!-- This nav drawer is set to permanent. will always be available on every screen size. -->
  <v-navigation-drawer  rail color="#e0e1dd"  permanent="">
    <v-list>
      <v-list-item
        prepend-avatar="https://pbs.twimg.com/profile_images/1237550450/mstom_400x400.jpg"
        title="Tom Anderson"
        subtitle="TomA@gmail.com"
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
        prepend-icon="mdi-cog"
        title="Settings"
        value="settings"
        to="/settings"
      ></v-list-item>
      <v-divider color="white"></v-divider>
      <v-list-item
        prepend-icon="mdi-logout"
        title="Sign Out"
        value="signOut"
        @click="Logout"
       
      ></v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { getAuth, signOut } from "firebase/auth"
//  import { useRouter } from "vue-router";

export default {
  name: "NavBar",
  setup() {
    // const router = useRouter();
  },
  methods: {
    Logout() {

        const auth = getAuth();
        console.log(auth.currentUser)
        signOut(auth).then(() => {
          console.log(auth.currentUser)
          // Sign-out successful.
          console.log("Sign Out")
          this.$router.push('/')
        }).catch((error) => {
          console.log(error)
        })
    }

 
  }
};
</script>

<style scoped>
.v-list-item {
  color: #166088;
}
</style>
