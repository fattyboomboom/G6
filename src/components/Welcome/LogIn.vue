<template>
  <section class="header">
    <h1>WolfCampus</h1>
  </section>

  <v-card class="logincard"  border>
    <v-form v-model="form" @submit.prevent="onSubmit">
      <v-text-field
        v-model="email"
        :readonly="loading"
        :rules="[required]"
        class="mb-2"
        clearable
        label="Emailed"
      ></v-text-field>

      <v-text-field
        type="password"
        v-model="password"
        :rules="[required]"
        clearable
        label="Password"
        placeholder="Enter your password"
      ></v-text-field>

      <br />

      <v-btn
        :loading="loading"
        block
        color="success"
        size="large"
        type="submit"
        variant="elevated"
      >
        Sign In
      </v-btn>
    </v-form>
    <SignUp>
      <v-btn
        class="mt-4"
        block
        color="primary"
        size="large"
        variant="elevated"
        @click="onSignUpClick"
      >
        Sign Up
      </v-btn>
    </SignUp>
  </v-card>
</template>

<script>
// import { ref } from 'vue';
import SignUp from "./SignUp.vue";

export default {
  setup() {
    // const popupTriggers = ref({
    //   buttonTrigger: false,
    // });

    return {
      SignUp,
    };
  },
  name: "LogIn",

  data: () => ({
    form: false,
    email: null,
    password: null,
    loading: false,
  }),

  methods: {
    onSubmit() {
      if (!this.form) return;

      this.loading = true;

      setTimeout(() => (this.loading = false), 2000);
    },
    required(v) {
      return !!v || "Field is required";
    },
    onSignUpClick() {
      console.log("Sign up button clicked");
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
  border-color: #000000;
  margin: 10%;
}
.logincard {
  width:35%;
  margin-left: 30%;
  
}
</style>
