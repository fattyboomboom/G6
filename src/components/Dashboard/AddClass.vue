<template>
  <v-form>
    <v-card>
      <v-card-title class="text-h5">Add Class</v-card-title>
      <v-carousel :hide-delimiters="true" show-arrows="hover" height="">
        <v-carousel-item v-for="(classData, index) in classes" :key="index">
          <v-card-text class="">
            <v-col cols="12" md="12">
              <v-text-field
                :label="'Class Prefix ' + (index + 1)"
                v-model="classData.prefix"
                type="text"
                outlined
                :color="colors[index % colors.length]"
              ></v-text-field>
            </v-col>
            <v-col cols="12" md="12">
              <v-text-field
                :label="'Class Number ' + (index + 1)"
                v-model="classData.number"
                type="number"
                outlined
                :color="colors[index % colors.length]"
              ></v-text-field>
            </v-col>
            <v-col cols="12" md="12">
              <v-text-field
                :label="'Class Section ' + (index + 1)"
                v-model="classData.section"
                outlined
                :color="colors[index % colors.length]"
              ></v-text-field>
            </v-col>
            <v-divider></v-divider>
          </v-card-text>
        </v-carousel-item>
        
      </v-carousel>
      <v-btn @click="addClass" > Add Class </v-btn>
      <v-row>
        <v-col cols="12" md="10">
          <v-btn block @click="saveSettings">Save</v-btn>
        </v-col>
      </v-row>
    </v-card>
    
  </v-form>
</template>

<script>
import { db, auth } from "@/firebase";
import { doc, getDoc, updateDoc } from "firebase/firestore";

export default {
  name: "AddClass",
  data() {
    return {
      dialog: false,
      classes: [
        {
          prefix: "",
          number: null,
          section: "",
        },
      ],
      colors: ["blue", "green", "pink", "purple", "orange", "white"], // Add more colors as needed
    };
  },
  methods: {
    async saveSettings() {
      const userRef = doc(db, "users", auth.currentUser.uid);
      const userDoc = await getDoc(userRef);
      const existingClasses = userDoc.exists()
        ? userDoc.data().classes || []
        : [];
      const newClasses = this.classes.map((classData) => ({
        prefix: classData.prefix,
        number: classData.number,
        section: classData.section,
      }));
      const allClasses = [...existingClasses, ...newClasses];
      await updateDoc(userRef, { classes: allClasses });
    },
    addClass() {
      this.classes.push({
        prefix: "",
        number: null,
        section: "",
      });
    },
  },
};
</script>

<style scoped>
.v-form {
  background-color: rgba(
    255,
    255,
    255,
    0.5
  ); /* set a semi-transparent white background */
  backdrop-filter: blur(10px); /* apply a blur effect */
  opacity: 1; /* set the overall opacity */
}
.v-card {
  border: solid;
  border-color: #4a6fa5;
  border-width: 5px;
  margin: 5%;
  height: 80%;
  box-shadow: 0 16px 56px rgba(0, 0, 0, 0.1), 0 16px 56px rgba(0, 0, 0, 0.1),
    0 16px 56px rgba(0, 0, 0, 0.1);
  width: 35%;
}

.v-card-title {
  color: black;
  text-align: center;
}



.v-avatar {
  height: 100%;
  width: 100%;
  margin: 5px;
}

.v-btn {
  border-color: #4a6fa5;
  border: solid;
  border-width: 2px;
  margin-left: 11%;
}
.v-text-field {
  border-color: #4a6fa5;
  border: solid;
  border-width: 2px;
  margin-left: 2%;
}

@media (max-width: 600px) {
  .v-card {
    width: 80%;
    margin: 10% auto;
  }
}

@media (max-width: 400px) {
  .v-card {
    width: 90%;
    margin: 20% auto;
  }
}
</style>
