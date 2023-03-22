<template>
    <v-card class="avatar" border="true">
      <v-avatar
        image="https://pbs.twimg.com/profile_images/1237550450/mstom_400x400.jpg"
      >
      </v-avatar>
      <v-divider thickness="2"></v-divider>
      <h2>Name: {{ firstname}} {{ lastname }}</h2>
  
      <v-divider thickness="2"></v-divider>
      <h2>Major: {{ major }}</h2>
    </v-card>
  </template>
  
  
<script>
import { ref} from "vue";
import { useRoute } from "vue-router";
import { db } from '@/firebase';
import { collection, doc, getDoc } from "@firebase/firestore";

export default {
  name: "OtherProfileAvatar",
  setup() {
    const route = useRoute();
    const uid = ref(route.params.uid);
    const firstname= ref("");
    const lastname=ref("");
    const major = ref("Undecided");

    const fetchUserData = async (uid) => {
      const userRef = doc(collection(db, 'users'), uid);
      const userDoc = await getDoc(userRef);
      console.log(userDoc.data())
      return userDoc.data();
    };

    const getUserData = async () => {
      const user = await fetchUserData(uid.value);
      firstname.value = user.FirstName;
      lastname.value = user.LastName;
    };

    getUserData();

    return { firstname, lastname, major };
  }
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
  