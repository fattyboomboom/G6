<template>
  <div class="popup">
    <div class="popup-inner">
      <slot />
      <button class="popup-close">Close</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "SignUp",
  //   data: () => ({
  //     first: null,
  //     last: null,
  //     email: null,
  //     password: null,
  //     terms: false,
  //   }),
};
</script>

<style scoped>
.popup {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 99;
    background-color: cornflowerblue;

    display: flex;
    align-items: center;
    justify-content: center;
}

.popup-inner {
        background: white;
        padding: 32px;
    }
</style>
