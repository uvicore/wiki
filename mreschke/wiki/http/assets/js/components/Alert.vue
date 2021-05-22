// src/Alert.vue
<template>
    <div class="alert" v-text="message"></div>
</template>

<script>
export default {
    data() {
        return {
            message: 'I am an alert4.'
        };
    }
};
</script>

<style>
.alert {
    background: red;
}
</style>
