import { createRouter, createWebHistory } from "vue-router";
import PointsActivity from "../views/PointsActivity.vue";
import Settings from "../views/Settings.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/activity",
      name: "My Points Activity",
      component: PointsActivity,
    },
    {
      path: "/settings",
      name: "settings",
      component: Settings,
    }
  ],
  linkExactActiveClass: "selected",
});

export default router;
