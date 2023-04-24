<template>
  <v-card class="avatar" border="true">
    <v-avatar> <v-img :src="profileImage"></v-img> </v-avatar>
    <v-divider thickness="2"></v-divider>
    <h2>Name: {{ firstName }}  {{  lastName }}</h2>

    <v-divider thickness="2"></v-divider>
    <h2>Major: {{ major }}</h2>
  </v-card>
</template>

<script>
import { auth, db } from "@/firebase";
import { ref, onMounted } from "vue";
import { collection, query, where, onSnapshot } from "firebase/firestore";

export default {
  name: "ProfileAvatar",
  setup() {
    const firstName= ref("");
    const lastName = ref("");
    const major = ref("");
    const profileImage = ref("");

    const userRef = collection(db, "users");
    const q = query(userRef, where("uid", "==", auth.currentUser.uid));
    console.log(q);

    const fetchImage = () => {
      try {
        onSnapshot(q, (querySnapshot) => {
          querySnapshot.forEach((doc) => {
            profileImage.value = doc.data().profilePicture;
            major.value = doc.data().Major;
            firstName.value = doc.data().FirstName;
            lastName.value = doc.data().LastName;
          });
        });
      } catch (err) {
        console.log(err.message);
      }
    };

    onMounted(() => {
      fetchImage();
    });

    return {
      firstName,
      lastName,
      major,
      profileImage,
    };
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
  height: 40%;
}
.v-avatar {
  width: 70%;
  height: 65%;
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
