<template>
  <v-app>
    <v-container>
      <v-form @submit.prevent="submitForm">
        <v-text-field v-model="inputValue" label="Type your submission here" />
        <v-btn type="submit" color="primary">Submit</v-btn>
      </v-form>
      <p class="mt-12" v-if="submitted">Your submission: {{ submitted }}</p>
      <p class="mt-12" v-if="submitted">Profanity: {{ profanity }} </p>
    </v-container>
  </v-app>
</template>

<script>
import axios from 'axios';
 
export default {
  data() {
    return {
      inputValue: "",
      msg: "",
      submitted: false,
      profanity: ""
    };
  },
  methods: {
    //POST Function
   async submitForm() {
    await axios.post('http://127.0.0.1:5000/process', this.inputValue)
    .then(response => {
      console.log(response)
      this.profanity = response.data.profanity
    })
    .catch(err => console.error(err));
    this.submitted = this.inputValue;
    this.inputValue = '';

    },
    // //GET Function
    // const async getData() {
    //   axios.get('http://127.0.0.1:5000/process')
    //   .then(response => {
    //     this.profanity = response.data.profanity;
    //   })
    //   .catch(err => console.error(err));
    // }

  },
  created() {
    this.submitForm();
  }
};
</script>
