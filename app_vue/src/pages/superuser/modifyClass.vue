
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
        <tr v-for="item in filteredUsers" :key="item.name"> 
          <td class="border-black">{{ item.name }}</td> 
          <td class="border-black">{{ item.lastName }}</td> 
          <td class="border-black">{{ item.email }}</td> 
          <td class="border-black">{{ item.lastLogin }}</td> 
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
        { text: 'Email', value: 'email' }, 
        { text: 'Last LogIn', value: 'lastLogin' }, 
      ], 
      users: [ 
        { name: 'John', lastName:'Doe', email: 'john.doe@example.com', lastLogin: '4/2/2023' }, 
        { name: 'Jane', lastName: 'Doe', email: 'jane.doe@example.com', lastLogin: '3/28/2023' }, 
        { name: 'Bob', lastName: 'Smith', email: 'bob.smith@example.com', lastLogin: '3/30/2023' }, 
      ], 
      filteredUsers: [], 
    }), 
   
    methods: { 
      onClick () { 
    this.loading = true 
    setTimeout(() => { 
      this.loading = false 
      const searchText = this.$refs.searchInput.value.toLowerCase() 
      this.filteredUsers = this.users.filter(user => { 
        return user.name.toLowerCase().includes(searchText) || 
               user.email.toLowerCase().includes(searchText) 
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