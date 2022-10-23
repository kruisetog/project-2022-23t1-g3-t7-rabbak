<script setup>
import { RouterLink, RouterView } from "vue-router";
import custNav from "./components/custNav.vue";
import staffNav from "./components/staffNav.vue";
</script>

<template>
  <div class="main-cont">
    <div class="nav-side">
      <custNav v-if="!$route.meta.hideCustNav"></custNav>
      <staffNav v-if="!$route.meta.hideStaffNav"></staffNav>
    </div>
    <div class="large-side">
      <RouterView />
    </div>
  </div>
</template>

<style scoped>
.main-cont {
  display: flex;
}

.large-side{
  width: 100%;
  margin-left: 130px;
  padding-right:15px;
}
</style>

 