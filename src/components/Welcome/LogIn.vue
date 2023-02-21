<template>
  <section class="header">
    <h1>WolfCampus</h1>
  </section>

  <SignUp @close="toggleModal" :modalActive="modalActive">
    <v-card border>
      <div class="modal-content">
        <form>
          <v-text-field class="" label=" First Name"></v-text-field>
          <v-text-field class="mb-2" label="First Name"></v-text-field>
          <v-text-field class="mb-2" label="Major"></v-text-field>
          <v-text-field class="mb-2" label="Date of Birth"></v-text-field>
          <v-text-field label="E-mail"></v-text-field>
          <v-btn
            :loading="loading"
            block
            color="success"
            size="large"
            type="submit"
            variant="elevated"
          >
            Submit
          </v-btn>
        </form>
      </div>
    </v-card>
  </SignUp>

  <v-card class="logincard" border>
    <v-form v-model="form" @submit.prevent="onSubmit">
      <v-text-field
        v-model="email"
        :readonly="loading"
        :rules="[required]"
        class="mb-2"
        clearable
        label="Email"
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
  </v-card>
</template>

<script>
// import { ref } from 'vue';
import SignUp from "./SignUp.vue";
import { ref } from "vue";

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
};

//   data: () => ({
//     form: false,
//     email: null,
//     password: null,
//     loading: false,
//   }),

//   methods: {
//     onSubmit() {
//       if (!this.form) return;

//       this.loading = true;

//       setTimeout(() => (this.loading = false), 2000);
//     },
//     required(v) {
//       return !!v || "Field is required";
//     },
//     onSignUpClick() {
//       console.log("Sign up button clicked");
//     },
//   },
// };
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
  width: 35%;
  margin-left: 30%;
}
.modal-content {
  width: 50%;
}
</style>
