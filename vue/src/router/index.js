import { createRouter, createWebHistory } from "vue-router";

import Home from "@/views/Home.vue";
import Policy from "@/views/Policy.vue";

const routes = [
  { path: "/", name: "home", component: Home },
  { path: "/policy", name: "policy", component: Policy },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
