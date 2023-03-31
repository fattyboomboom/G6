<template>
  <v-card class="avatar" border="true">
    <v-avatar :image="profileImage"></v-avatar>
    <v-divider thickness="2"></v-divider>
    <h2>Name: {{ username }}</h2>

    <v-divider thickness="2"></v-divider>
    <h2>Major: {{ major }}</h2>
  </v-card>
</template>

<script>
import { auth, db } from "@/firebase";
import { ref } from "vue";
import { doc, getDoc } from "firebase/firestore";

export default {
  name: "ProfileAvatar",
  setup() {
    const username = ref(auth.currentUser.displayName);
    const major = ref("Undecided");
    const profileImage = ref("");

    async function getImage(uid) {
      const docRef = doc(db, "users", uid);
      const docSnap = await getDoc(docRef);

      if (docSnap.exists()) {
        const data = docSnap.data();
        const imageUrl = data.profilePicture;
        return imageUrl;
      } else {
        console.log("No such document!");
      }
    }

    getImage(auth.currentUser.uid).then((url) => {
      profileImage.value = url;
    });

    return { username, major, profileImage };
  },
};
</script>

<style scoped>
.avatar {
  position: absolute;
  margin-left: 6%;
  margin-top: 1%;
  background-color: #4a6fa5;
  width: 25%;
  border: none;
  border-radius: 25px;
  box-sizing: border-box;
}
.v-avatar {
  width: 70%;
  height: auto;
  margin-left: 15%;
  margin-top: 2%;
  margin-bottom: 2%;
}

body {
  background-color: #4a6fa5;
}

.v-divider {
  color: #dbe9ee;
}

h2 {
  color: #fdf0d5;
  font-size: 1.5rem;
  margin-inline: 5%;
  text-align: left;
  line-height: 2;
}
</style>
