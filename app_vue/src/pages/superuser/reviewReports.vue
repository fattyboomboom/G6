<template>
    
    <super-nav-bar></super-nav-bar>

  <v-container fluid>
    <v-card>
      <v-card-title class="justify-center">Reported Posts</v-card-title>
      <v-card-text>
        <v-simple-table>
          <thead>
            <tr>
              <th class="text-left">ID</th>
              <th class="text-left">Author</th>
              <th class="text-left">Date</th>
              <th class="text-left">Content</th>
              <th class="text-center">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="post in posts" :key="post.post_id">
              <td>{{ post.id }}</td>
              <td>{{ post.name }}</td>
              <td>{{ post.date }}</td>
              <td>{{ post.content }}</td>
              <td class="text-right">
                <v-btn color="red" class="mr-3">Delete</v-btn>
                <!-- <v-btn color="primary">Repeal</v-btn> -->
              </td>
            </tr>
            <tr>
              <td colspan="5" class="border-top py-3"></td>
            </tr>
          </tbody>
        </v-simple-table>
      </v-card-text>
    </v-card>
  </v-container>

  <v-dialog v-model="modalOpen" max-width="700px" style="background-color: white; backdrop-filter: 0;">
  <v-card>
    <v-card-title class="text-h5">Add Class</v-card-title>
    <v-card-text>
      <v-form>
        <v-text-field
  v-model="className"
  label="Class Name (e.g. CS426)"
  :rules="[() => !!className || 'Class name is required', () => isClassNameValid || 'Invalid class name format']"
  style="width: 350px;"
></v-text-field>
<v-text-field
  v-model="section"
  label="Section"
  :rules="[() => !!section || 'Section is required']"
  style="width: 100px;"
></v-text-field>
<v-text-field
  v-model="professor"
  label="Professor"
  :rules="[() => !!professor || 'Professor name is required']"
  style="width: 250px;"
></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-btn color="primary" @click="addClass" :disabled="!className || !section || !professor">Add</v-btn>
      <v-btn color="secondary" @click="() => (modalOpen = false)">Cancel</v-btn>
    </v-card-actions>
  </v-card>
</v-dialog>


</template>

<script>
import axios from "axios";
import { ref, computed } from "vue";
export default {
  name: "SuperUserDash",
  setup() {
    const posts = ref([]);
    const error = ref(null);
    axios
      .get("http://localhost:3000/posts")
      .then((response) => {
        posts.value = response.data;
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
    const modalOpen = ref(false);
    const className = ref("");
    const section = ref("");
    const professor = ref("");
    const isClassNameValid = computed(() => {
      const regex = /^[A-Za-z]{2,4}\d{3}$/;
      return regex.test(className.value);
    });
    const isFormValid = computed(() => {
      return (
        className.value !== "" && section.value !== "" && professor.value !== ""
      );
    });
    function openModal() {
      modalOpen.value = true;
    }
    function addClass() {
  if (isFormValid.value) {
    axios.post('http://localhost:3000/add_class', {
      class_name: className.value,
      section: section.value,
      professor: professor.value
    })
    .then(function (response) {
      console.log(response);
      modalOpen.value = false;
      className.value = "";
      section.value = "";
      professor.value = "";
    })
    .catch(function (error) {
      console.log(error);
    });
  } else {
    alert("Please fill out all fields before submitting");
  }
}
    return {
      posts,
      error,
      modalOpen,
      className,
      section,
      professor,
      openModal,
      addClass,
      isClassNameValid,
      isFormValid,
    };
  },
};
</script>



<style scoped>
.v-card {
  max-width: 80%;
  margin: 50px auto;
}
td {
  padding: 10px;
}
.v-btn {
  margin: 0 10px;
}
.text-right {
  text-align: right;
}
tbody tr {
  border-top: 1px solid lightgray;
}
.black {
  background-color: #000000;
}
</style>