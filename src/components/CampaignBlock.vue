<script setup>
// defineProps({
//     campaignName: {
//         type: String,
//         required: true
//     },
//     expiryText: {
//         type: String,
//         required: true
//     },
//     progress: {
//         type: String,
//         required: true
//     },
//     campaignDesc:{
//         type: String,
//         required: true
//     }
// })
</script>

<template>
    <div class="row campaign pt-3">
        <div class="col-6">
            <h6 class="text-capitalize"><slot name="campaignName"></slot></h6>
            <!-- <div class="progress-bar-cont">
                <div class="progress-bar" :content="ddd" :style="'width: '+progress + '%'"></div>
            </div>
            <span class="progress-text">{{progress}}%</span> -->
        </div>
        <div class="col-6">
            <span class="campaignName text-capitalize"><slot name="campaignDesc"></slot></span>
            <div class="expire">Campaign Ends On <slot name="endDate"></slot></div>
        </div>
    </div>
    <br>
</template>

<style scoped>
.expire{
    color:grey;
}
.campaign{
    background-color:#f0f5fb;
}
.progressText{
    float:right;
}
.progress-bar-cont{
    background: white;
    border-radius: 10px;
    margin-top: 4px;
}
.progress-bar{
    height: 10px;
    border-radius: 10px;
    color: #a8bcd6!important;
    background-color: #a8bcd6!important;
}

.progress-text{
    float:right;
}
</style>