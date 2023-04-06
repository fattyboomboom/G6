<template>
  
  <v-form>
    <v-card>
      <v-card-title class="text-h5">Add Class</v-card-title>
      <v-carousel hide-delimiter-background delimiter-icon="mdi-square" show-arrows="hover" height="">
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
            <v-col cols="12" md="12" class="mb-4">
              <v-text-field
                :label="'Class Section ' + (index + 1)"
                v-model="classData.section"
                outlined
                :color="colors[index % colors.length]"
              ></v-text-field>
            </v-col>
           
          </v-card-text>
           <v-divider class="mb-2 "></v-divider>
        </v-carousel-item>
       
      </v-carousel>
      <v-btn class="addClass" @click="addClass"> Add Class </v-btn>
      <v-row>
        <v-col cols="12" md="10">
          <v-btn class="saveBtn" block @click="saveSettings">Save</v-btn>
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
 
      classes: [
        {
          prefix: "",
          number: null,
          section: "",
        },
      ],
      colors: ["blue", "green", "pink", "purple", "orange", "white"], 
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
        prefix: classData.prefix.replace(/\s+/g, '').toUpperCase(),
        number: classData.number.replace(/\s+/g, ''),
        section: classData.section.replace(/\s+/g, ''),
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
  
  position: absolute;
  z-index: 1;
  margin-left: 25%;
  margin-right: 25%;
  margin-top: 5%;
  margin-bottom: 5%;
  width: 50%;
}
.v-card {
  border: solid;
  border-color: #4a6fa5;
  border-width: 5px;
  margin: 5%;
  height: 92%;
  box-shadow: 0 16px 56px rgba(0, 0, 0, 0.1), 0 16px 56px rgba(0, 0, 0, 0.1),
    0 16px 56px rgba(0, 0, 0, 0.1);
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
  margin-bottom: 3%;
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

.addClass {
  /* margin-left: 11%; */
  margin-bottom: 3%;
  margin-inline: 40%;
  background-color: #c0d6df;
}

.saveBtn {

  background-color: #166088;
}

@media (max-width: 400px) {
  .v-card {
    width: 90%;
    margin: 20% auto;
  }
}
</style>
