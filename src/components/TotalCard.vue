<script setup>
defineProps({
    cashbacks: {
    type: String,
    required: true
  },
     loyaltyPoints: {
    type: String,
    required: true
  },
  miles: {
    type: String,
    required: true
  }
})
</script>

<template>
    <div class="card col-lg-4  text-justify">
        <div class="card-content">
        <div class="card-body">
            <div class="media">
            <div class="align-self-center">
                <i class="icon-money icon-2x"></i>
            </div>
            <div class="media-body text-right">
                <h3>{{cashbacks}}</h3>
                <span>Cashbacks</span>
            </div>
            </div>
        </div>
        </div>
    </div>
    <div class="card col-lg-4">
        <div class="card-content">
        <div class="card-body">
            <div class="media">
            <div class="align-self-center">
                <i class="icon-bell-alt icon-2x"></i>
            </div>
            <div class="media-body text-right">
                <h3>{{loyaltyPoints}}</h3>
                <span>Loyalty Points</span>
            </div>
            </div>
        </div>
        </div>
    </div>
    <div class="card col-lg-4">
        <div class="card-content">
        <div class="card-body">
            <div class="media">
            <div class="align-self-center">
                <i class="icon-suitcase icon-2x"></i>
            </div>
            <div class="media-body text-right">
                <h3>{{miles}}</h3>
                <span>Miles</span>
            </div>
            </div>
        </div>
        </div>
    </div>
</template>

<style scoped>
.icon-money{
    color:#40bdc7;
}
.icon-bell-alt{
    color: #f7eb63;
}
.icon-suitcase{
    color:#877bed;
}
.media{
    display:contents
}
</style>