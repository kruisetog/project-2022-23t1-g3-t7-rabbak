import { createRouter, createWebHistory } from "vue-router";
import PointsActivity from "../views/PointsActivity.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: PointsActivity,
    }
  ],
  linkExactActiveClass: "selected",
});

export default router;
