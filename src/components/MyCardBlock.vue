<script setup>
const props = defineProps({
    cardid: {
        type: String,
        required: true
    },
    cardNum:{
        type: String,
        required: true
    },
    cardType:{
        type: String,
        required: true
    }
})
</script>

<template>
    <tr>
        <td>
           {{cardNum}}
        </td>
        <td>
            {{cardType}}
        </td>
        <td>
            <!-- <slot name="deleteCard"></slot> -->
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