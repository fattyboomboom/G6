<template>
  <Transition name="modal-animation">
    <!-- The modal class sets the background color -->
    <div v-show="modalActive" class="modal">
      <Transition name="modal-animation-inner">
        <!-- sets a white background behind the form -->
        <div v-show="modalActive" class="modal-inner">
          <!-- closes the modal and this is where the content of the slot on longin.vue is inserted -->
        <v-btn @click="$emit('close')" append-icon="mdi-close-box-outline" variant="flat"
      color="error"></v-btn>
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
  background: #e0e1dd;
  width: 60%;
  border: none;
  height: 98%;
  /* margin: 20%; */
  align-items: center;
}

button {
  position: fixed;
  margin-left: 50%;
  margin-top: 1%;
  transform: scale(1.5);
  color: red;


 
  transition: all 0.3s ease;
} 

button:hover {
  color: red;
  transform: scale(2);
}
</style>
