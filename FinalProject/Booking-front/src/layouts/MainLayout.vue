<template>
  <div>
    <Menu />

    <v-main class="page-container">
      <v-container fluid class="pa-6">
        <router-view />
      </v-container>
    </v-main>
  </div>
</template>

<script>
import Menu from "../components/Menu";

export default {
  name: "MainLayout",
  components: {
    Menu,
  },
};
</script>

<style scoped></style>
