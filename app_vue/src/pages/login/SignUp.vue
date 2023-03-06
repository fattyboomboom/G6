<template>
  <Transition name="modal-animation">
    <!-- The modal class sets the background color -->
    <div v-show="modalActive" class="modal">
      <Transition name="modal-animation-inner">
        <!-- sets a white background behind the form -->
        <div v-show="modalActive" class="modal-inner">
          <!-- closes the modal and this is where the content of the slot on longin.vue is inserted -->
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
  background: #FDF0D5;
  display: flex;
  width: 50%;
  border: none;
  border-radius: 20px;
  height: 70%;
  margin: 20%;
  /* align-items: center; */
}
button {
  position: fixed;
  text-align: right;
  color: red;
}
</style>