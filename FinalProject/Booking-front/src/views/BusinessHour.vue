<template>
  <div>
    <h2 class="text-center mb-4">Рабочий график</h2>
    <v-card>
      <v-card-text class="px-10">
        <v-row>
          <v-col cols="3">
            <div class="d-flex align-center" style="height: 100%">
              <v-checkbox
                class="ma-0"
                v-model="form.mon"
                label="Понедельник"
                hide-details
              ></v-checkbox>
            </div>
          </v-col>
          <v-col cols="4">
            <v-menu
              ref="menuMonStart"
              v-model="menu.mon.start"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="form.mon_start"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  :disabled="!form.mon"
                  v-model="form.mon_start"
                  label="Время старта"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  hide-details
                ></v-text-field>
              </template>
              <v-time-picker
                v-if="menu.mon.start"
                v-model="form.mon_start"
                full-width
                format="24hr"
                @click:minute="$refs.menuMonStart.save(form.mon_start)"
              ></v-time-picker>
            </v-menu>
          </v-col>
          <v-col cols="4">
            <v-menu
              ref="menuMonEnd"
              v-model="menu.mon.end"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="form.mon_end"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  :disabled="!form.mon"
                  v-model="form.mon_end"
                  label="Время окончания"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  hide-details
                ></v-text-field>
              </template>
              <v-time-picker
                v-if="menu.mon.end"
                v-model="form.mon_end"
                full-width
                format="24hr"
                @click:minute="$refs.menuMonEnd.save(form.mon_end)"
              ></v-time-picker>
            </v-menu>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="3">
            <div class="d-flex align-center" style="height: 100%">
              <v-checkbox
                class="ma-0"
                v-model="form.tue"
                label="Вторник"
                hide-details
              ></v-checkbox>
            </div>
          </v-col>
          <v-col cols="4">
            <v-menu
              ref="menuTueStart"
              v-model="menu.tue.start"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="form.tue_start"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  :disabled="!form.tue"
                  v-model="form.tue_start"
                  label="Время старта"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  hide-details
                ></v-text-field>
              </template>
              <v-time-picker
                v-if="menu.tue.start"
                v-model="form.tue_start"
                full-width
                format="24hr"
                @click:minute="$refs.menuTueStart.save(form.tue_start)"
              ></v-time-picker>
            </v-menu>
          </v-col>
          <v-col cols="4">
            <v-menu
              ref="menuTueEnd"
              v-model="menu.tue.end"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="form.tue_end"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  :disabled="!form.tue"
                  v-model="form.tue_end"
                  label="Время окончания"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  hide-details
                ></v-text-field>
              </template>
              <v-time-picker
                v-if="menu.tue.end"
                v-model="form.tue_end"
                full-width
                format="24hr"
                @click:minute="$refs.menuTueEnd.save(form.tue_end)"
              ></v-time-picker>
            </v-menu>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="3">
            <div class="d-flex align-center" style="height: 100%">
              <v-checkbox
                class="ma-0"
                v-model="form.wen"
                label="Cреда"
                hide-details
              ></v-checkbox>
            </div>
          </v-col>
          <v-col cols="4">
            <v-menu
              ref="menuWenStart"
              v-model="menu.wen.start"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="form.wen_start"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  :disabled="!form.wen"
                  v-model="form.wen_start"
                  label="Время старта"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  hide-details
                ></v-text-field>
              </template>
              <v-time-picker
                v-if="menu.wen.start"
                v-model="form.wen_start"
                full-width
                format="24hr"
                @click:minute="$refs.menuWenStart.save(form.wen_start)"
              ></v-time-picker>
            </v-menu>
          </v-col>
          <v-col cols="4">
            <v-menu
              ref="menuWenEnd"
              v-model="menu.wen.end"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="form.wen_end"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  :disabled="!form.wen"
                  v-model="form.wen_end"
                  label="Время окончания"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  hide-details
                ></v-text-field>
              </template>
              <v-time-picker
                v-if="menu.wen.end"
                v-model="form.wen_end"
                full-width
                format="24hr"
                @click:minute="$refs.menuWenEnd.save(form.wen_end)"
              ></v-time-picker>
            </v-menu>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="3">
            <div class="d-flex align-center" style="height: 100%">
              <v-checkbox
                class="ma-0"
                v-model="form.thu"
                label="Четверг"
                hide-details
              ></v-checkbox>
            </div>
          </v-col>
          <v-col cols="4">
            <v-menu
              ref="menuThuStart"
              v-model="menu.thu.start"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="form.thu_start"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  :disabled="!form.thu"
                  v-model="form.thu_start"
                  label="Время старта"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  hide-details
                ></v-text-field>
              </template>
              <v-time-picker
                v-if="menu.thu.start"
                v-model="form.thu_start"
                full-width
                format="24hr"
                @click:minute="$refs.menuThuStart.save(form.thu_start)"
              ></v-time-picker>
            </v-menu>
          </v-col>
          <v-col cols="4">
            <v-menu
              ref="menuThuEnd"
              v-model="menu.thu.end"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="form.thu_end"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  :disabled="!form.thu"
                  v-model="form.thu_end"
                  label="Время окончания"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  hide-details
                ></v-text-field>
              </template>
              <v-time-picker
                v-if="menu.thu.end"
                v-model="form.thu_end"
                full-width
                format="24hr"
                @click:minute="$refs.menuThuEnd.save(form.thu_end)"
              ></v-time-picker>
            </v-menu>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="3">
            <div class="d-flex align-center" style="height: 100%">
              <v-checkbox
                class="ma-0"
                v-model="form.fri"
                label="Пятница"
                hide-details
              ></v-checkbox>
            </div>
          </v-col>
          <v-col cols="4">
            <v-menu
              ref="menuFriStart"
              v-model="menu.fri.start"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="form.fri_start"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  :disabled="!form.fri"
                  v-model="form.fri_start"
                  label="Время старта"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  hide-details
                ></v-text-field>
              </template>
              <v-time-picker
                v-if="menu.fri.start"
                v-model="form.fri_start"
                full-width
                format="24hr"
                @click:minute="$refs.menuFriStart.save(form.fri_start)"
              ></v-time-picker>
            </v-menu>
          </v-col>
          <v-col cols="4">
            <v-menu
              ref="menuFriEnd"
              v-model="menu.fri.end"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="form.fri_end"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  :disabled="!form.fri"
                  v-model="form.fri_end"
                  label="Время окончания"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  hide-details
                ></v-text-field>
              </template>
              <v-time-picker
                v-if="menu.fri.end"
                v-model="form.fri_end"
                full-width
                format="24hr"
                @click:minute="$refs.menuFriEnd.save(form.fri_end)"
              ></v-time-picker>
            </v-menu>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="3">
            <div class="d-flex align-center" style="height: 100%">
              <v-checkbox
                class="ma-0"
                v-model="form.sat"
                label="Суббота"
                hide-details
              ></v-checkbox>
            </div>
          </v-col>
          <v-col cols="4">
            <v-menu
              ref="menuSatStart"
              v-model="menu.sat.start"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="form.sat_start"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  :disabled="!form.sat"
                  v-model="form.sat_start"
                  label="Время старта"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  hide-details
                ></v-text-field>
              </template>
              <v-time-picker
                v-if="menu.sat.start"
                v-model="form.sat_start"
                full-width
                format="24hr"
                @click:minute="$refs.menuSatStart.save(form.sat_start)"
              ></v-time-picker>
            </v-menu>
          </v-col>
          <v-col cols="4">
            <v-menu
              ref="menuSatEnd"
              v-model="menu.sat.end"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="form.sat_end"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  :disabled="!form.sat"
                  v-model="form.sat_end"
                  label="Время окончания"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  hide-details
                ></v-text-field>
              </template>
              <v-time-picker
                v-if="menu.sat.end"
                v-model="form.sat_end"
                full-width
                format="24hr"
                @click:minute="$refs.menuSatEnd.save(form.sat_end)"
              ></v-time-picker>
            </v-menu>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="3">
            <div class="d-flex align-center" style="height: 100%">
              <v-checkbox
                class="ma-0"
                v-model="form.sun"
                label="Воскресенье"
                hide-details
              ></v-checkbox>
            </div>
          </v-col>
          <v-col cols="4">
            <v-menu
              ref="menuSunStart"
              v-model="menu.sun.start"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="form.sun_start"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  :disabled="!form.sun"
                  v-model="form.sun_start"
                  label="Время старта"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  hide-details
                ></v-text-field>
              </template>
              <v-time-picker
                v-if="menu.sun.start"
                v-model="form.sun_start"
                full-width
                format="24hr"
                @click:minute="$refs.menuSunStart.save(form.sun_start)"
              ></v-time-picker>
            </v-menu>
          </v-col>
          <v-col cols="4">
            <v-menu
              ref="menuSunEnd"
              v-model="menu.sun.end"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="form.sun_end"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="290px"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  :disabled="!form.sun"
                  v-model="form.sun_end"
                  label="Время окончания"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                  hide-details
                ></v-text-field>
              </template>
              <v-time-picker
                v-if="menu.sun.end"
                v-model="form.sun_end"
                full-width
                format="24hr"
                @click:minute="$refs.menuSunEnd.save(form.sun_end)"
              ></v-time-picker>
            </v-menu>
          </v-col>
        </v-row>
        <v-row class="mt-4">
          <v-col cols="11">
            <div class="d-flex">
              <v-btn
                v-if="
                  user &&
                  hasPermission(['bHour_create'], user.permissions, user.role)
                "
                class="ml-auto btn-text"
                color="primary"
                @click="saveBusinessHour"
              >
                <v-icon class="mr-2">mdi-check-all</v-icon>
                Сохранить
              </v-btn>
            </div>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "BusinessHour",
  data() {
    return {
      form: {
        mon: false,
        mon_start: "00:00",
        mon_end: "23:59",
        tue: false,
        tue_start: "00:00",
        tue_end: "23:59",
        wen: false,
        wen_start: "00:00",
        wen_end: "23:59",
        thu: false,
        thu_start: "00:00",
        thu_end: "23:59",
        fri: false,
        fri_start: "00:00",
        fri_end: "23:59",
        sat: false,
        sat_start: "00:00",
        sat_end: "23:59",
        sun: false,
        sun_start: "00:00",
        sun_end: "23:59",
      },
      menu: {
        mon: {
          start: false,
          end: false,
        },
        tue: {
          start: false,
          end: false,
        },
        wen: {
          start: false,
          end: false,
        },
        thu: {
          start: false,
          end: false,
        },
        fri: {
          start: false,
          end: false,
        },
        sat: {
          start: false,
          end: false,
        },
        sun: {
          start: false,
          end: false,
        },
      },
    };
  },
  methods: {
    loadData() {
      const loader = this.$loading.show(this.$loadingParams);
      this.$restApi
        .get(`booking/business-hour`)
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
    saveBusinessHour() {
      const loader = this.$loading.show(this.$loadingParams);
      this.$restApi
        .post(`/booking/business-hour`, {
          mon: this.form.mon,
          mon_start: this.form.mon_start,
          mon_end: this.form.mon_end,
          tue: this.form.tue,
          tue_start: this.form.tue_start,
          tue_end: this.form.tue_end,
          wen: this.form.wen,
          wen_start: this.form.wen_start,
          wen_end: this.form.wen_end,
          thu: this.form.thu,
          thu_start: this.form.thu_start,
          thu_end: this.form.thu_end,
          fri: this.form.fri,
          fri_start: this.form.fri_start,
          fri_end: this.form.fri_end,
          sat: this.form.sat,
          sat_start: this.form.sat_start,
          sat_end: this.form.sat_end,
          sun: this.form.sun,
          sun_start: this.form.sun_start,
          sun_end: this.form.sun_end,
        })
        .then((response) => {
          if (response.status === 200) {
            this.$store.dispatch("snackbar/setStatus", true);
            this.$store.dispatch("snackbar/setText", `Успешно`);
          }
          loader.hide();
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
