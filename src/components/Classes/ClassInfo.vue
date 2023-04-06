<template>
    <v-card class="avatar" border="true">
      <div class="avatar-container">
      <v-avatar
        :image=classPhoto
        size = 200
      >
      </v-avatar>
      </div>
      <v-divider thickness="2"></v-divider>
      <h2 style="text-align: center;">{{ classPrefix }}{{ classNumber }}</h2>
      <v-divider thickness="2"></v-divider>
      <h3 style="text-align: center;">Students</h3>
  
      
      
    </v-card>
  </template>
  
  
<script>
import { ref} from "vue";
import { useRoute } from "vue-router";
import { db } from '@/firebase';
import { collection, query, getDocs, where} from "@firebase/firestore";
export default {
  name: "ClassInfo",
  setup() {
    const route = useRoute();
    const classPrefix = ref(route.params.classPrefix);
    const classNumber = ref(route.params.classNumber)
    const profFirstName= ref("");
    const profLastName=ref("");
    const profTitle = ref("");
    const classPhoto = ref("");
    const fetchClassData = async (classPrefix, classNumber) => {
    const querySnapshot = await getDocs(
        query(
        collection(db, 'classes'),
        where("classPrefix", "==", classPrefix),
        where("classNumber", "==", classNumber)
        )
    );
    if (querySnapshot.docs.length > 0) {
        return querySnapshot.docs[0].data();
    } else {
        throw new Error(`Class ${classPrefix} - ${classNumber} not found`);
    }
    };
    const getClassData = async () => {
    const classData = await fetchClassData(classPrefix.value, classNumber.value);
    profFirstName.value = classData.profFirstName;
    profLastName.value = classData.profLastName;
    classPhoto.value = classData.classPhoto
    profTitle.value = classData.profTitle;
    };
    getClassData();
    return { classPrefix, classNumber, profFirstName, profLastName, profTitle, classPhoto};
  }
};
</script>
  
  <style scoped>
  .avatar {
    position: absolute;
    margin-left: 6%;
    margin-top: 1%;
    background-color: #e0e1dd;
    border: 6px solid #4a6fa5;
    width: 25%;
    border-radius: 25px;
    box-sizing: border-box;
    align-items: center;
  }
  .avatar-container {
  display: flex;
  justify-content: center;
 
}
  .v-avatar {
    width: 70%;
    height: auto;
    margin-top: 2%;
    margin-bottom: 2%;
  }
  
  body {
    background-color: #4a6fa5;
  }
  
  .v-divider {
    color: black;
  }
  
  h2 {
    color: black;
    font-size: 1.5rem;
    margin-inline: 5%;
    text-align: left;
    line-height: 2;
  }
  h3 {
    color: black;
    font-size: 1.25rem;
    margin-inline: 5%;
    text-align: left;
    line-height: 2;
  }
  </style>