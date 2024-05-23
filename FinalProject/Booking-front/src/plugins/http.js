import axios from "axios";
import store from "@/store";
import router from "@/router";

const restApi = axios.create({
  baseURL: "http://localhost:8000/api/v1/",
});

restApi.interceptors.request.use(
  (config) => {
    const token = store.getters["user/token"];
    if (token) {
      config.headers["Authorization"] = `JWT ${token}`;
    }
    return config;
  },
  (error) => {
    if (error.response) {
      if (error.response.status === 401) {
        store.dispatch("user/logoutUser", {}, { root: true });
        router.push({ name: "Login" });
      }
    }
    return Promise.reject(error);
  }
);

restApi.interceptors.response.use(
  function (response) {
    return response;
  },
  function (error) {
    if (error.response) {
      if (error.response.status === 401) {
        store.dispatch("user/logoutUser", {}, { root: true });
        router.push({ name: "Login" });
      }
    }
    return Promise.reject(error);
  }
);

export default restApi;
