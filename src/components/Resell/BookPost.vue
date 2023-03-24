<template>
<div class="modalBackground" v-show="open">
    <div class="modalInner">
        <div class="modalContent">
            <slot />

            <v-btn  @click="$emit('close')">Close</v-btn>
        </div>
    </div>
  
</div>
</template>

<script>
export default {
    name: "BookPost",

    props: {
        open: {
            type: Boolean,
            required: true
        }
    }
};



</script>

<style>
.modalbackground {
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
</style>