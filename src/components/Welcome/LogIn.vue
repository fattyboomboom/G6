<template>
  <!-- Heaer for out landing page -->
  <section class="header">
    <h1>WolfCampus</h1>
  </section>

  <!-- This is a pop up modal when the sign up button is pressed. -->
  <SignUp @close="toggleModal" :modalActive="modalActive">
    <v-card class="signupcard">
      <div class="modal-content">
        <form class="signupform">
          <v-row>
            <!--Text input for entering first name and trim any whitespace-->
            <v-text-field
              class="rounded-xl mt-5"
              label="First Name"
              v-model.trim="signup.firstname"
            ></v-text-field>

            <!--Text input for entering last name and trim any whitespace-->
            <v-text-field
              class="rounded-xl mt-5"
              label="Last Name"
              v-model.trim="signup.lastname"
            ></v-text-field>
          </v-row>

          <!--Text input for selecting a majors-->

          <v-row>
            <!-- sign up email input -->
            <v-text-field
              class="rounded-xl"
              v-model.trim="signup.email"
              :readonly="loading"
              prepend-inner-icon="mdi-email-outline"
              :rules="[required]"
              label="Email"
            ></v-text-field>

            <v-text-field
              class="rounded-xl"
              v-model.trim="signup.retryemail"
              :readonly="loading"
              prepend-inner-icon="mdi-email-outline"
              :rules="[required]"
              label="Re-enter email"
            ></v-text-field>
          </v-row>

          <v-row>
            <!-- sign up password input -->
            <v-text-field
              class="rounded-xl"
              type="password"
              v-model="signup.password"
              :rules="[required]"
              label="Password"
              prepend-inner-icon="mdi-lock-outline"
              placeholder="Enter your password"
            ></v-text-field>

            <v-text-field
              class="rounded-xl"
              type="password"
              v-model="signup.retrypassword"
              prepend-inner-icon="mdi-lock-outline"
              label="Re-enter password"
              placeholder="re-enter your password"
            ></v-text-field>
          </v-row>
          <v-autocomplete
            class="rounded-xl"
            label="majors"
            :items="majors"
            v-model="signup.majors"
          >
          </v-autocomplete>

          <!-- button to save form -->
          <v-btn
            class="saveNewButton rounded-pill"
            :disabled="!passwordsMatch || !emailsMatch"
            type="submit"
            variant="elevated"
            @click="createAccount"
          >
            Submit
          </v-btn>
        </form>
      </div>
    </v-card>
  </SignUp>

  <!-- log in card with a form to enter email and password -->
  <v-card class="logincard">
    <v-form class="formdetail">
      <!-- Input for log in email -->
      <v-text-field
        v-model="auth.email"
        class="rounded-xl"
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
        class="rounded-xl"
        placeholder="Enter your password"
      ></v-text-field>

      <br />

      <!-- button to submit log in information -->
      <v-btn
        class="signinbutton rounded-t-xl"
        color="success"
        size="large"
        type="submit"
        variant="elevated"
        @click.prevent="authuser"
        margin-t
      >
        Log In
      </v-btn>

      <!-- button to bring up sign up form -->
      <v-btn
        class="signupbutton rounded-b-xl"
        color="primary"
        size="large"
        variant="elevated"
        @click.prevent="toggleModal"
      >
        Sign Up
      </v-btn>
      <!-- <a href="" class="forgotpassword">Forgot password</a> -->
    </v-form>
  </v-card>
</template>

