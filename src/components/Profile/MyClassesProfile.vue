<template>
  <v-card class="classcard" variant="outlined">
    <v-list bg-color="#4a6fa5">
      <v-list-item-title class="itemtitle">
        <h2>My Classes</h2>
      </v-list-item-title>

      <v-divider thickness="2"></v-divider>
      <v-list>
        <v-list-item v-for="(item, index) in items" :key="index">
          <li>{{ item.prefix }} {{ item.number }} - {{ item.section }}</li>
        </v-list-item>
      </v-list>
    </v-list>
  </v-card>
</template>

<script>
import { ref, onMounted } from "vue";
import { db } from "@/firebase";
import { getAuth } from "firebase/auth";
import { doc, getDoc } from "firebase/firestore";

export default {
  name: "MyClassesProfile",

  setup() {
   
    const items = ref([]);

    const auth = getAuth();
    const uid = auth.currentUser.uid;
    const userDocRef = doc(db, "users", uid);

    // Load the initial items from Firebase
    onMounted(async () => {
      const userDocSnap = await getDoc(userDocRef);
      if (userDocSnap.exists()) {
        const data = userDocSnap.data();
        const classes = data.classes;
        console.log(classes);
        items.value = classes;
      } else {
        console.log("No such document!");
      }
    });

    return {
    
      items,
    };
  },
};
</script>

<style scoped>
.classcard {
  left: 10%;
  width: 30%;
  top: 1%;
  color: #e0e1dd;
  border: none;
  border-radius: 25px;
  margin-top: 5%;
  box-shadow: 0 16px 56px rgba(0, 0, 0, 0.1), 0 16px 56px rgba(0, 0, 0, 0.1),
    0 16px 56px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
}


h2 {
  background-color: #4a6fa5;
  color: white;
}

.listitem {
  background-color: #e0e1dd;
  width: 70%;
  margin: 0 15%;

  margin-top: 3%;
}

a {
  color: rgb(0, 0, 0);
}
v-card {
  background-color: #4a6fa5;
}



.v-card {
  border: 3px solid #4a6fa5;
}
</style>
