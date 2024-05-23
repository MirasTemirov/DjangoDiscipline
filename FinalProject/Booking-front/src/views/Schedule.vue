<template>
  <div>
    <v-dialog v-model="operation.create" max-width="800">
      <v-card>
        <v-card-title>
          <span class="text-h6">Добавить бронирование</span>
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text class="py-4">
          <v-form ref="formCreate">
            <v-row>
              <v-col cols="12" class="py-0">
                <v-autocomplete
                  :items="handbook.groups"
                  v-model="form.create.group"
                  label="Группа"
                  item-text="title"
                  item-value="id"
                  :rules="[rules.required]"
                ></v-autocomplete>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" class="py-0">
                <v-autocomplete
                  :items="handbook.objects"
                  v-model="form.create.object"
                  label="Объект"
                  item-text="title"
                  item-value="id"
                  :rules="[rules.required]"
                ></v-autocomplete>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="4" class="py-0">
                <v-menu
                  v-model="form.create.menu"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  transition="scale-transition"
                  offset-y
                  :disabled="true"
                  min-width="auto"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="form.create.date"
                      label="Дата"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker
                    v-model="form.create.date"
                    @input="form.create.menu = false"
                  ></v-date-picker>
                </v-menu>
              </v-col>
              <v-col cols="4" class="py-0">
                <v-menu
                  ref="fromMenu"
                  v-model="form.create.fromMenu"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  :return-value.sync="form.create.fromDateTime"
                  transition="scale-transition"
                  offset-y
                  :disabled="true"
                  max-width="290px"
                  min-width="290px"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="form.create.fromDateTime"
                      label="От"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                      hide-details
                    ></v-text-field>
                  </template>
                  <v-time-picker
                    v-if="form.create.fromMenu"
                    v-model="form.create.fromDateTime"
                    full-width
                    format="24hr"
                    @click:minute="
                      $refs.fromMenu.save(form.create.fromDateTime)
                    "
                  ></v-time-picker>
                </v-menu>
              </v-col>
              <v-col cols="4" class="py-0">
                <v-menu
                  ref="toMenu"
                  v-model="form.create.toMenu"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  :return-value.sync="form.create.toDateTime"
                  transition="scale-transition"
                  offset-y
                  :disabled="true"
                  max-width="290px"
                  min-width="290px"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="form.create.toDateTime"
                      label="До"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                      hide-details
                    ></v-text-field>
                  </template>
                  <v-time-picker
                    v-if="form.create.toMenu"
                    v-model="form.create.toDateTime"
                    full-width
                    format="24hr"
                    @click:minute="$refs.toMenu.save(form.create.toDateTime)"
                  ></v-time-picker>
                </v-menu>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" class="py-0">
                <v-text-field
                  v-model="form.create.comment"
                  label="Комментарий"
                ></v-text-field>
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
          <span class="text-h6">Редактировать бронирование</span>
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text class="py-4">
          <v-form ref="formUpdate">
            <v-row>
              <v-col cols="12" class="py-0">
                <v-autocomplete
                  :items="handbook.groups"
                  v-model="form.update.group"
                  label="Группа"
                  item-text="title"
                  item-value="id"
                  :rules="[rules.required]"
                ></v-autocomplete>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" class="py-0">
                <v-autocomplete
                  :items="handbook.objects"
                  v-model="form.update.object"
                  label="Объект"
                  item-text="title"
                  item-value="id"
                  :rules="[rules.required]"
                ></v-autocomplete>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="4" class="py-0">
                <v-menu
                  v-model="form.update.menu"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  transition="scale-transition"
                  offset-y
                  :disabled="true"
                  min-width="auto"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="form.update.date"
                      label="Дата"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker
                    v-model="form.update.date"
                    @input="form.update.menu = false"
                  ></v-date-picker>
                </v-menu>
              </v-col>
              <v-col cols="4" class="py-0">
                <v-menu
                  ref="fromMenu"
                  v-model="form.update.fromMenu"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  :return-value.sync="form.update.fromDateTime"
                  transition="scale-transition"
                  offset-y
                  max-width="290px"
                  min-width="290px"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="form.update.fromDateTime"
                      label="От"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                      hide-details
                    ></v-text-field>
                  </template>
                  <v-time-picker
                    v-if="form.update.fromMenu"
                    v-model="form.update.fromDateTime"
                    full-width
                    :min="form.update.min"
                    :max="
                      form.update.toDateTime
                        ? form.update.toDateTime
                        : form.update.max
                    "
                    format="24hr"
                    @click:minute="
                      $refs.fromMenu.save(form.update.fromDateTime)
                    "
                  ></v-time-picker>
                </v-menu>
              </v-col>
              <v-col cols="4" class="py-0">
                <v-menu
                  ref="toMenu"
                  v-model="form.update.toMenu"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  :return-value.sync="form.update.toDateTime"
                  transition="scale-transition"
                  offset-y
                  max-width="290px"
                  min-width="290px"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="form.update.toDateTime"
                      label="До"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                      hide-details
                    ></v-text-field>
                  </template>
                  <v-time-picker
                    v-if="form.update.toMenu"
                    v-model="form.update.toDateTime"
                    full-width
                    :min="
                      form.update.fromDateTime
                        ? form.update.fromDateTime
                        : form.update.min
                    "
                    :max="form.update.max"
                    format="24hr"
                    @click:minute="$refs.toMenu.save(form.update.toDateTime)"
                  ></v-time-picker>
                </v-menu>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" class="py-0">
                <v-text-field
                  v-model="form.update.comment"
                  label="Комментарий"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="4" class="py-0">
                <v-text-field
                  v-model="form.update.created_by"
                  label="Автор"
                  readonly
                ></v-text-field>
              </v-col>
              <v-col cols="4" class="py-0">
                <v-text-field
                  v-model="form.update.created_on"
                  label="Дата создания"
                  readonly
                ></v-text-field>
              </v-col>
              <v-col cols="4" class="py-0">
                <v-text-field
                  v-model="form.update.edited_on"
                  label="Дата редактирования"
                  readonly
                ></v-text-field>
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
            v-if="
              user &&
              hasPermission(['booking_delete'], user.permissions, user.role)
            "
            color="error"
            class="btn-text mr-2"
            dark
            @click="deleteElement(form.update)"
          >
            <v-icon small class="mr-1">mdi-delete-forever</v-icon>
            Удалить
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
          Вы действительно хотите удалить?
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
    <v-dialog v-model="operation.read" max-width="800">
      <v-card>
        <v-card-title>
          <span class="text-h6">Бронирование</span>
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text class="py-4">
          <v-form>
            <v-row>
              <v-col cols="12" class="py-0">
                <v-autocomplete
                  :items="handbook.groups"
                  :value="form.read.group"
                  label="Группа"
                  readonly
                  item-text="title"
                  item-value="id"
                ></v-autocomplete>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" class="py-0">
                <v-autocomplete
                  :items="handbook.objects"
                  :value="form.read.object"
                  label="Объект"
                  readonly
                  item-text="title"
                  item-value="id"
                ></v-autocomplete>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="4" class="py-0">
                <v-text-field
                  v-model="form.read.date"
                  label="Дата"
                  readonly
                ></v-text-field>
              </v-col>
              <v-col cols="4" class="py-0">
                <v-text-field
                  v-model="form.read.fromDateTime"
                  label="От"
                  readonly
                ></v-text-field>
              </v-col>
              <v-col cols="4" class="py-0">
                <v-text-field
                  v-model="form.read.toDateTime"
                  label="До"
                  readonly
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="4" class="py-0">
                <v-text-field
                  v-model="form.read.created_by"
                  label="Автор"
                  readonly
                ></v-text-field>
              </v-col>
              <v-col cols="4" class="py-0">
                <v-text-field
                  v-model="form.read.created_on"
                  label="Дата создания"
                  readonly
                ></v-text-field>
              </v-col>
              <v-col cols="4" class="py-0">
                <v-text-field
                  v-model="form.read.edited_on"
                  label="Дата редактирования"
                  readonly
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" class="py-0">
                <v-text-field
                  v-model="form.read.comment"
                  label="Комментарий"
                  readonly
                ></v-text-field>
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
            @click="operation.read = false"
          >
            <v-icon small class="mr-1">mdi-close</v-icon>
            Закрыть
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <h2 class="text-center mb-4">График</h2>
    <v-card class="mb-4">
      <v-card-text>
        <v-row>
          <v-col cols="4" class="py-0">
            <v-autocomplete
              v-model="filter.group"
              :items="handbook.groups"
              label="Группа"
              item-text="title"
              item-value="id"
              clearable
              @change="loadData"
            />
          </v-col>
          <v-col cols="4" class="py-0">
            <v-autocomplete
              v-model="filter.object"
              :items="handbook.objects"
              label="Объекты"
              item-text="title"
              item-value="id"
              clearable
              @change="loadData"
            />
          </v-col>
          <v-col cols="4" class="py-0">
            <v-autocomplete
              v-model="filter.created_by"
              :items="handbook.created_by"
              label="Автор"
              item-text="full_name"
              item-value="id"
              clearable
              @change="loadData"
            />
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
    <v-card>
      <v-card-text>
        <FullCalendar :options="calendarOptions" />
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import "@fullcalendar/core/vdom"; // solves problem with Vite
import FullCalendar from "@fullcalendar/vue";
import dayGridPlugin from "@fullcalendar/daygrid";
import timeGridPlugin from "@fullcalendar/timegrid";
import interactionPlugin from "@fullcalendar/interaction";
import ruLocale from "@fullcalendar/core/locales/ru";

