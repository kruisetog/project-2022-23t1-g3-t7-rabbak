<script>
export default {
    methods: {
        logout(){
        this.show=false;
        this.$emit('logout', "logout");
      }
    }
};
</script>

<template>
    <div class="float-right mt-5 pt-5">
    <span class="logout">
        <i class="icon-signout primary font-large-2"></i>
   <a @click="logout">LOGOUT</a></span>
    </div>
</template>