<script setup>
    import Temperature from './Temperature.vue'
    import Activity from './Activity.vue'
    import Actuators from './Actuators.vue'
</script>
<template>
    <h2>Dashboard</h2>
    <hr>
    <h3><em>Sensors</em></h3>
    <Temperature />
    <Activity />
    <hr>
    <h3><em>Actuators</em></h3>
    <Actuators />
</template>
<style scoped>

</style>