<template>
  <v-app>
    <v-container>
      <v-form @submit.prevent="submitForm">
        <v-alert        
        type="error"
        title="Error Submitting Post"
        closable
        close-label="Close"
        v-if="err">{{ err }}</v-alert>
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
import ErrorService from './services/uploadFile'

export default {
  data() {
    return {
      inputValue: "",
      msg: "",
      submitted: false,
      profanity: "",
      successCode: null,
    };
  },
  methods: {
    //POST Function
   async submitForm() {
    if (!this.inputValue) {
      return;
    }

    const json = JSON.stringify({ post: this.inputValue})
    await axios.post('http://127.0.0.1:5000/process', json, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => {
      this.successCode = response.status
      this.profanity = response.data.profanity
      console.log(response)
    })
    .catch((err) => {
      let errorMessage = ErrorService.getErrorMessage(
        err.response.status,
      );
      this.err=errorMessage;
      console.log(errorMessage);

      setTimeout(() => {
        this.err='';
      }, 2000);

    });
    this.submitted = this.inputValue;
    this.inputValue = '';
    },
  },
  created() {
    if (!this.submitted) {
    this.submitForm();
    }
  }
};
</script>