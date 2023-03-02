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

          <!--Text input for selecting a major-->
          <v-autocomplete label="Major" :items="major" v-model="signup.major">
          </v-autocomplete>

          <!-- sign up email input -->
          <v-text-field
            v-model.trim="signup.email"
            :readonly="loading"
            :rules="[required]"
            class="mb-2"
            label="Email"
          ></v-text-field>

          <v-text-field
            v-model.trim="signup.email"
            :readonly="loading"
            :rules="[required]"
            class="mb-2"
            label="Re-enter email"
          ></v-text-field>

          <!-- sign up password input -->
          <v-text-field
            type="password"
            v-model="signup.password"
            :rules="[required]"
            label="Password"
            placeholder="Enter your password"
          ></v-text-field>

          <v-text-field
            type="password"
            v-model="signup.password"
            :rules="[required]"
            label="Re-enter password"
            placeholder="re-enter your password"
          ></v-text-field>

          <!-- button to save form -->
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
        prepend-inner-icon="mdi-email-outline"
        placeholder="NetID@nevada.unr.edu"
      ></v-text-field>

      

      <!-- input for login password -->
      <v-text-field
        type="password"
        v-model="auth.password"
        :rules="[required]"
        prepend-inner-icon="mdi-lock-outline"
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
        @click.prevent="authuser"
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
      <a href="" class="forgotpassword">Forgot password</a>
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
        email: "",
        retryemail: "",
        password: "",
        retrypassword: ""
      },
      major: [
        "accounting",
        "acouting & information systems",
        "agricultural economics",
        "agricultural science",
        "anthropology",
        "art",
        "art history",
        "atmospheric science",
        "biochemistry and molecular biology",
        "biology",
        "biomedical engineering",
        "biotechnology",
        "business",
        "chemical engineering",
        "chemistry civil engineering communication studies",
        "computer science & engineering",
        "computational linguistics",
        "criminal justice",
        "dance",
        "economics",
        "elementary education",
        "electrical engineering",
        "engineering physics",
        "english",
        "environmental engineering",
        "environmental science",
        "finance",
        "forest ecology & management",
        "french gender",
        "race & identity",
        "general studies",
        "geography",
        "geological engineering",
        "geology",
        "geophysics",
        "history",
        "human development & family science",
        "hydrogeology",
        "information systems",
        "international affairs",
        "international business",
        "journalism",
        "kinesiology",
        "management",
        "marketing",
        "materials science & engineering",
        "mathematics",
        "mechanical engineering",
        "metallurgical engineering",
        "microbiology & immunology",
        "mining engineering",
        "music",
        "neuroscience nevadateach",
        "nursing",
        "nursing rn to bsn",
        "nutrition",
        "packteach",
        "philosophy",
        "physics",
        "political science",
        "phychology",
        "public health",
        "rangeland & ecology & management",
        "secondary education",
        "social work",
        "sociology",
        "spanish",
        "speech pathology",
        "theatre",
        "betinary science",
        "wildlife ecology & conservation",
      ],
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
        email: this.signup.email,
        password: this.signup.password,
       
      };
      // sending data FOR NEW USER
      axios
        .put("http://localhost:5000/api/account", data)
        .then((response) => {
          console.log(response);
         
        })
        .catch((error) => {
          console.log(error);
          
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
        .put("http://localhost:5000/api/account", authdata)
        .then((response) => {
          console.log(response);
          console.log(authdata.email);
          console.log(authdata.password);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
p,
a {
  margin: 0;
  padding: 0;
}
h1 {
  font-size: 2.8em;
  padding: 10px 0;
  font-weight: 800;
  font-family: cursive;
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
.forgotpassword {
  color: black;
}
.modal-content {
  height: 8%;
}
.forgotpassword:hover {
  font-size: large;
  color: green;
}
@keyframes mymove {
  from {
    left: 0px;
  }
  to {
    left: 200px;
  }
}
</style>