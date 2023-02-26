<template>
  <Transition name="modal-animation">
    <div v-show="modalActive" class="modal">
      <Transition name="modal-animation-inner">
        <div v-show="modalActive" class="modal-inner">
          <slot />
          <v-card border>
      <div class="modal-content">
        <form>
          <v-text-field label="First Name"></v-text-field>
          <v-text-field label="Last Name"></v-text-field>
          <v-text-field label="Major"></v-text-field>
          <v-text-field v-model="date" label="Date of Birth"></v-text-field>
          <v-text-field
            v-model="email"
            :readonly="loading"
            :rules="[required]"
            class="mb-2"
            label="Email"
          ></v-text-field>
          <v-text-field
            type="password"
            v-model="password"
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
          >
            Submit
          </v-btn>
        </form>
      </div>
    </v-card>
          <button @click="close">Close</button>
        </div>
      </Transition>
    </div>
  </Transition>
</template>

<script>
export default {
  name: "SignUp",
  props: ["modalActive"],
  //   data: () => ({
  //     first: null,
  //     last: null,
  //     email: null,
  //     password: null,
  //     terms: false,
  //   }),
  setup(props, { emit }) {
    const close = () => {
      emit("close");
    };

    return { close };
  },
};
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 99;
  background-color: rgb(65, 65, 65);

  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-inner {
  background: white;
  width: 40%;
}
</style>
