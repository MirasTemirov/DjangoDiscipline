import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import restApi from "./plugins/http";
import Loading from "vue-loading-overlay";
import "vue-loading-overlay/dist/vue-loading.css";
import store from "./store";
import vuetify from "./plugins/vuetify";

Vue.config.productionTip = false;
Vue.prototype.$restApi = restApi;
Vue.prototype.$loadingParams = {
  canCancel: false,
  color: "#e7e7e7",
  loader: "dots",
  width: 128,
  height: 128,
  backgroundColor: "#000",
  opacity: 0.7,
  zIndex: 10000,
};
Vue.use(Loading);

Vue.mixin({
  methods: {
    hasPermission: function (needlePermissions, userPermissions, userRole) {
      if (userRole === "admin") {
        return true;
      }

      if (needlePermissions === undefined || needlePermissions === null) {
        return true;
      }

      let res = true;
      for (let i = 0; i < needlePermissions.length; i++) {
        if (!userPermissions.includes(needlePermissions[i])) {
          res = false;
          break;
        }
      }

      return res;
    },
  },
});

new Vue({
  router,
  store,
  vuetify,
  render: function (h) {
    return h(App);
  },
}).$mount("#app");
