<template>
  <v-card class="classcard" variant="outlined">
    <v-list bg-color="#4a6fa5">
      <v-list-item-title class="itemtitle">
        <h2>My Classes</h2>
      </v-list-item-title>

      <v-divider thickness="2"></v-divider>

      <v-list>
        <v-list-item v-for="(item, index) in items" :key="index">
          
          
         <li> <v-btn class="classButton" elevation="0" style="cursor: pointer" :to="'/classes/' + item.prefix + item.number">{{ item.prefix }} {{ item.number }}</v-btn>
          </li> 
          <div v-show="!editbtn">
            <v-btn icon @click="removeClass(index)">
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </div>
        </v-list-item>
        <v-list-item v-if="addingItem">
          <v-text-field
            v-model="newItem"
            @keydown.enter="addItem"
            label="New Item"
          ></v-text-field>
        </v-list-item>
      </v-list>
    </v-list>

    <VBtn class="addclass" color="success" width="50%" rounded="0" @click="$emit('add-class')">Add</VBtn>


    <VBtn class="deleteclass" width="50%" rounded="0" @click="editToggle">Delete</VBtn>
  </v-card>
</template>

<script>
import { ref, onMounted, watch } from "vue";
import { db } from "@/firebase";
import { getAuth } from "firebase/auth";
import { collection,addDoc, doc, getDoc } from "firebase/firestore";


export default {
  name: "MyClasses",

  setup() {
    const newItem = ref("");
    const items = ref([]);
    let editbtn = ref(true);


    const auth = getAuth();
    const uid = auth.currentUser.uid;
    const userDocRef = doc(db, 'users', uid);
  
    // Load the initial items from Firebase
    onMounted(async () => {
      const userDocSnap = await getDoc(userDocRef);
      if (userDocSnap.exists()) {
        const data = userDocSnap.data();
        const classes = data.classes;
        console.log(classes);
        items.value = classes;
      } else {
        console.log('No such document!');
      }
    });

    function removeClass(index) {
      items.value.splice(index, 1);
    }

    function editToggle() {
      editbtn.value = !editbtn.value;
    }


    watch(items, async (newVal) => {
      // create a reference to the 'classes' collection
      const classesRef = collection(db, "classes");

      // loop through the new items and add them to the 'classes' collection
      for (const item of newVal) {
        await addDoc(classesRef, { name: item });
      }
    });

    const addingItem = ref(false);

    return {
      newItem,
      items,
      addingItem,
    
      removeClass,
      editToggle,
      editbtn,
    };
  },
};
</script>

<style scoped>
.classcard {
  position: absolute;
  right: 1%;
  width: 20%;
  top: 1%;
  color: #e0e1dd;
  border: none;
  border-radius: 25px;
}

h2 {
  text-align: center;
}

.editbutton {
  background-color: #4a6fa5;
  width: 100%;
  transition: width 2s, height 2s, transform 2s;
}

.editbutton:hover {
  background-color: #669bbc;

  transform: rotateY(360deg);
}

.addclass {
  left: 0%;
  background-color: #669bbc;
}
.deleteclass {
  right: 0%;
  background-color: #c1121f;
}

h2 {
  background-color: #4a6fa5;
  color: white;
}

.listitem {
  background-color: #e0e1dd;
  /* color: white; */
  width: 70%;
  margin: 0 15%;
  border: none;
  border-radius: 5px;
  list-style: none;
  margin-top: 3%;
}
a {
  color: rgb(0, 0, 0);
}
v-card {
  background-color: #4a6fa5;
}
.itemtitle {
  background-color: #4a6fa5;
}
input {
  color: white;
  width: 70%;
  margin: 0 15%;
  border: none;
  border-radius: 5px;
  list-style: none;
  margin-top: 3%;
}

.listitem:hover {
  scale: 1.2;
}

.v-card {
  border: 3px solid #4a6fa5;
}
</style>
