<template>
  <v-container>
    <v-alert
      type="error"
      title="Error Submitting Post"
      closable
      close-label="Close"
      v-if="err"
      >{{ err }}</v-alert
    >
    <v-textarea
      clearable
      clear-icon="mdi-close-circle"
      label="Post to your wall"
      variant="outlined"
      no-resize=""
      v-model="inputValue"
    ></v-textarea>
    <v-btn @click="submitForm" variant="outlined">Submit</v-btn>
  </v-container>
</template>

<script>
import axios from "axios";
import ErrorService from "./services/uploadFile";
export default {
  name: "WallPost",
  data() {
    return {
      inputValue: "",
      msg: "",
      date: undefined,
      time: undefined,

      submitted: false,
      profanity: "",
      successCode: null,

      image: "",
      imageData: undefined,
    };
  },
  methods: {
    async submitForm() {
      if (!this.inputValue) {
        return;
      }

      //checks if submission is json
      this.parseJSON();
      //updates timestamps on every request
      this.getDate();

      const appendJSON = JSON.parse(this.inputValue);
      appendJSON.date = this.date;
      appendJSON.time = this.time;
      console.log(appendJSON);

      // const json = JSON.stringify({ post: this.inputValue, user: this.inputValue });
      await axios
        .post("http://127.0.0.1:5000/process", appendJSON, {
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          this.successCode = response.status;
          this.profanity = response.data.profanity;
          console.log(response);
        })
        .catch((err) => {
          let errorMessage = ErrorService.getErrorMessage(err.response.status);
          this.err = errorMessage;
          console.log(errorMessage);

          setTimeout(() => {
            this.err = "";
          }, 2000);
        });
      this.submitted = this.inputValue;
      this.inputValue = "";
    },

    parseJSON() {
      try {
        JSON.parse(this.submitted);
        JSON.parse(this.inputValue);
      } catch (error) {
        console.error("Invalid input", error);
      }
    },

    //function that retrieves current timestamps using local format
    getDate() {
      const options = {
        hour12: true, // use 12-hour clock
        hour: "numeric",
        minute: "numeric",
      };
      var currentDate = new Date();

      this.date = currentDate.toLocaleDateString("en-US");
      this.time = currentDate.toLocaleTimeString("en-US", options);
    },
  },
};
</script>

<style scoped>
.v-container {
  width: 40%;

  /* margin-right: 25%; */
  margin-left: 35%;
}
</style>
