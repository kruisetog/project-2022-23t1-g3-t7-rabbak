<script setup>
defineProps({
    excludeProcessing: {
        type: Boolean,
        required: false,
        default: false
    }
})
</script>

<template>
    <tr v-bind:style=" excludeProcessing ? 'background-color:#ffd8d4;' : 'background-color:none;' ">
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