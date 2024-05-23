<template>
  <v-app>
    <v-snackbar v-model="snackbarStatus" top timeout="5000">
      <span v-html="snackbarText"></span>
      <template v-slot:action="{ attrs }">
        <v-btn text v-bind="attrs" @click="snackbarStatus = false">
          Закрыть
        </v-btn>
      </template>
    </v-snackbar>
    <router-view />
  </v-app>
</template>

<script>
export default {
  name: "App",
  data: () => ({
    snackbar: false,
    text: `Success`,
  }),
  computed: {
    snackbarStatus: {
      get() {
        return this.$store.getters["snackbar/status"];
      },
      set(value) {
        this.$store.dispatch("snackbar/setStatus", value);
      },
    },
    snackbarText() {
      return this.$store.getters["snackbar/text"];
    },
  },
};
</script>

<style>
.color-box {
  width: 20px;
  height: 20px;
  border: 1px solid black;
  border-radius: 50%;
  display: inline-block;
}

.btn-text {
  text-transform: none !important;
}

.page-container {
  background: #f5f5f5aa;
  min-height: 100vh;
}
</style>

