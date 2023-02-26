<template>
  <!-- Heaer for out landing page -->
  <section class="header">
    <h1>WolfCampus</h1>
  </section>

  <!-- This is a pop up modal when the sign up button is pressed. -->
  <SignUp @close="toggleModal" :modalActive="modalActive">
    <v-card border>
      <div class="modal-content">
        <form>
          <!--Text input for entering first name and trim any whitespace-->
          <v-text-field
            label="First Name"
            v-model.trim="signup.firstname"
          ></v-text-field>

          <!--Text input for entering last name and trim any whitespace-->
          <v-text-field
            label="Last Name"
            v-model.trim="signup.lastname"
          ></v-text-field>

          <!--Text input for entering date of birth and trim any whitespace-->
          <v-text-field label="Major" v-model="signup.major"></v-text-field>
          <v-text-field
            v-model="signup.dob"
            label="Date of Birth"
          ></v-text-field>

          <v-text-field
            v-model.trim="signup.email"
            :readonly="loading"
            :rules="[required]"
            class="mb-2"
            label="Email"
          ></v-text-field>

          <v-text-field
            type="password"
            v-model="signup.password"
            :rules="[required]"
            label="Password"
            placeholder="Enter your password"
          ></v-text-field>

          <v-btn
            :loading="loading"
            block
            color="success"
            size="large"
            type="submit"
            variant="elevated"
            @click="saveNew"
          >
            Submit
          </v-btn>
        </form>
      </div>
    </v-card>
  </SignUp>

  <!-- log in card with a form to enter email and password -->
  <v-card class="logincard" border>
    <v-form class="formdetail">
      <!-- Input for log in email -->
      <v-text-field
        v-model="auth.email"
        class="mb-2"
        label="Email"
        placeholder="NetID@nevada.unr.edu"
      ></v-text-field>

      <!-- input for login password -->
      <v-text-field
        type="password"
        v-model="auth.password"
        :rules="[required]"
        label="Password"
        placeholder="Enter your password"
      ></v-text-field>

      <br />

      <!-- button to submit log in information -->
      <v-btn
        block
        color="success"
        size="large"
        type="submit"
        variant="elevated"
        @click="authuser"
      >
        Sign In
      </v-btn>

      <!-- button to bring up sign up form -->
      <v-btn
        class="mt-4"
        block
        color="primary"
        size="large"
        variant="elevated"
        @click="toggleModal"
      >
        Sign Up
      </v-btn>
    </v-form>
  </v-card>
</template>

<script>
import SignUp from "./SignUp.vue";
import { ref } from "vue";
import axios from "axios";

export default {
  name: "LogIn",
  components: {
    SignUp,
  },
  setup() {
    const modalActive = ref(false);

    const toggleModal = () => {
      modalActive.value = !modalActive.value;
    };

    return { modalActive, toggleModal };
  },

  data: () => {
    return {
      // Data properties for authentication
      auth: {
        email: null,
        password: null,
      },

      // Data properties for sign up
      signup: {
        firstname: "",
        lastname: "",
        major: "",
        dob: "",
        email: "",
        password: "",
      },

      loading: false,
      required: true,
    };
  },

  methods: {
    // method for capturing data from form
    saveNew() {
      var data = {
        firstname: this.signup.firstname,
        lastname: this.signup.lastname,
        major: this.signup.major,
        dob: this.signup.dob,
        email: this.signup.email,
        password: this.signup.password,
      };

      // sending data
      axios
        .post("http://localhost:3000/signup", data)
        .then(function (response) {
          console.log(response);
        });
    },

    // capturing data from log in form
    authuser() {
      var authdata = {
        email: this.auth.email,
        password: this.auth.password,
      };

      // sending data
      axios
        .post("http://localhost:3000/login", authdata)
        .then(function (response) {
          console.log(response);
        });
    },
  },
};
</script>

<style scoped>
h1,
p,
a {
  margin: 0;
  padding: 0;
  font-family: cursive;
}

h1 {
  font-size: 2.8em;
  padding: 10px 0;
  font-weight: 800;
}

p {
  font-size: 1.1em;
  font-weight: 100;
  letter-spacing: 5px;
}

.header {
  width: 100%;
  /* padding: 60px 0; */
  text-align: center;
  background: #000000;
  color: white;
}
.v-card {
  box-shadow: 0 16px 56px rgba(0, 0, 0, 0.1), 0 16px 56px rgba(0, 0, 0, 0.1),
    0 16px 56px rgba(0, 0, 0, 0.1);
  border: none;
  border-radius: 20px;
  box-sizing: border-box;
  margin: 10%;
  background-color: whitesmoke;
  width: 396px;
}
.logincard {
  width: 35%;
  margin-left: 30%;
  text-align: center;
}

.formdetail {
  margin: 5%;
}
</style>
