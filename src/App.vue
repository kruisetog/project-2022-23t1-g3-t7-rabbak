<script setup>
import { RouterLink, RouterView } from "vue-router";
import Nav from "./components/nav.vue";
</script>

<template>
  <div class="main-cont">
    <div class="nav-side">
      <Nav></Nav>
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
