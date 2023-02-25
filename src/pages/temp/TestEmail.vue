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







<!-- <template>
    <v-btn color="primary" class="mx-auto mt-8" @click="send">Send Email</v-btn>
  </template>
  
  <script>
  import AWS from 'aws-sdk';
  
  export default {
    methods: {
      async send() {
        AWS.config.update({
          accessKeyId: 'AKIAZ6IIAQRWTCGQQWEA',
          secretAccessKey: 'R1+MVSPmeoLuo0YdCvUy7N/xMEHfdAzmu0WiSYZO',
          region: 'us-west-2' // replace with your desired region
        });
  
        const params = {
          Destination: {
            ToAddresses: ['clintv619@gmail.com']
          },
          Message: {
            Body: {
              Html: {
                Charset: 'UTF-8',
                Data: 'This is a test'
              }
            },
            Subject: {
              Charset: 'UTF-8',
              Data: 'Test'
            }
          },
          Source: 'WolfCampus <clintv@nevada.unr.edu>'
        };
  
        try {
          const sendPromise = new AWS.SES({ apiVersion: '2010-12-01' }).sendEmail(params).promise();
          await sendPromise;
          alert('Email sent successfully!');
        } catch (err) {
          console.error(err);
          alert(`An error occurred while sending the email: ${err.message}`);
        }
      }
    }
  };
  </script> -->