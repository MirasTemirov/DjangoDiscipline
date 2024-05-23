<template>
  <v-app>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="elevation-12">
            <v-toolbar dark color="#222a2e">
              <v-toolbar-title>Логин</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <v-form>
                <v-text-field
                  v-model="username"
                  prepend-icon="mdi-account"
                  label="Логин"
                  type="text"
                  :rules="[rules.required]"
                ></v-text-field>
                <v-text-field
                  prepend-icon="mdi-lock"
                  v-model="password"
                  label="Пароль"
                  :append-icon="newPasswordVisible ? 'mdi-eye-off' : 'mdi-eye'"
                  @click:append="
                    () => (newPasswordVisible = !newPasswordVisible)
                  "
                  :type="newPasswordVisible ? 'text' : 'password'"
                  :rules="[rules.required]"
                ></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" class="btn-text" dark @click="login">
                <v-icon small class="mr-1">mdi-login</v-icon>
                Войти
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      newPasswordVisible: false,
      rules: {
        required: (value) => !!value || "Обязательное поле",
      },
    };
  },
  methods: {
    login() {
      const loader = this.$loading.show(this.$loadingParams);
      this.$restApi
        .post(`auth/`, {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          if (response.status === 200) {
            const userData = response.data["user"];
            this.$store.dispatch("user/setUser", userData);
            this.$store.dispatch("user/setToken", response.data.token);
            if (userData.permissions.includes("booking_list")) {
              this.$router.push("/");
            } else {
              this.$router.push("/business-hour");
            }
          }
          loader.hide();
        })
        .catch((error) => {
          if (error.response) {
            if (error.response.status === 400) {
              let errorText = [];
              let fields = Object.keys(error.response.data);
              for (let i = 0; i < fields.length; i++) {
                errorText.push(
                  "<b>" +
                    fields[i] +
                    "</b>: " +
                    error.response.data[fields[i]].join(", ")
                );
              }
              this.$store.dispatch("snackbar/setStatus", true);
              this.$store.dispatch(
                "snackbar/setText",
                errorText.join("<br />")
              );
            }
          }
          loader.hide();
        });
    },
  },
};
</script>

<style scoped></style>
