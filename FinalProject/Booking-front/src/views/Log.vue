<template>
  <div>
    <h2 class="text-center mb-4">Лог</h2>
    <v-card>
      <v-data-table
        :headers="headers"
        :items="elements"
        hide-default-footer
        disable-sort
      >
        <template v-slot:top>
          <v-row class="px-4">
            <v-col cols="3">
              <v-autocomplete
                v-model="filter.type"
                :items="filterTypeList"
                label="Тип операций"
                clearable
                @change="filterData"
              ></v-autocomplete>
            </v-col>
            <v-col cols="3">
              <v-autocomplete
                v-model="filter.data"
                :items="filterDataList"
                label="Объект операций"
                clearable
                @change="filterData"
              ></v-autocomplete>
            </v-col>
            <v-col cols="3">
              <v-autocomplete
                v-model="filter.user"
                :items="handbook.user"
                label="Пользователь"
                item-text="full_name"
                item-value="id"
                clearable
                @change="filterData"
              >
              </v-autocomplete>
            </v-col>
            <v-col cols="3">
              <v-menu
                ref="menuCreatedOn"
                v-model="filter.menuCreatedOn"
                :close-on-content-click="false"
                :return-value.sync="filter.createdOn"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    :value="filterDateText"
                    label="Дата"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                    clearable
                    @click:clear="
                      filter.createdOn = [];
                      filterData();
                    "
                  ></v-text-field>
                </template>
                <v-date-picker v-model="filter.createdOn" scrollable range>
                  <v-spacer></v-spacer>
                  <v-btn
                    text
                    color="primary"
                    @click="filter.menuCreatedOn = false"
                  >
                    Отмена
                  </v-btn>
                  <v-btn
                    text
                    color="primary"
                    @click="
                      $refs.menuCreatedOn.save(filter.createdOn);
                      filterData();
                    "
                  >
                    OK
                  </v-btn>
                </v-date-picker>
              </v-menu>
            </v-col>
          </v-row>
        </template>

        <template v-slot:item.user="{ item }">
          <template v-if="item.user">
            <template v-if="item.user['first_name'] || item.user['last_name']">
              {{ item.user["first_name"] }}
              {{ item.user["last_name"] }}
              ({{ item.user.email }})
            </template>
            <template v-else>
              {{ item.user.email }}
            </template>
          </template>
        </template>

        <template v-slot:item.type="{ item }">
          {{
            item.type in handbook.type ? handbook.type[item.type] : item.type
          }}
        </template>

        <template v-slot:item.data="{ item }">
          {{
            item.data in handbook.data ? handbook.data[item.data] : item.data
          }}
        </template>
      </v-data-table>
      <div class="text-center py-6">
        <v-pagination
          v-model="pagination.current_page"
          :length="pagination.num_pages"
          :total-visible="7"
          color="primary"
          @input="changePage"
        ></v-pagination>
      </div>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "Log",
  data() {
    return {
      filter: {
        menuCreatedOn: false,
        createdOn: [],
        type: null,
        data: null,
        user: null,
      },
      pagination: {
        current_page: 1,
        num_pages: 10,
      },
      headers: [
        {
          text: "Описание",
          align: "left",
          value: "description",
        },
        {
          text: "Тип операций",
          align: "left",
          value: "type",
        },
        {
          text: "Объект операций",
          align: "left",
          value: "data",
        },
        {
          text: "Пользователь",
          align: "left",
          value: "user",
        },
        {
          text: "Дата",
          align: "left",
          value: "created_on",
        },
      ],
      elements: [],
      handbook: {
        type: {
          read: "Считования элементов",
          create: "Создание элемента",
          update: "Редактирование элемента",
          delete: "Удаление элемента",
          login: "Авторизация пользователя",
          read_one: "Считование элемента",
          reset_password: "Сброс пароля",
        },
        data: {
          account: "Пользователь",
          booking: "Бронирование",
          handbook_group: "Группа",
          handbook_object: "Объект",
          log: "Лог",
          booking_business_hour: "Рабочие часы",
          analytic: "Аналитика",
        },
        user: [],
      },
    };
  },
  methods: {
    filterData() {
      this.pagination.current_page = 1;
      this.loadData();
    },
    loadData() {
      const loader = this.$loading.show(this.$loadingParams);
      this.$restApi
        .get(`log/`, {
          params: {
            page: this.pagination.current_page,
            type: this.filter.type,
            data: this.filter.data,
            user: this.filter.user,
            from:
              this.filter.createdOn.length === 2
                ? this.filter.createdOn[0]
                : null,
            to:
              this.filter.createdOn.length === 2
                ? this.filter.createdOn[1]
                : null,
          },
        })
        .then((response) => {
          if (response.status === 200) {
            this.elements = response.data.data;
            this.pagination.num_pages = response.data.pagination.num_pages;
          }
          loader.hide();
        })
        .catch((error) => {
          console.log(error);
          loader.hide();
        });
    },
    changePage(page) {
      this.pagination.current_page = page;
      this.loadData();
    },
  },
  mounted() {
    this.loadData();

    // load user
    this.$restApi
      .get("account/")
      .then((response) => {
        if (response.status === 200) {
          this.handbook.user = [];
          for (let i = 0; i < response.data.length; i++) {
            this.handbook.user.push({
              id: response.data[i].id,
              full_name:
                response.data[i]["first_name"] +
                " " +
                response.data[i]["last_name"],
            });
          }
        }
      })
      .catch((error) => {
        console.log(error);
      });
  },
  computed: {
    filterDateText() {
      return this.filter.createdOn.join(" - ");
    },
    filterTypeList() {
      let r = [];
      for (const typeKey in this.handbook.type) {
        r.push({
          text: this.handbook.type[typeKey],
          value: typeKey,
        });
      }
      return r;
    },
    filterDataList() {
      let r = [];
      for (const dataKey in this.handbook.data) {
        r.push({
          text: this.handbook.data[dataKey],
          value: dataKey,
        });
      }
      return r;
    },
  },
};
</script>

<style scoped></style>
