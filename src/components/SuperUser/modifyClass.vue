
<template>
    <div>
    
      <v-sheet
              :class="[computedMargin]"
              elevation="4"
              rounded
            >
      <v-card
        class="mx-auto"
        color="grey-lighten-3"
        max-width="400"
      >
        <v-card-text>
          <v-text-field
          ref="searchInput"
            :loading="loading"
            density="default"
            variant="solo"
            label="Search class by name, section or prof"
            append-inner-icon="mdi-magnify"
            single-line
            hide-details
            @click:append-inner="onClick"
          ></v-text-field>
        </v-card-text>
      </v-card>
      </v-sheet>
    </div>
      <v-table style="margin-left: 3.5rem;">
      <thead>
        <tr>
          <th class="text-left">
            Name
          </th>
          <th class="text-left">
            Section
          </th>
          <th class="text-left">
            Professor
          </th>

        </tr>
      </thead>
      <tbody>
        <tr v-for="clas in classes" :key="clas.uid">
          <td class="border-black">{{ clas.prefix }}</td>
          <!-- <td class="border-black">{{ clas.section }}</td> -->
          <!-- <td class="border-black">{{ clas.prof }}</td> -->

          <td class="border-black">
              <v-btn color="indigo" @click="onButtonClicked(item)">
                Modify
              </v-btn>
            </td>
            <td class="border-black">
              <v-btn color="error" @click="onButtonClicked(item)">
                Delete
              </v-btn>
            </td>
        </tr>
      </tbody>
    </v-table>

  </template>

  <script>
import { ref, onMounted } from "vue";
import { collection, query, where, getDocs,limit } from "firebase/firestore";
import { db } from "@/firebase";

  
  export default {
      data: () => ({
      loaded: false,
      loading: false,
      headers: [
        { text: 'Name', value: 'name' },
        { text: 'Section', value: 'section' },
        { text: 'Professor', value: 'prof' },
      ],
      filteredUsers: [
        //{ name: 'CS425', section: '1234124', prof: 'Vinh Le' },
        //{ name: 'CS426', section: '43532', prof: 'Devrin Lee'},
        //{ name: 'CHS360', section: '234656', prof: 'Bob Burgers' },
        //{ name: 'CH201', section: '984958', prof: 'John Doe'},
      ],
    }),

    setup() {
    const classes = ref([]);
    const error = ref(null);

    const fetchClas = async () => {
      try {
        const postRef = collection(db, "classes");
        const q = query(postRef,where("moderatorUID", "==", ""),where("students", "!=", ""),limit(10));
        const querySnapshot = await getDocs(q);
        const clasArray = querySnapshot.docs.map((doc) => ({
          id: doc.id,
          ...doc.data(),
        }));
        classes.value = clasArray;
        console.log(classes.value);
      } catch (err) {
        error.value = err.message;
      }
    };

    onMounted(() => {
      fetchClas();
    });

    return { classes, error };
  },
    //methods: {
     // onClick () {
    //this.loading = true
    //setTimeout(() => {
     // this.loading = false
     // const searchText = this.$refs.searchInput.value.toLowerCase()
      //this.filteredUsers = this.filteredUsers.filter(user => {
        //return user.name.toLowerCase().includes(searchText) ||
          //     user.prof.toLowerCase().includes(searchText) ||
            //    user.section.toLowerCase().includes(searchText)
      //})
    //}, 2000)
  //}
  //},
    //  onButtonClicked (item) {
        // Implement your row action here
      //  console.log('Row clicked:', item)
      //},
  
  }
  </script>
