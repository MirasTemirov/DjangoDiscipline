<template>
  <div>
    <h2 class="text-center mb-4">Пароль</h2>
    <v-row>
      <v-col cols="3"></v-col>
      <v-col cols="6">
        <v-card>
          <v-card-text class="py-4">
            <v-form ref="formUpdate">
              <v-row class="mt-2">
                <v-col cols="12" class="py-0">
                  <v-text-field
                    v-model="form.oldPassword"
                    label="Старый пароль"
                    :rules="[rules.required]"
                    clearable
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" class="py-0">
                  <v-text-field
                    v-model="form.newPassword"
                    label="Новый пароль"
                    :rules="[rules.required, rules.password]"
                    clearable
                    :append-icon="
                      form.newPasswordVisible ? 'mdi-eye-off' : 'mdi-eye'
                    "
                    @click:append="
                      () => (form.newPasswordVisible = !form.newPasswordVisible)
                    "
                    :type="form.newPasswordVisible ? 'text' : 'password'"
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" class="py-0">
                  <v-text-field
                    v-model="form.newPasswordConfirmation"
                    label="Подтверждение нового пароля"
                    :rules="[rules.required, rules.passwordConfirm]"
                    clearable
                    :append-icon="
                      form.newPasswordConfirmationVisible
                        ? 'mdi-eye-off'
                        : 'mdi-eye'
                    "
                    @click:append="
                      () =>
                        (form.newPasswordConfirmationVisible =
                          !form.newPasswordConfirmationVisible)
                    "
                    :type="
                      form.newPasswordConfirmationVisible ? 'text' : 'password'
                    "
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              class="btn-text mr-2 mb-3"
              dark
              @click="passwordUpdate"
            >
              <v-icon small class="mr-1">mdi-check-all</v-icon>
              Сохранить
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col cols="3"></v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "Password",
  data() {
    return {
      form: {
        oldPassword: "",
        newPassword: "",
        newPasswordConfirmation: "",
        newPasswordVisible: false,
        newPasswordConfirmationVisible: false,
      },
      rules: {
        required: (value) => !!value || "Обязательное поле",
        password: (value) =>
          (value && value.length > 6 && value.length < 16) ||
          "Неправильный пароль, длина пароль должен быть между 6 и 16",
        passwordConfirm: (value) =>
          value === this.form.newPassword || "Пароль не совпадает",
      },
    };
  },
  methods: {
    passwordUpdate() {
      if (!this.$refs.formUpdate.validate()) {
        this.$store.dispatch("snackbar/setStatus", true);
        this.$store.dispatch(
          "snackbar/setText",
          `Пожалуйста, исправьте ошибки!`
        );
      } else {
        const loader = this.$loading.show(this.$loadingParams);
        this.$restApi
          .put(`account/password`, {
            old_password: this.form.oldPassword,
            new_password: this.form.newPassword,
            new_password_confirmation: this.form.newPasswordConfirmation,
          })
          .then((response) => {
            if (response.status === 200) {
              this.$store.dispatch("snackbar/setStatus", true);
              this.$store.dispatch("snackbar/setText", `Успешно`);

              this.$store.dispatch("user/setPassword", this.form.newPassword);
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
      }
    },
  },
};
</script>

<style scoped></style>
