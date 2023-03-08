<template>
  <!-- Heaer for out landing page -->
  <section class="header">
    <h1 >WolfCampus</h1>
  </section>

  <!-- This is a pop up modal when the sign up button is pressed. -->
  <SignUp @close="toggleModal" :modalActive="modalActive">
    <v-card class="">
      <div class="modal-content">
        <form class="signupform">
          <!--Text input for entering first name and trim any whitespace-->
          <v-text-field
            class="rounded-xl"
            label="First Name"
            v-model.trim="signup.name"
            :readonly="loading"
            :rules="[required]"
          ></v-text-field>

          <!--Text input for entering last name and trim any whitespace-->
          <v-text-field
            class="rounded-xl"
            label="Last Name"
            v-model.trim="signup.last_name"
          ></v-text-field>

          <!--Text input for selecting a major-->
          <v-autocomplete
            class="rounded-xl"
            label="Major"
            :items="major"
            transition="fab-transition"
            v-model="signup.major"
          >
          </v-autocomplete>

          <!-- sign up email input -->
          <v-text-field
            class="rounded-xl"
            v-model.trim="signup.email"
            :readonly="loading"
            :rules="[required]"
        
            label="Email"
          ></v-text-field>

          <v-text-field
            class="rounded-xl"
            v-model.trim="signup.email"
            :readonly="loading"
            :rules="[required]"
            
            label="Re-enter email"
          ></v-text-field>

          <!-- sign up password input -->
          <v-text-field
            class="rounded-xl"
            type="password"
            v-model="signup.password"
            :rules="[required]"
            label="Password"
            placeholder="Enter your password"
          ></v-text-field>

          <v-text-field
            class="rounded-xl"
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
            class="signinbutton rounded-pill"
            color="success"
            size="large"
            type="submit"
            variant="elevated"
            @click.prevent="saveNew"
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
      >
        Sign In
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
        name: null,
        last_name: "",
        major: null,
        email: "",
        retryemail: "",
        password: "",
        retrypassword: "",
      },
      major: [
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
      required: false,
    };
  },
  methods: {
    // method for capturing data from form
    saveNew() {
      var data = {
        name: this.signup.name,
        last_name: this.signup.last_name,
        major: this.signup.major,
        email: this.signup.email,
        password: this.signup.password,
      };
      // sending data
      axios
        .post("http://localhost:5000/api/user", data)
        .then((response) => {
          console.log(response);
          if (response.status === 201){
            this.modalActive = false;
          }
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
          if (response.status === 200) {
            this.router.push("/dashboard");
          }
          if (response.status === 201) {
            this.router.push("/dashboard");
          }
          if (response.status === 202) {
            this.router.push("/superuser");
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
  font-family: cursive;
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
  background-color: #669BBC;
  margin: 0 5% 5% 5%;
  width: 80%;
}
.signupbutton:hover,
.signinbutton:hover {
  scale: 1.1;
  background-color: #649FC4;
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
  background: #003049;
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
  width: 35%;
  margin-left: 30%;
  text-align: center;
  background-color: #003049;
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
