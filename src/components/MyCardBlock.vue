<script setup>
const props = defineProps({
    cardid: {
        type: String,
        required: true
    }
    ,cardNum:{
        type: String,
        required: true
    }
})
</script>

<template>
    <tr>
        <td>
            <slot name="cardNum"></slot>
        </td>
        <td>
            <slot name="cardType"></slot>
        </td>
        <td>
            <button :bind=cardNum :value=cardid v-on:click.native="deleteCard($event)" class="btn btn-danger">Delete Card</button>
        </td>
    </tr>
</template>

<script>
export default {
    data(){
        return{
            showDeleteCard: true,
            buttonValue: ""
        }
    },
    methods: {
        deleteCard: function(e) {
            e.preventDefault();
            const buttonValue = e.target.value;
            this.buttonValue = buttonValue;
            this.$emit("showDeleteCard", buttonValue, this.cardNum);
            
        }
    }
};
</script>