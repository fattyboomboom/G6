
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
          label="Search users by name or email"
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
          Last Name
        </th>
        <th class="text-left">
          Email
        </th>
        <th class="text-left">
          Last LogIn
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="users in users" :key="users.uid">
        <!-- <td class="border-black">{{ users.FirstName }}</td>
        <td class="border-black">{{ users.LastName }}</td> -->
        <td class="border-black">{{ users.AcctEmail }}</td>
        <td class="border-black">{{ formatDistanceToNow(users.LastLogin) }}</td>
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
import { collection, query, getDocs } from "firebase/firestore";
import { db } from "@/firebase";
import { formatDistanceToNow } from "date-fns";

export default {
    data: () => ({
    loaded: false,
    loading: false,
    headers: [
      { text: 'Name', value: 'name' },
      { text: 'Email', value: 'email' },
      { text: 'Last LogIn', value: 'lastLogin' },
    ],
    filteredUsers: [
      // { name: 'John', lastName:'Doe', email: 'john.doe@example.com', lastLogin: '4/2/2023' },
      // { name: 'Jane', lastName: 'Doe', email: 'jane.doe@example.com', lastLogin: '3/28/2023' },
      // { name: 'Bob', lastName: 'Smith', email: 'bob.smith@example.com', lastLogin: '3/30/2023' },
    ],

    
  }),

  setup() {
    const users = ref([]);
    const error = ref(null);

    const fetchUsers = async () => {
      try {
        const postRef = collection(db, "accounts");
        const q = query(postRef);
        const querySnapshot = await getDocs(q);
        const usersArray = querySnapshot.docs.map((doc) => ({
          id: doc.id,
          ...doc.data(),
        }));
        users.value = usersArray;
        console.log(users.value);
      } catch (err) {
        error.value = err.message;
      }
    };

    onMounted(() => {
      fetchUsers();
    });

    return { users, error };
  },

  methods: {
    formatTime(timestamp) {
      const date = timestamp.toDate();
      const hours = date.getHours();
      const minutes = date.getMinutes().toString().padStart(2, "0");
      const ampm = hours >= 12 ? "PM" : "AM";
      const twelveHours = hours % 12 || 12;
      return `${twelveHours}:${minutes} ${ampm}`;
    },

    formatDate(timestamp) {
      const date = timestamp.toDate();
      const options = { month: "short", day: "numeric", year: "2-digit" };
      return new Intl.DateTimeFormat("en-US", options).format(date);
    },

    formatDistanceToNow(timestamp) {
      const date = timestamp.toDate();
      return formatDistanceToNow(date);
    },
  },
  computed: {
    displayedPosts() {
      return this.posts.slice(0, this.maxPosts);
    },
  },
}


//   methods: {
//     onClick () {
//   this.loading = true
//   setTimeout(() => {
//     this.loading = false
//     const searchText = this.$refs.searchInput.value.toLowerCase()
//     this.filteredUsers = this.filteredUsers.filter(user => {
//       return user.name.toLowerCase().includes(searchText) ||
//              user.email.toLowerCase().includes(searchText)
//     })
//   }, 2000)
// }
// },
//     onButtonClicked (item) {
      
//       console.log('Row clicked:', item)
//     },

// }
</script>
