<template>
  <div>
    <v-dialog v-model="operation.create" max-width="800">
      <v-card>
        <v-card-title>
          <span class="text-h6">Создание</span>
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text class="py-4">
          <v-form ref="formCreate">
            <v-row>
              <v-col cols="12" class="py-0">
                <v-text-field
                  v-model="form.create.first_name"
                  label="Имя"
                  :rules="[rules.required]"
                  clearable
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" class="py-0">
                <v-text-field
                  v-model="form.create.last_name"
                  label="Фамилия"
                  :rules="[rules.required]"
                  clearable
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" class="py-0">
                <v-text-field
                  v-model="form.create.email"
                  label="Электронная почта"
                  :rules="[rules.required]"
                  clearable
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" class="py-0">
                <v-autocomplete
                  v-model="form.create.permissions"
                  label="Доступы"
                  :items="handbook.permissions"
                  clearable
                  multiple
                  :return-object="false"
                  chips
                  :deletable-chips="true"
                  @change="permissionsUpdate"
                ></v-autocomplete>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="6" class="py-0">
                <v-autocomplete
                  v-model="form.create.role"
                  :items="handbook.role"
                  label="Должность"
                  :rules="[rules.required]"
                ></v-autocomplete>
              </v-col>
              <v-col cols="6" class="py-0">
                <v-autocomplete
                  v-model="form.create.gender"
                  :items="handbook.gender"
                  label="Пол"
                  :rules="[rules.required]"
                ></v-autocomplete>
              </v-col>
            </v-row>
          </v-form>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="red darken-1"
            class="btn-text mr-2"
            text
            @click="operation.create = false"
          >
            <v-icon small class="mr-1">mdi-close</v-icon>
            Отменить
          </v-btn>
          <v-btn
            color="primary"
            class="btn-text"
            dark
            @click="handlerCreateElement"
          >
            <v-icon small class="mr-1">mdi-check-all</v-icon>
            Создать
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="operation.update" max-width="800">
      <v-card>
        <v-card-title>
          <span class="text-h6">Редактирование</span>
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text class="py-4">
          <v-form ref="formUpdate">
            <v-row>
              <v-col cols="12" class="py-0">
                <v-text-field
                  v-model="form.update.first_name"
                  label="Имя"
                  :rules="[rules.required]"
                  clearable
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" class="py-0">
                <v-text-field
                  v-model="form.update.last_name"
                  label="Фамилия"
                  :rules="[rules.required]"
                  clearable
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" class="py-0">
                <v-autocomplete
                  v-model="form.update.permissions"
                  label="Доступы"
                  :items="handbook.permissions"
                  clearable
                  multiple
                  :return-object="false"
                  chips
                  :deletable-chips="true"
                  @change="permissionsUpdate"
                ></v-autocomplete>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="6" class="py-0">
                <v-autocomplete
                  v-model="form.update.role"
                  :items="handbook.role"
                  label="Должность"
                  :rules="[rules.required]"
                ></v-autocomplete>
              </v-col>
              <v-col cols="6" class="py-0">
                <v-autocomplete
                  v-model="form.update.gender"
                  :items="handbook.gender"
                  label="Пол"
                  :rules="[rules.required]"
                ></v-autocomplete>
              </v-col>
            </v-row>
          </v-form>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="red darken-1"
            class="btn-text mr-2"
            text
            @click="operation.update = false"
          >
            <v-icon small class="mr-1">mdi-close</v-icon>
            Отменить
          </v-btn>
          <v-btn
            color="primary"
            class="btn-text"
            dark
            @click="handlerUpdateElement"
          >
            <v-icon small class="mr-1">mdi-check-all</v-icon>
            Сохранить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="operation.delete" max-width="400">
      <v-card>
        <v-card-title>
          <span class="text-h6">Удаление</span>
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text class="py-4">
          Вы действительно хотите удалить "{{ form.delete.email }}"?
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="red darken-1"
            class="btn-text mr-2"
            text
            @click="operation.delete = false"
          >
            <v-icon small class="mr-1">mdi-close</v-icon>
            Отменить
          </v-btn>
          <v-btn
            color="primary"
            class="btn-text"
            dark
            @click="handlerDeleteElement"
          >
            <v-icon small class="mr-1">mdi-delete-forever</v-icon>
            Удалить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="operation.return" max-width="400">
      <v-card>
        <v-card-title>
          <span class="text-h6">Возврат</span>
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text class="py-4">
          Вы действительно хотите вернуть "{{ form.return.email }}"?
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="red darken-1"
            class="btn-text mr-2"
            text
            @click="operation.return = false"
          >
            <v-icon small class="mr-1">mdi-close</v-icon>
            Отменить
          </v-btn>
          <v-btn
            color="primary"
            class="btn-text"
            dark
            @click="handlerReturnElement"
          >
            <v-icon small class="mr-1">mdi-replay</v-icon>
            Вернуть
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="operation.showPassword" max-width="400">
      <v-card>
        <v-card-title>
          <span class="text-h6">Новый пароль</span>
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text class="py-4">
          Пароль пользователя:
          <strong>{{ form.showPassword.password }}</strong>
          <br />
          <em>Пожалуйста, скопируйте и сохраните этот пароль!</em>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            class="btn-text"
            dark
            @click="operation.showPassword = false"
          >
            <v-icon small class="mr-1">mdi-close</v-icon>
            Закрыть
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="operation.resetPassword" max-width="400">
      <v-card>
        <v-card-title>
          <span class="text-h6">Сброс пароля</span>
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text class="py-4">
          Вы действительно хотите сбросить пароль "{{
            form.resetPassword.email
          }}"?
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="red darken-1"
            class="btn-text mr-2"
            text
            @click="operation.resetPassword = false"
          >
            <v-icon small class="mr-1">mdi-close</v-icon>
            Отменить
          </v-btn>
          <v-btn
            color="primary"
            class="btn-text"
            dark
            @click="handlerResetPassword"
          >
            <v-icon small class="mr-1">mdi-lock-reset</v-icon>
            Сбросить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <h2 class="text-center mb-4">Пользователи</h2>
    <v-card>
      <v-card-title>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Поиск"
          single-line
          hide-details
        ></v-text-field>
        <v-spacer />
        <v-spacer />
        <v-spacer />
        <v-btn
          color="primary"
          class="btn-text"
          @click="createElement"
          v-if="
            user && hasPermission(['user_create'], user.permissions, user.role)
          "
        >
          <v-icon small class="mr-1">mdi-plus</v-icon>
          Создать
        </v-btn>
      </v-card-title>
      <v-data-table :headers="headers" :items="elements" :search="search">
        <template v-slot:item.role_gender="{ item }">
          <template v-if="item.role === 'mentor'">
            <template v-if="item.gender === 'f'"> Abla </template>
            <template v-else> Abi </template>
          </template>
          <template v-else> Teacher </template>
        </template>

        <template v-slot:item.permissions="{ item }">
          <small
            class="d-block"
            v-for="(permission, permissionIndex) in item.permissions"
            :key="permissionIndex"
          >
            <em>
              {{ getPermissionName(permission) }}
            </em>
          </small>
        </template>

        <template v-slot:item.is_active="{ item }">
          <template v-if="item['is_active']">
            <span class="green--text"> Активный </span>
          </template>
          <template v-else>
            <span class="red--text"> Не активный </span>
          </template>
        </template>

        <template v-slot:item.actions="{ item }">
          <div class="text-no-wrap">
            <v-tooltip
              bottom
              v-if="
                user &&
                hasPermission(['user_update'], user.permissions, user.role)
              "
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  icon
                  @click="updateElement(item)"
                  v-bind="attrs"
                  v-on="on"
                >
                  <v-icon>mdi-pencil</v-icon>
                </v-btn>
              </template>
              <span>Редактирование</span>
            </v-tooltip>
            <template v-if="item['is_active']">
              <v-tooltip
                bottom
                v-if="
                  user &&
                  hasPermission(['user_delete'], user.permissions, user.role)
                "
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    icon
                    @click="deleteElement(item)"
                    color="red"
                    v-bind="attrs"
                    v-on="on"
                  >
                    <v-icon>mdi-delete-forever</v-icon>
                  </v-btn>
                </template>
                <span>Удаление</span>
              </v-tooltip>
            </template>
            <template v-else>
              <v-tooltip
                bottom
                v-if="
                  user &&
                  hasPermission(['user_update'], user.permissions, user.role)
                "
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    icon
                    @click="returnElement(item)"
                    color="black"
                    v-bind="attrs"
                    v-on="on"
                  >
                    <v-icon>mdi-replay</v-icon>
                  </v-btn>
                </template>
                <span>Возврат</span>
              </v-tooltip>
            </template>
            <template v-if="item['is_active']">
              <v-tooltip
                bottom
                v-if="
                  user &&
                  hasPermission(['user_update'], user.permissions, user.role)
                "
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    icon
                    @click="resetPassword(item)"
                    color="black"
                    v-bind="attrs"
                    v-on="on"
                  >
                    <v-icon>mdi-lock-reset</v-icon>
                  </v-btn>
                </template>
                <span>Сброс пароля</span>
              </v-tooltip>
            </template>
          </div>
        </template>
      </v-data-table>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "Account",
  data() {
    return {
      search: "",
      headers: [
        {
          text: "Имя",
          align: "left",
          value: "first_name",
        },
        {
          text: "Фамилия",
          align: "left",
          value: "last_name",
        },
        {
          text: "Электронная почта",
          align: "left",
          value: "email",
        },
        {
          text: "Должность",
          align: "left",
          value: "role_gender",
        },
        {
          text: "Доступы",
          align: "left",
          value: "permissions",
        },
        {
          text: "Статус",
          align: "left",
          value: "is_active",
        },
        {
          text: "Действия",
          align: "right",
          value: "actions",
          sortable: false,
        },
      ],
      elements: [],
      handbook: {
        permissions: [
          {
            header: "Доступы пользователей",
          },
          {
            divider: true,
          },
          {
            text: "Просмотр списка пользователей",
            value: "user_list",
          },
          {
            text: "Создание нового пользователя",
            value: "user_create",
          },
          {
            text: "Редактирование пользователя",
            value: "user_update",
          },
          {
            text: "Удаление пользователя",
            value: "user_delete",
          },
          {
            divider: true,
          },
          {
            header: "Доступы групп",
          },
          {
            divider: true,
          },
          {
            text: "Просмотр список групп",
            value: "group_list",
          },
          {
            text: "Создание новой группы",
            value: "group_create",
          },
          {
            text: "Редактирование группы",
            value: "group_update",
          },
          {
            text: "Удаление группы",
            value: "group_delete",
          },
          {
            divider: true,
          },
          {
            header: "Доступы объектов",
          },
          {
            divider: true,
          },
          {
            text: "Просмотр список объектов",
            value: "object_list",
          },
          {
            text: "Создание нового объекта",
            value: "object_create",
          },
          {
            text: "Редактирование объекта",
            value: "object_update",
          },
          {
            text: "Удаление объекта",
            value: "object_delete",
          },
          {
            divider: true,
          },
          {
            header: "Доступы бронирования",
          },
          {
            divider: true,
          },
          {
            text: "Просмотр список бронирования",
            value: "booking_list",
          },
          {
            text: "Создание нового бронирования",
            value: "booking_create",
          },
          {
            text: "Редактирование бронирования",
            value: "booking_update",
          },
          {
            text: "Удаление бронирования",
            value: "booking_delete",
          },
          {
            divider: true,
          },
          {
            header: "Доступы лога",
          },
          {
            divider: true,
          },
          {
            text: "Просмотр лога",
            value: "log_list",
          },
          {
            divider: true,
          },
          {
            header: "Просмотр аналитик",
          },
          {
            divider: true,
          },
          {
            text: "Просмотр аналитик",
            value: "analytic_list",
          },
        ],
        role: [
          {
            text: "Учитель",
            value: "teacher",
          },
          {
            text: "Воспитатель",
            value: "mentor",
          },
        ],
        gender: [
          {
            text: "Мужской",
            value: "m",
          },
          {
            text: "Женский",
            value: "f",
          },
        ],
      },
      form: {
        create: {
          first_name: "",
          last_name: "",
          email: "",
          permissions: [],
          role: null,
          gender: null,
        },
        update: {
          id: "",
          first_name: "",
          last_name: "",
          permissions: [],
          role: null,
          gender: null,
        },
        delete: {
          id: "",
          email: "",
        },
        return: {
          id: "",
          email: "",
        },
        showPassword: {
          password: null,
        },
        resetPassword: {
          id: "",
          email: "",
        },
      },
      operation: {
        create: false,
        update: false,
        delete: false,
        return: false,
        showPassword: false,
        resetPassword: false,
      },
      rules: {
        required: (value) => !!value || "Обязательное поле",
      },
    };
  },
  methods: {
    permissionsUpdate() {
      let perms = {
        userList: false,
        groupList: false,
        objectList: false,
        bookingList: false,
      };

      let operationType = "create";
      if (this.operation.update) {
        operationType = "update";
      }

      for (let i = 0; i < this.form[operationType].permissions.length; i++) {
        if (
          ["user_create", "user_update", "user_delete"].includes(
            this.form[operationType].permissions[i]
          )
        ) {
          perms.userList = true;
        }

        if (
          ["group_create", "group_update", "group_delete"].includes(
            this.form[operationType].permissions[i]
          )
        ) {
          perms.groupList = true;
        }

        if (
          ["object_create", "object_update", "object_delete"].includes(
            this.form[operationType].permissions[i]
          )
        ) {
          perms.objectList = true;
        }

        if (
          ["booking_create", "booking_update", "booking_delete"].includes(
            this.form[operationType].permissions[i]
          )
        ) {
          perms.bookingList = true;
        }
      }

      if (
        perms.userList &&
        !this.form[operationType].permissions.includes("user_list")
      ) {
        this.form[operationType].permissions.push("user_list");
      }

      if (
        perms.groupList &&
        !this.form[operationType].permissions.includes("group_list")
      ) {
        this.form[operationType].permissions.push("group_list");
      }

      if (
        perms.objectList &&
        !this.form[operationType].permissions.includes("object_list")
      ) {
        this.form[operationType].permissions.push("object_list");
      }

      if (
        perms.bookingList &&
        !this.form[operationType].permissions.includes("booking_list")
      ) {
        this.form[operationType].permissions.push("booking_list");
      }
    },
    getPermissionName(permissionEn) {
      let permissionRu = permissionEn;
      for (let i = 0; i < this.handbook.permissions.length; i++) {
        if (this.handbook.permissions[i].value === permissionEn) {
          permissionRu = this.handbook.permissions[i].text;
          break;
        }
      }
      return permissionRu;
    },
    loadData() {
      const loader = this.$loading.show(this.$loadingParams);
      this.$restApi
        .get(`account/`)
        .then((response) => {
          if (response.status === 200) {
            this.elements = response.data;
          }
          loader.hide();
        })
        .catch((error) => {
          console.log(error);
          loader.hide();
        });
    },
    createElement() {
      this.operation.create = true;
      this.form.create = {
        first_name: "",
        last_name: "",
        email: "",
        permissions: [],
        role: null,
        gender: null,
      };
    },
    handlerCreateElement() {
      if (!this.$refs.formCreate.validate()) {
        this.$store.dispatch("snackbar/setStatus", true);
        this.$store.dispatch(
          "snackbar/setText",
          `Пожалуйста, исправьте ошибки!`
        );
      } else {
        const loader = this.$loading.show(this.$loadingParams);
        this.$restApi
          .post(`/account/`, {
            first_name: this.form.create.first_name,
            last_name: this.form.create.last_name,
            email: this.form.create.email,
            permissions: this.form.create.permissions,
            role: this.form.create.role,
            gender: this.form.create.gender,
          })
          .then((response) => {
            if (response.status === 201) {
              this.$store.dispatch("snackbar/setStatus", true);
              this.$store.dispatch("snackbar/setText", `Успешно`);
              loader.hide();

              this.operation.create = false;

              this.operation.showPassword = true;
              this.form.showPassword.password = response.data.password;

              this.loadData();
            } else {
              loader.hide();
            }
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

    updateElement(item) {
      this.operation.update = true;
      this.form.update = {
        id: item.id,
        first_name: item.first_name,
        last_name: item.last_name,
        permissions: item.permissions,
        role: item.role,
        gender: item.gender,
      };
    },
    handlerUpdateElement() {
      if (!this.$refs.formUpdate.validate()) {
        this.$store.dispatch("snackbar/setStatus", true);
        this.$store.dispatch(
          "snackbar/setText",
          `Пожалуйста, исправьте ошибки!`
        );
      } else {
        const loader = this.$loading.show(this.$loadingParams);
        this.$restApi
          .put(`/account/${this.form.update.id}`, {
            first_name: this.form.update.first_name,
            last_name: this.form.update.last_name,
            permissions: this.form.update.permissions,
            role: this.form.update.role,
            gender: this.form.update.gender,
          })
          .then((response) => {
            if (response.status === 200) {
              this.$store.dispatch("snackbar/setStatus", true);
              this.$store.dispatch("snackbar/setText", `Успешно`);
              loader.hide();

              this.operation.update = false;

              this.loadData();
            } else {
              loader.hide();
            }
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

    deleteElement(item) {
      this.operation.delete = true;
      this.form.delete = {
        id: item.id,
        email: item.email,
      };
    },
    handlerDeleteElement() {
      const loader = this.$loading.show(this.$loadingParams);
      this.$restApi
        .delete(`/account/${this.form.delete.id}`)
        .then((response) => {
          if (response.status === 204) {
            this.$store.dispatch("snackbar/setStatus", true);
            this.$store.dispatch("snackbar/setText", `Успешно`);
            loader.hide();

            this.operation.delete = false;

            this.loadData();
          } else {
            loader.hide();
          }
        })
        .catch((error) => {
          console.log(error);
          loader.hide();
        });
    },

    returnElement(item) {
      this.operation.return = true;
      this.form.return = {
        id: item.id,
        email: item.email,
      };
    },
    handlerReturnElement() {
      const loader = this.$loading.show(this.$loadingParams);
      this.$restApi
        .put(`/account/${this.form.return.id}`, {
          is_active: true,
          deleted_on: null,
        })
        .then((response) => {
          if (response.status === 200) {
            this.$store.dispatch("snackbar/setStatus", true);
            this.$store.dispatch("snackbar/setText", `Успешно`);
            loader.hide();

            this.operation.return = false;

            this.loadData();
          } else {
            loader.hide();
          }
        })
        .catch((error) => {
          console.log(error);
          loader.hide();
        });
    },

    resetPassword(item) {
      this.operation.resetPassword = true;
      this.form.resetPassword = {
        id: item.id,
        email: item.email,
      };
    },
    handlerResetPassword() {
      const loader = this.$loading.show(this.$loadingParams);
      this.$restApi
        .post(`/account/${this.form.resetPassword.id}/reset-password`)
        .then((response) => {
          if (response.status === 200) {
            this.$store.dispatch("snackbar/setStatus", true);
            this.$store.dispatch("snackbar/setText", `Успешно`);
            loader.hide();

            this.operation.resetPassword = false;

            this.operation.showPassword = true;
            this.form.showPassword.password = response.data.password;
          } else {
            loader.hide();
          }
        })
        .catch((error) => {
          console.log(error);
          loader.hide();
        });
    },
  },
  mounted() {
    this.loadData();
  },
  computed: {
    user() {
      return this.$store.getters["user/user"];
    },
  },
};
</script>

<style scoped></style>
