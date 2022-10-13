import { createRouter, createWebHistory } from "vue-router";
import PointsActivity from "../views/PointsActivity.vue";
import Settings from "../views/Settings.vue";
import Login from "../views/Login.vue"
import uploadFile from "../views/UploadFile.vue"
import addTransaction from "../views/AddTransaction.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Login",
      component: Login,
      meta: {
        hideCustNav: true,
        hideStaffNav: true
       }
    },
    {
      path: "/activity",
      name: "My Points Activity",
      component: PointsActivity,
      meta: {
        hideCustNav: false,
        hideStaffNav: true
       }
    },
    {
      path: "/settings",
      name: "settings",
      component: Settings,
      meta: {
        hideCustNav: false,
        hideStaffNav: true
       }
    },
    {
      path: "/uploadFile",
      name: "uploadFile",
      component: uploadFile,
      meta: {
        hideCustNav: true,
        hideStaffNav: false
       }
    },
    {
      path: "/addTransaction",
      name: "addTransaction",
      component: addTransaction,
      meta: {
        hideCustNav: true,
        hideStaffNav: false
       }
    },{
      path: "/:logout",
      name: "logOut",
      component: Login,
      meta: {
        hideCustNav: true,
        hideStaffNav: true
       }
    },

  ],
  linkExactActiveClass: "selected",
});

export default router;
