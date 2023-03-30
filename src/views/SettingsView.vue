<template>
  <navBar />
  <h1 >Settings</h1>
  <SettingsForm />
</template>
<script>
import SettingsForm from "@/components/SettingsStuff/SettingsForm.vue";
import navBar from "@/globalcomponents/NavBar.vue";
export default {
  name: "SettingsView",
    components: {
        SettingsForm,
        navBar,
    },
  setup() {
    return {
      //
    };
  },
};
</script>
<style scoped>
h1 {
    text-align: center;
}
</style>
