
<template>
    <div>
      <super-nav-bar></super-nav-bar>
      <!-- Your other Vue components go here -->
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
        <tr v-for="item in filteredUsers" :key="item.name">
          <td class="border-black">{{ item.name }}</td>
          <td class="border-black">{{ item.section }}</td>
          <td class="border-black">{{ item.prof }}</td>

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
  import SuperNavBar from '@/components/SuperNavBar.vue'
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
        { name: 'CS425', section: '1234124', prof: 'Vinh Le' },
        { name: 'CS426', section: '43532', prof: 'Devrin Lee'},
        { name: 'CHS360', section: '234656', prof: 'Bob Burgers' },
        { name: 'CH201', section: '984958', prof: 'John Doe'},
      ],
    }),

    methods: {
      onClick () {
    this.loading = true
    setTimeout(() => {
      this.loading = false
      const searchText = this.$refs.searchInput.value.toLowerCase()
      this.filteredUsers = this.filteredUsers.filter(user => {
        return user.name.toLowerCase().includes(searchText) ||
               user.prof.toLowerCase().includes(searchText) ||
                user.section.toLowerCase().includes(searchText)
      })
    }, 2000)
  }
  },
      onButtonClicked (item) {
        // Implement your row action here
        console.log('Row clicked:', item)
      },
    components: {
      SuperNavBar
    }
  }
  </script>
