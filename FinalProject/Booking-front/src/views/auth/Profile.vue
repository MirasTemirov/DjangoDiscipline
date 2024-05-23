<template>
  <div>
    <h2 class="text-center mb-4">Профиль</h2>
    <v-row>
      <v-col cols="3"></v-col>
      <v-col cols="6">
        <v-card>
          <v-card-text class="py-4">
            <v-form ref="formUpdate">
              <v-row class="mt-2">
                <v-col cols="12" class="py-0">
                  <v-text-field
                    v-model="form.first_name"
                    label="Имя"
                    :rules="[rules.required]"
                    clearable
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" class="py-0">
                  <v-text-field
                    v-model="form.last_name"
                    label="Фамилия"
                    :rules="[rules.required]"
                    clearable
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" class="py-0">
                  <v-text-field
                    v-model="form.email"
                    label="Электронная почта"
                    :rules="[rules.required, rules.email]"
                    clearable
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
              @click="profileUpdate"
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
  name: "Profile",
  data() {
    return {
      form: {
        first_name: "",
        last_name: "",
        email: "",
      },
      rules: {
        required: (value) => !!value || "Обязательное поле",
        email: (value) => {
          const pattern =
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || "Некорректный e-mail.";
        },
      },
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    loadData() {
      const loader = this.$loading.show(this.$loadingParams);
      this.$restApi
        .get(`account/me`)
        .then((response) => {
          if (response.status === 200) {
            this.form = response.data;
          }
          loader.hide();
        })
        .catch((error) => {
          console.log(error);
          loader.hide();
        });
    },
    profileUpdate() {
      if (!this.$refs.formUpdate.validate()) {
        this.$store.dispatch("snackbar/setStatus", true);
        this.$store.dispatch(
          "snackbar/setText",
          `Пожалуйста, исправьте ошибки!`
        );
      } else {
        const loader = this.$loading.show(this.$loadingParams);
        this.$restApi
          .put(`/account/profile`, {
            first_name: this.form.first_name,
            last_name: this.form.last_name,
            email: this.form.email,
          })
          .then((response) => {
            if (response.status === 200) {
              this.$store.dispatch("snackbar/setStatus", true);
              this.$store.dispatch("snackbar/setText", `Успешно`);

              this.$store.dispatch("user/setEmail", this.form.email);
              this.$store.dispatch("user/setLastName", this.form.last_name);
              this.$store.dispatch("user/setFirstName", this.form.first_name);
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
