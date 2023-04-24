<template>
    <v-container>
      <v-row>
        <v-col md="12" >
          <v-avatar :image=profilePicture >
           
          </v-avatar>
          <h2 class="my-4">{{ firstname }} {{ lastname }}</h2>
          <v-btn color="login" class="mb-4" v-model="follow" @click="followClicked">{{ followText }}</v-btn>
          <v-card class="class-list mt-6">
            <v-card-text>
            <h1>Classes</h1>
            
              <v-list >
                <v-list-item v-for="(userClass, index) in classes" :key="index">
                  <v-btn class="classButton" elevation="0" style="cursor: pointer" :to="'/classes/' + userClass.prefix + userClass.number">{{ userClass.prefix }}{{ userClass.number }}</v-btn>
                </v-list-item>
              </v-list>
            </v-card-text>
          </v-card>
        </v-col>
       
      </v-row>
    </v-container>
  </template>
  
  <script>
  import { ref} from "vue";
  import { useRoute } from "vue-router";
  import { db } from '@/firebase';
  import { collection, getDocs, where, query } from "@firebase/firestore";
  export default {
    name: "OtherProfileAvatar",
    setup() {
      const route = useRoute();
      // const uid = ref(route.params.uid);
      const username = ref(route.params.username);
      const firstname= ref("");
      const lastname=ref("");
      const profilePicture=ref("");
      const major = ref("Undecided");
      const classes = ref([])
      const fetchUserData = async (username) => {
    const usersRef = collection(db, 'users');
    const q = query(usersRef, where('username', '==', username));
    const querySnapshot = await getDocs(q);
    if (querySnapshot.empty) {
      throw new Error(`No user found with username: ${username}`);
    }
    const userDoc = querySnapshot.docs[0];
    return userDoc.data();
  };
  const getUserData = async () => {
    const user = await fetchUserData(username.value);
    firstname.value = user.FirstName;
    lastname.value = user.LastName;
    profilePicture.value = user.profilePicture;
    classes.value = user.classes || [];
  };
      getUserData();
      console.log(profilePicture)
      return { firstname, lastname, major, profilePicture, classes };
    }
  };
  </script>
  
  <style scoped>
  .v-container {
    width: 40%;
    margin-left: 10%;
    text-align: center;
    border-color: #4a6fa5;
    border-style: solid;
    margin-top: 5%;
    height: 80%;
    box-shadow: 0 16px 56px rgba(0, 0, 0, 0.1), 0 16px 56px rgba(0, 0, 0, 0.1),
      0 16px 56px rgba(0, 0, 0, 0.1);
  }
  .v-card-text {
    text-align: center;
    border-color: #4a6fa5;
    border-style: solid;
  }
  .v-avatar {
    width: 40%;
    height: auto;
    margin-top: 2%;
    margin-bottom: 2%;
  }
  .classButton{
    background-color: transparent;
  }
  </style>