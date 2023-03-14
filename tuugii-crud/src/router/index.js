import { createRouter, createWebHashHistory } from 'vue-router'

const path = (path, name, componentPath = {}, args = {}) => {
  return { path, name, component: () => import(`../views/${componentPath}`), ...args };
};

const routes = [
  path('/','home', 'HomeView.vue'),
  path('/about','about','AboutView.vue'),
  path('/upload','Upload','upload.vue'),
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
