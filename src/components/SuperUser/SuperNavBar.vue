<template>


        <v-card>
          <v-card-title class="bg-homebanner d-flex justify-space-between">
            <v-spacer></v-spacer>
            <span class="text-center">Super User</span>

            <v-spacer></v-spacer>

            <v-menu>

              <template v-slot:activator="{ props }">
                <v-btn variant= "text" v-bind="props">Class</v-btn>
              </template>

              <v-list>
                <v-list-item
                title="Add"
                value="addclass"
                @click="openModal"
                ></v-list-item>
                <v-list-item
                title="Modify"
                value="modclass"
                to="/modifclass"
                ></v-list-item>
              </v-list>
            </v-menu>
             <v-menu>
              <template v-slot:activator="{ props }">
                <v-btn variant= "text" v-bind="props">User</v-btn>
              </template>
                 <v-list>
                <v-list-item
                title="Add"
                value="adduser"
                @click="openUserModal"
                ></v-list-item>
                <v-list-item
                title="Modify"
                value="moduser"
                to="/modifuser"
                ></v-list-item>
              </v-list>
            </v-menu>
            <v-btn variant= "text" to="/reports" >Review reports</v-btn>
          </v-card-title>
        </v-card>
\
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
<v-dialog v-model="modalUserOpen" max-width="700px" style="background-color: white; backdrop-filter: 0;">
  <v-card>
    <v-card-title class="text-h5">Add User</v-card-title>
    <v-card-text>
      <v-form>
        <v-text-field
  v-model="name"
  label="User Name"
  :rules="[() => !!name || 'User name is required', () => isClassNameValid || 'Invalid name format']"
  style="width: 350px;"
></v-text-field>
<v-text-field
  v-model="lastName"
  label="User Last Name"
  :rules="[() => !!lastName || 'User last name is required', () => isClassNameValid || 'Invalid last name format']"
  style="width: 350px;"
></v-text-field>
<v-text-field
  v-model="email"
  label="Email"
  :rules="[() => !!email || 'Email is required']"
  style="width: 100px;"
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
    const modalUserOpen = ref(false);
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
    function openUserModal() {
      modalUserOpen.value = true;
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
      openUserModal,
      isClassNameValid,
      isFormValid,
    };
  },
};
  </script>
<style>
.text-center {
  margin-left: 23%;
}
</style>
