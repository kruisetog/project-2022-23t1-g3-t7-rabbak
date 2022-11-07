<script setup>
defineProps({
    excludeProcessing: {
        type: Boolean,
        required: true,
        default: false
    }
})
</script>


<template>
    <tr v-bind:style=" !excludeProcessing ? 'background-color:none;' : 'background-color:#ffd8d4;' ">
        <td>
           <slot name="date"></slot>
        </td>
        <td>
            <slot name="description"></slot>
        </td>
        <td>
            <slot name="cardType"></slot>
        </td>
        <td>
            <slot name="amount"></slot>
        </td>
        <td>
            <slot name="benefit"></slot>
        </td>
    </tr>
</template>