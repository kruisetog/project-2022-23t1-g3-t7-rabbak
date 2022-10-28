<script setup>
defineProps({
    excludeProcessing: {
        type: Boolean,
        required: false,
        default: false
    } ,
    date: {
        type: String,
        required: true
    },
    desc:{
        type: String,
        required: true
    },
    cardType:{
        type: String,
        required: true
    },
    amount:{
        type: String,
        required: true
    },
    benefit:{
        type: String,
        required: true
    }
})
</script>

<template>
    <tr v-bind:style=" excludeProcessing ? 'background-color:#ffd8d4;' : 'background-color:none;' ">
        <td>
            {{date}}
        </td>
        <td>
           {{desc}}
        </td>
        <td>
            {{cardType}}
        </td>
        <td>
            {{amount}}
        </td>
        <td>
            {{benefit}}
        </td>
    </tr>
</template>