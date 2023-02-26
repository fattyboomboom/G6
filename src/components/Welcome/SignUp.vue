<template>
  <Transition name="modal-animation">
    <div v-show="modalActive" class="modal">
      <Transition name="modal-animation-inner">
        <div v-show="modalActive" class="modal-inner">
          <button @click="close">X</button>
          <slot />
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
  display: flex;
  /* align-items: center; */
}

button {
  position: fixed;
  text-align: right;
  color: red;
}
</style>
