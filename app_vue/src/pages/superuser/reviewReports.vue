<template>

  <super-nav-bar></super-nav-bar>

<v-container fluid>
  <v-card>
    <v-card-title class="mb-2">Reported Posts</v-card-title>
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
              <v-btn color="indigo">Repeal</v-btn>
              <v-btn color="red" class="mr-3">Delete</v-btn>

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

</template>

<script>
// import axios from "axios";
// import { ref, computed } from "vue";
export default {
name: "SuperUserDash",
data: () => ({
posts: [
    { id: '23', author:'Bob', date: '4/2/2023', content: 'Hi, my name is Bob' },
    { id: '34', author: 'john', date: '3/28/2023', content: 'Hi, my name is john' },
    { id: '31', author: 'jane', date: '3/30/2023', content: 'Hi, my name is jane' },
  ],
}),
//   setup() {
//     const posts = ref([]);
//     const error = ref(null);
//     axios
//       .get("http://localhost:3000/posts")
//       .then((response) => {
//         posts.value = response.data;
//         console.log(response.data);
//       })
//       .catch((error) => {
//         console.log(error);
//       });
//     const modalOpen = ref(false);
//     const className = ref("");
//     const section = ref("");
//     const professor = ref("");
//     const isClassNameValid = computed(() => {
//       const regex = /^[A-Za-z]{2,4}\d{3}$/;
//       return regex.test(className.value);
//     });
//     const isFormValid = computed(() => {
//       return (
//         className.value !== "" && section.value !== "" && professor.value !== ""
//       );
//     });
//     function openModal() {
//       modalOpen.value = true;
//     }
//     function addClass() {
//   if (isFormValid.value) {
//     axios.post('http://localhost:3000/add_class', {
//       class_name: className.value,
//       section: section.value,
//       professor: professor.value
//     })
//     .then(function (response) {
//       console.log(response);
//       modalOpen.value = false;
//       className.value = "";
//       section.value = "";
//       professor.value = "";
//     })
//     .catch(function (error) {
//       console.log(error);
//     });
//   } else {
//     alert("Please fill out all fields before submitting");
//   }
// }
//   return {
//     posts,
//     error,
//     modalOpen,
//     className,
//     section,
//     professor,
//     openModal,
//     addClass,
//     isClassNameValid,
//     isFormValid,
//   };
// },
};
</script>



<style scoped>
.v-card {
max-width: 80%;
margin: 5px auto;
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