<script>
import SignUp from "./SignUp.vue";
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";
export default {
  name: "LogIn",
  components: {
    SignUp,
  },
  setup() {
    const modalActive = ref(false);
    const router = useRouter();
    const toggleModal = () => {
      modalActive.value = !modalActive.value;
    };
    return { modalActive, toggleModal, router };
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
        majors: "",
        email: "",
        retryemail: "",
        password: null,
        retrypassword: null,
        matchingPw: null,
      },
      majors: [
        "Accounting",
        "Acouting & Information Systems",
        "Agricultural Economics",
        "Agricultural Science",
        "Anthropology",
        "Art",
        "Art History",
        "Atmospheric Science",
        "Biochemistry and Molecular Biology",
        "Biology",
        "Biomedical Engineering",
        "Biotechnology",
        "Business",
        "Chemical Engineering",
        "Chemistry Civil Engineering Communication Studies",
        "Computer Science & Engineering",
        "Computational Linguistics",
        "Criminal Justice",
        "Dance",
        "Economics",
        "Elementary Education",
        "Electrical Engineering",
        "Engineering Physics",
        "English",
        "Environmental Engineering",
        "Environmental Science",
        "Finance",
        "Forest Ecology & Management",
        "French Gender",
        "Race & Identity",
        "General Studies",
        "Geography",
        "Geological Engineering",
        "Geology",
        "Geophysics",
        "History",
        "Human Development & Family Science",
        "Hydrogeology",
        "Information Systems",
        "International Affairs",
        "International Business",
        "Journalism",
        "Kinesiology",
        "Management",
        "Marketing",
        "Materials Science & Engineering",
        "Mathematics",
        "Mechanical Engineering",
        "Metallurgical Engineering",
        "Microbiology & Immunology",
        "Mining Engineering",
        "Music",
        "Neuroscience Nevadateach",
        "Nursing",
        "Nursing RN to BSN",
        "Nutrition",
        "Packteach",
        "Philosophy",
        "Physics",
        "Political Science",
        "Phychology",
        "Public Health",
        "Rangeland & Ecology & Management",
        "Secondary Education",
        "Social Work",
        "Sociology",
        "Spanish",
        "Speech Pathology",
        "Theatre",
        "Vetinary Science",
        "Wildlife Ecology & Conservation",
      ],
      loading: false,
      required: true,
    };
  },
  computed: {
    passwordsMatch() {
      return this.signup.password === this.signup.retrypassword;
    },
    emailsMatch() {
      return this.signup.email === this.signup.retryemail;
    },
  },
  methods: {
    // method for capturing data from form
    createAccount() {
        axios.post('http://localhost:3000/create_account', { email: this.signup.email })
          .then(response => {
            console.log(response.data)
          })
          .catch(error => {
            console.error(error)
            alert(error.response.data.message)
          })
      },
    saveNew() {
      var data = {
        firstname: this.signup.firstname,
        lastname: this.signup.lastname,
        majors: this.signup.majors.id,
        email: this.signup.email,
        password: this.signup.password,
      };
      // sending data
      axios
        .post("http://localhost:3000/signup", data)
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
        .post("http://localhost:3000/login", authdata)
        .then((response) => {
          console.log(response);
          console.log(authdata.email);
          if (response.status === 200) {
            this.router.push("/home");
          }
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
}
.v-text-field {
  background-color: #fdf0d5;
  /* border-radius: 15px; */
  font-size: 12px;
  display: block;
  line-height: 1.5;
  margin: 5%;
  padding: 0;
}
.v-btn {
  background-color: #669bbc;
  margin: 0 5% 5% 5%;
  width: 80%;
}
.submitsignup,
.signupbutton:hover,
.signinbutton:hover {
  scale: 1.1;
  background-color: #649fc4;
}
.submitsignup {
  width: 8%;
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
  background: #4a6fa5;
  color: #fdf0d5;
}
.v-card {
  box-shadow: 0 16px 56px rgba(0, 0, 0, 0.1), 0 16px 56px rgba(0, 0, 0, 0.1),
    0 16px 56px rgba(0, 0, 0, 0.1);
  border: none;
  border-radius: 20px;
  box-sizing: border-box;
  margin: 10%;
  width: 396px;
}
.logincard {
  width: 36%;
  margin-inline: 32%;
  text-align: center;
  background-color: #4a6fa5;
}
.formdetail {
  /* margin: 5%; */
  /* color: #FDF0D5; */
  /* background: #fff; */
  color: #1c1e21;
  direction: ltr;
  line-height: 1.34;
  margin: 0;
  padding: 0;
  unicode-bidi: embed;
}
.v-row {
  margin-inline: 5%;
  margin-top: 1%;
}
.forgotpassword {
  color: black;
}
.submitsignup {
  width: 70%;
  margin-inline: 15%;
}
.signupcard {
  width: 90%;
  margin-inline: 5%;
  height: 80%;
  background-color: #4a6fa5;
  align-items: center;
  margin-top: 10%;
}
.saveNewButton {
  width: 80%;
  margin-inline: 10%;
}
.forgotpassword:hover {
  font-size: large;
  color: green;
}
.error {
  color: red;
  margin-top: 0.5rem;
  position: absolute;
  z-index: auto;
}
.signuptextinput {
  margin-inline: 15%;
  width: 70%;
}
</style>