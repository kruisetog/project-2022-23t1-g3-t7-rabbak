<script setup>
defineProps({
    title: {
        type: String,
        required: true
    }
})
</script>

<script>
export default {
    data() {
        return{
            show:true
        }
    },
    methods: {
      close(){
        this.show=false;
        this.$emit('close', "close");
      }
    }
};
</script>

<template>
    <div v-show="show" class="row successRow">
        <div class="col-12 text-center">
            <img class="img-fluid mx-auto d-block" src="../assets/tick.png"/><br>
            <h4 class="text-capitalize text-center">{{title}}</h4>
            <h6 class="text-capitalize text-center">{{title}} Success</h6>
            <button type="button" @click="close" class="btn btn-primary w-50">OK</button>
        </div>
    </div>
    <br>
</template>

<style scoped>
.successRow{
    padding-top:30px
}

@media only screen and (min-width: 1000px) {
    img{
    width:20%;
    height:60%
}
}
</style>