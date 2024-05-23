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
              <v-col cols="12">
                <v-text-field
                  v-model="form.create.title"
                  label="Наименование"
                  :rules="[rules.required]"
                  clearable
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="6">
                <v-text-field
                  :value="form.create.background.slice(0, 7)"
                  label="Цвет фона"
                  :rules="[rules.required]"
                  readonly
                ></v-text-field>
                <v-color-picker
                  v-model="form.create.background"
                  :canvas-height="70"
                  dot-size="22"
                  hide-mode-switch
                  mode="hexa"
                  swatches-max-height="182"
                  hide-inputs
                ></v-color-picker>
              </v-col>
              <v-col cols="6">
                <v-text-field
                  :value="form.create['text_color'].slice(0, 7)"
                  label="Цвет текста"
                  :rules="[rules.required]"
                  readonly
                ></v-text-field>
                <v-color-picker
                  v-model="form.create['text_color']"
                  :canvas-height="70"
                  dot-size="22"
                  hide-mode-switch
                  mode="hexa"
                  swatches-max-height="182"
                  hide-inputs
                ></v-color-picker>
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
              <v-col cols="12">
                <v-text-field
                  v-model="form.update.title"
                  label="Наименование"
                  :rules="[rules.required]"
                  clearable
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="6">
                <v-text-field
                  :value="form.update.background.slice(0, 7)"
                  label="Цвет фона"
                  :rules="[rules.required]"
                  readonly
                ></v-text-field>
                <v-color-picker
                  v-model="form.update.background"
                  :canvas-height="70"
                  dot-size="22"
                  hide-mode-switch
                  mode="hexa"
                  swatches-max-height="182"
                  hide-inputs
                ></v-color-picker>
              </v-col>
              <v-col cols="6">
                <v-text-field
                  :value="form.update['text_color'].slice(0, 7)"
                  label="Цвет текста"
                  :rules="[rules.required]"
                  readonly
                ></v-text-field>
                <v-color-picker
                  v-model="form.update['text_color']"
                  :canvas-height="70"
                  dot-size="22"
                  hide-mode-switch
                  mode="hexa"
                  swatches-max-height="182"
                  hide-inputs
                ></v-color-picker>
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
          Вы действительно хотите удалить "{{ form.delete.title }}"?
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
          Вы действительно хотите вернуть "{{ form.return.title }}"?
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

    <h2 class="text-center mb-4">Объекты</h2>
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
            user &&
            hasPermission(['object_create'], user.permissions, user.role)
          "
        >
          <v-icon small class="mr-1">mdi-plus</v-icon>
          Создать
        </v-btn>
      </v-card-title>
      <v-data-table :headers="headers" :items="elements" :search="search">
        <template v-slot:item.is_active="{ item }">
          <template v-if="item['is_active']">
            <span class="green--text"> Активный </span>
          </template>
          <template v-else>
            <span class="red--text"> Не активный </span>
            <br />
            <small>
              <em>Дата удаления: {{ item["deleted_on"] }}</em>
            </small>
          </template>
        </template>

        <template v-slot:item.created_by="{ item }">
          <template v-if="item['created_by']">
            <template
              v-if="
                item['created_by']['first_name'] ||
                item['created_by']['last_name']
              "
            >
              {{ item["created_by"]["first_name"] }}
              {{ item["created_by"]["last_name"] }}
              ({{ item["created_by"].email }})
            </template>
            <template v-else>
              {{ item["created_by"].email }}
            </template>
          </template>
        </template>

        <template v-slot:item.background="{ item }">
          <div class="d-flex align-center">
            <span
              class="color-box mr-2"
              :style="{ background: item.background }"
            ></span>
            {{ item.background }}
          </div>
        </template>

        <template v-slot:item.text_color="{ item }">
          <div class="d-flex align-center">
            <span
              class="color-box mr-2"
              :style="{ background: item.text_color }"
            ></span>
            {{ item["text_color"] }}
          </div>
        </template>

        <template v-slot:item.actions="{ item }">
          <div class="text-no-wrap">
            <v-tooltip
              bottom
              v-if="
                user &&
                hasPermission(['object_update'], user.permissions, user.role)
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
                  hasPermission(['object_delete'], user.permissions, user.role)
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
                  hasPermission(['object_update'], user.permissions, user.role)
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
          </div>
        </template>
      </v-data-table>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "Object",
  data() {
    return {
      search: "",
      headers: [
        {
          text: "Название",
          align: "left",
          value: "title",
        },
        {
          text: "Автор",
          align: "left",
          value: "created_by",
        },
        {
          text: "Цвет фона",
          align: "left",
          value: "background",
          sortable: false,
        },
        {
          text: "Цвет текста",
          align: "left",
          value: "text_color",
          sortable: false,
        },
        {
          text: "Дата создания",
          align: "left",
          value: "created_on",
        },
        {
          text: "Дата редактирования",
          align: "left",
          value: "edited_on",
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
      form: {
        create: {
          title: "",
          background: "",
          text_color: "",
        },
        update: {
          id: "",
          title: "",
          background: "",
          text_color: "",
        },
        delete: {
          id: "",
          title: "",
        },
        return: {
          id: "",
          title: "",
        },
      },
      operation: {
        create: false,
        update: false,
        delete: false,
        return: false,
      },
      rules: {
        required: (value) => !!value || "Обязательное поле",
      },
    };
  },
  methods: {
    loadData() {
      const loader = this.$loading.show(this.$loadingParams);
      this.$restApi
        .get(`handbook/object`)
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
        title: "",
        background: "",
        text_color: "",
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
          .post(`/handbook/object`, {
            title: this.form.create.title,
            background: this.form.create.background.slice(0, 7),
            text_color: this.form.create["text_color"].slice(0, 7),
          })
          .then((response) => {
            if (response.status === 201) {
              this.$store.dispatch("snackbar/setStatus", true);
              this.$store.dispatch("snackbar/setText", `Успешно`);
              loader.hide();

              this.operation.create = false;

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
      this.form.update = JSON.parse(JSON.stringify(item));
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
          .put(`/handbook/object/${this.form.update.id}`, {
            title: this.form.update.title,
            background: this.form.update.background.slice(0, 7),
            text_color: this.form.update["text_color"].slice(0, 7),
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
        title: item.title,
      };
    },
    handlerDeleteElement() {
      const loader = this.$loading.show(this.$loadingParams);
      this.$restApi
        .delete(`/handbook/object/${this.form.delete.id}`)
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
        title: item.title,
      };
    },
    handlerReturnElement() {
      const loader = this.$loading.show(this.$loadingParams);
      this.$restApi
        .put(`/handbook/object/${this.form.return.id}`, {
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
