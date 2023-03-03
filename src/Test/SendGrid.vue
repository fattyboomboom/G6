<!-- npm install axios -->

<template>
    <div>
      <v-text-field v-model="email" label="Email"></v-text-field>
      <v-btn @click="createAccount">Create Account</v-btn>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        email: ''
      }
    },
    methods: {
      createAccount() {
        axios.post('http://localhost:3000/create_account', { email: this.email })
          .then(response => {
            console.log(response.data)
          })
          .catch(error => {
            console.error(error)
            alert(error.response.data.message)
          })
      }
    }
  }
  </script>