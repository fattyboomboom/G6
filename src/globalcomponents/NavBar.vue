<template>
 
  <!-- This nav drawer is set to permanent. will always be available on every screen size. -->
  <v-navigation-drawer  rail color="#e0e1dd"  permanent="">
    <v-list>
      <v-list-item
  :prepend-avatar="userProfilePicture"
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
import { ref, onMounted } from "vue";
import { getFirestore, doc, getDoc } from "firebase/firestore";
import { getAuth, signOut } from "firebase/auth";

export default {
  name: "NavBar",
  setup() {
    const userProfilePicture = ref("");

    onMounted(async () => {
      const auth = getAuth();
      const uid = auth.currentUser.uid;
      const db = getFirestore();
      const userDocRef = doc(db, "users", uid);
      const userDocSnapshot = await getDoc(userDocRef);

      if (userDocSnapshot.exists()) {
        userProfilePicture.value = userDocSnapshot.data().profilePicture;
      } else {
        console.log("No such user document!");
      }
    });

    return {
      userProfilePicture,
    };
  },
  methods: {
    Logout() {
      const auth = getAuth();
      console.log(auth.currentUser);
      signOut(auth)
        .then(() => {
          console.log(auth.currentUser);
          console.log("Sign Out");
          this.$router.push("/");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.v-list-item {
  color: #166088;
}
</style>
