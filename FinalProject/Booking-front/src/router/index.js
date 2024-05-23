import Vue from "vue";
import VueRouter from "vue-router";
import store from "@/store";

Vue.use(VueRouter);

const ifAuthenticated = (to, from, next) => {
  if (!store.getters["user/user"]) {
    next();
    return;
  }
  next("/");
};

const routes = [
  {
    path: "/",
    name: "MainPage",
    component: () => import("../layouts/MainLayout.vue"),
    redirect: "/schedule",
    children: [
      {
        path: "/schedule",
        name: "Schedule",
        component: () => import("../views/Schedule.vue"),
      },
      {
        path: "/login",
        name: "Login",
        component: () => import("../views/auth/Login.vue"),
        beforeEnter: ifAuthenticated,
      },
      {
        path: "/handbook/object",
        name: "Object",
        component: () => import("../views/handbook/Object.vue"),
      },
      {
        path: "/handbook/group",
        name: "Group",
        component: () => import("../views/handbook/Group.vue"),
      },
      {
        path: "/account",
        name: "Account",
        component: () => import("../views/Account.vue"),
      },
      {
        path: "/log",
        name: "Log",
        component: () => import("../views/Log.vue"),
      },
      {
        path: "/business-hour",
        name: "BusinessHour",
        component: () => import("../views/BusinessHour.vue"),
      },
      {
        path: "/profile",
        name: "Profile",
        component: () => import("../views/auth/Profile.vue"),
      },
      {
        path: "/password",
        name: "Password",
        component: () => import("../views/auth/Password.vue"),
      },
      {
        path: "/analytics",
        name: "Analytics",
        component: () => import("../views/Analytics.vue"),
      },
    ],
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