export default {
  name: "Schedule",
  components: {
    FullCalendar,
  },
  data() {
    return {
      filter: {
        group: null,
        object: null,
        created_by: null,
      },
      operation: {
        read: false,
        create: false,
        update: false,
        delete: false,
      },
      form: {
        read: {
          group: null,
          object: null,
          fromDateTime: null,
          toDateTime: null,
          created_by: null,
          created_on: null,
          edited_on: null,
          comment: null,
        },
        create: {
          group: null,
          object: null,
          fromDateTime: null,
          toDateTime: null,
          fromMenu: false,
          toMenu: false,
          menu: false,
          min: false,
          max: false,
          comment: null,
        },
        update: {
          id: "",
          group: null,
          object: null,
          created_by: null,
          created_on: null,
          edited_on: null,
          fromDateTime: null,
          toDateTime: null,
          fromMenu: false,
          toMenu: false,
          menu: false,
          min: false,
          max: false,
          comment: null,
        },
        delete: {
          id: "",
        },
        content: {
          fromDateTime: null,
          toDateTime: null,
        },
      },
      handbook: {
        groups: [],
        objects: [],
        created_by: [],
      },
      rules: {
        required: (value) => !!value || "Обязательное поле",
      },
      element: null,
      elements: [],
      calendarOptions: {
        plugins: [dayGridPlugin, timeGridPlugin, interactionPlugin],
        headerToolbar: {
          start: "prev,next today",
          center: "title",
          end: "timeGridDay,timeGridWeek,dayGridMonth",
        },
        initialView: "timeGridWeek",
        locale: ruLocale,
        timeZone: "Asia/Almaty",
        selectable: false,
        select: this.createEvent,
        eventClick: null,
        eventContent: this.contentElement,
        selectConstraint: "businessHours",
        events: [],
        nowIndicator: true,
        firstDay: 1,
        slotDuration: "00:10:00",
        businessHours: [],
        slotMinTime: "09:00:00",
        slotMaxTime: "20:00:00",
      },
    };
  },
  methods: {
    maxAndMin(item, weekDay) {
      this.calendarOptions.businessHours.map((el) => {
        let daysOfWeek = el.daysOfWeek;
        if (daysOfWeek.includes(weekDay)) {
          item.max = el.endTime;
          item.min = el.startTime;
        }
      });
    },
    contentElement(item) {
      let props = item.event.extendedProps,
        start = new Date(item.event.startStr),
        end = new Date(item.event.endStr),
        endHours = end.getHours(),
        endMinutes = end.getMinutes(),
        startHours = start.getHours(),
        startMinutes = start.getMinutes();
      if (endHours < 10) endHours = "0" + endHours.toString();
      if (endMinutes < 10) endMinutes = "0" + endMinutes.toString();
      if (startHours < 10) startHours = "0" + startHours.toString();
      if (startMinutes < 10) startMinutes = "0" + startMinutes.toString();
      let teacherData = props.group.teacher.split(" "),
        teacher = "";
      if (teacherData.length !== 0)
        teacher = teacherData[1] + ". " + teacherData[0][0];
      else teacher = props.teacher;
      let abiData = props.group.mentor_for_boys.split(" "),
        abi = "";
      if (abiData.length !== 0) abi = abiData[1] + ". " + abiData[0][0];
      else teacher = props.teacher;
      let ablaData = props.group.mentor_for_girls.split(" "),
        abla = "";
      if (ablaData.length !== 0) abla = ablaData[1] + ". " + ablaData[0][0];
      else teacher = props.teacher;
      if (["timeGridDay", "timeGridWeek"].includes(item.view.type)) {
        return {
          html: `<div class="calendar-content"><b>${props.group.title}</b><br />
                 <b>${props.object.title}</b><br />
                 <small><em><b>${startHours}:${startMinutes} - ${endHours}:${endMinutes}</em></b></small>
                 <hr />
                 <small><em><b>Teacher: ${teacher}</em></b></small><br />
                 <small><em><b>Abi: ${abi}</em></b></small><br />
                 <small><em><b>Abla: ${abla}</em></b></small></div>`,
        };
      } else {
        return {
          html: `<b>${props.group.title} | ${props.object.title}</b>`,
        };
      }
    },

    createEvent(info) {
      let start = new Date(info.startStr),
        end = new Date(info.endStr),
        month = start.getMonth() + 1,
        endHours = end.getHours(),
        endMinutes = end.getMinutes(),
        startHours = start.getHours(),
        startMinutes = start.getMinutes();
      if (month < 10) month = "0" + month.toString();
      if (endHours < 10) endHours = "0" + endHours.toString();
      if (endMinutes < 10) endMinutes = "0" + endMinutes.toString();
      if (startHours < 10) startHours = "0" + startHours.toString();
      if (startMinutes < 10) startMinutes = "0" + startMinutes.toString();
      this.operation.create = true;
      this.form.create = {
        group: null,
        object: null,
        fromDateTime: startHours + ":" + startMinutes,
        toDateTime: endHours + ":" + endMinutes,
        date: start.getFullYear() + "-" + month + "-" + start.getDate(),
        comment: null,
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
          .post(`/booking/`, {
            group: this.form.create.group,
            object: this.form.create.object,
            start: `${this.form.create.date} ${this.form.create.fromDateTime}:00`,
            end: `${this.form.create.date} ${this.form.create.toDateTime}:00`,
            comment: this.form.create.comment,
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

    readElement(item) {
      let props = item.event.extendedProps,
        start = new Date(item.event.startStr),
        end = new Date(item.event.endStr),
        month = start.getMonth() + 1,
        endHours = end.getHours(),
        endMinutes = end.getMinutes(),
        startHours = start.getHours(),
        startMinutes = start.getMinutes(),
        fl = props.created_by.first_name + " " + props.created_by.last_name,
        email = props.created_by.email;
      if (month < 10) month = "0" + month.toString();
      if (endHours < 10) endHours = "0" + endHours.toString();
      if (endMinutes < 10) endMinutes = "0" + endMinutes.toString();
      if (startHours < 10) startHours = "0" + startHours.toString();
      if (startMinutes < 10) startMinutes = "0" + startMinutes.toString();
      this.operation.read = true;
      this.element = item;
      this.form.read = {
        group: props.group.id,
        object: props.object.id,
        created_by: fl.trim() ? fl : email,
        created_on: props.created_on,
        edited_on: props.edited_on,
        fromDateTime: startHours + ":" + startMinutes,
        toDateTime: endHours + ":" + endMinutes,
        date: start.getFullYear() + "-" + month + "-" + start.getDate(),
        comment: props.comment,
      };
    },

    updateElement(item) {
      let props = item.event.extendedProps,
        start = new Date(item.event.startStr),
        end = new Date(item.event.endStr),
        month = start.getMonth() + 1,
        endHours = end.getHours(),
        endMinutes = end.getMinutes(),
        startHours = start.getHours(),
        startMinutes = start.getMinutes(),
        fl = props.created_by.first_name + " " + props.created_by.last_name,
        email = props.created_by.email;
      if (month < 10) month = "0" + month.toString();
      if (endHours < 10) endHours = "0" + endHours.toString();
      if (endMinutes < 10) endMinutes = "0" + endMinutes.toString();
      if (startHours < 10) startHours = "0" + startHours.toString();
      if (startMinutes < 10) startMinutes = "0" + startMinutes.toString();
      this.operation.update = true;
      this.element = item;
      this.form.update = {
        id: item.event.id,
        group: props.group.id,
        object: props.object.id,
        created_by: fl.trim() ? fl : email,
        created_on: props.created_on,
        edited_on: props.edited_on,
        fromDateTime: startHours + ":" + startMinutes,
        toDateTime: endHours + ":" + endMinutes,
        date: start.getFullYear() + "-" + month + "-" + start.getDate(),
        comment: props.comment,
      };
      this.maxAndMin(this.form.update, start.getDay());
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
          .put(`/booking/${this.form.update.id}`, {
            group: this.form.update.group,
            object: this.form.update.object,
            start: `${this.form.update.date} ${this.form.update.fromDateTime}:00`,
            end: `${this.form.update.date} ${this.form.update.toDateTime}:00`,
            comment: this.form.update.comment,
          })
          .then((response) => {
            if (response.status === 200) {
              this.$store.dispatch("snackbar/setStatus", true);
              this.$store.dispatch("snackbar/setText", `Успешно`);
              loader.hide();

              this.operation.update = false;
              this.loadData();
              // this.element.event.extendedProps.object.id =
              //   response.data["object_info"]["id"];
              // this.element.event.extendedProps.object.title =
              //   response.data["object_info"]["title"];
              // this.element.event.extendedProps.start = response.data.start;
              // this.element.event.extendedProps.end = response.data.end;
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
      };
    },
    handlerDeleteElement() {
      const loader = this.$loading.show(this.$loadingParams);
      this.$restApi
        .delete(`/booking/${this.form.delete.id}`)
        .then((response) => {
          if (response.status === 204) {
            this.$store.dispatch("snackbar/setStatus", true);
            this.$store.dispatch("snackbar/setText", `Успешно`);
            loader.hide();

            this.operation.delete = false;
            this.operation.update = false;

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

    loadData() {
      const loader = this.$loading.show(this.$loadingParams);
      this.$restApi
        .get(`booking/`, {
          params: {
            group: this.filter.group,
            object: this.filter.object,
            created_by: this.filter.created_by,
          },
        })
        .then((response) => {
          if (response.status === 200) {
            this.calendarOptions.events = [];
            for (let i = 0; i < response.data.length; i++) {
              let el = response.data[i];
              el["textColor"] = el.object["text_color"];
              el["backgroundColor"] = el.object.background;
              if (el["is_active"] === true) {
                this.calendarOptions.events.push(el);
              }
            }
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

    // update permissions
    this.calendarOptions.selectable = this.hasPermission(
      ["booking_create"],
      this.user.permissions,
      this.user.role
    );

    this.calendarOptions.eventClick = this.hasPermission(
      ["booking_update"],
      this.user ? this.user.permissions : [],
      this.user ? this.user.role : ""
    )
      ? this.updateElement
      : this.readElement;

    // load group
    this.$restApi
      .get("handbook/group")
      .then((response) => {
        if (response.status === 200) {
          this.handbook.groups = [];
          for (let i = 0; i < response.data.length; i++) {
            this.handbook.groups.push({
              id: response.data[i].id,
              title: response.data[i].title,
            });
          }
        }
      })
      .catch((error) => {
        console.log(error);
      });

    // load object
    this.$restApi
      .get("handbook/object")
      .then((response) => {
        if (response.status === 200) {
          this.handbook.objects = [];
          for (let i = 0; i < response.data.length; i++) {
            this.handbook.objects.push({
              id: response.data[i].id,
              title: response.data[i].title,
            });
          }
        }
      })
      .catch((error) => {
        console.log(error);
      });

    // load created_by
    this.$restApi
      .get("account/?booking=1")
      .then((response) => {
        if (response.status === 200) {
          this.handbook.created_by = [];
          for (let i = 0; i < response.data.length; i++) {
            let fullName =
              response.data[i]["first_name"] +
              " " +
              response.data[i]["last_name"];
            if (fullName.trim().length === 0) {
              fullName = response.data[i].email;
            }
            this.handbook.created_by.push({
              id: response.data[i].id,
              full_name: fullName,
            });
          }
        }
      })
      .catch((error) => {
        console.log(error);
      });

    this.$restApi
      .get(`booking/business-hour`)
      .then((response) => {
        if (response.status === 200) {
          this.calendarOptions.businessHours = [];

          let els = {
            mon: 1,
            tue: 2,
            wen: 3,
            thu: 4,
            fri: 5,
            sat: 6,
            sun: 0,
          };
          for (const day in els) {
            if (response.data[day]) {
              this.calendarOptions.businessHours.push({
                daysOfWeek: [els[day]],
                startTime: response.data[day + "_start"],
                endTime: response.data[day + "_end"],
              });
            }
          }
          this.calendarOptions.slotMinTime = response.data.start;
          this.calendarOptions.slotMaxTime = response.data.end;
        }
      })
      .catch((error) => {
        console.log(error);
      });
  },
  computed: {
    user() {
      return this.$store.getters["user/user"];
    },
  },
};
</script>

<style>
.fc-event-main {
  overflow: hidden;
}
</style>
