<template>
  <v-form class="d-flex flex-column align-center">
  <v-col cols="12" md="6">
    <v-text-field v-model="recipient" label="Recipient Email" class="mt-8"></v-text-field>
  </v-col>
    <v-btn color="primary" class="mx-auto mt-8" @click="send">Send Email</v-btn>
  </v-form>
</template>

<script>
import { sendEmail } from '../../utilities/AmazonSES';

export default {
  data() {
    return {
      recipient: '',
      subject: 'Your Subject Here',
      message: 'Your Message Here'
    };
  },
  methods: {
    async send() {
      try {
        await sendEmail(this.recipient, this.subject, this.message);
        alert('Email sent successfully!');
      } catch (error) {
        console.error(error);
        alert('Error sending email!');
      }
    }
  }
};
</script>

<style scoped>
.v-text-field {
  max-width: 400px; /* adjust as needed */
}
</style> 
