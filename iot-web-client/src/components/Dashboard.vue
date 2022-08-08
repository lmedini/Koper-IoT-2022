<script setup>
import Temperature from "./Temperature.vue";
import Sensors from "./Sensors.vue";
import Actuators from "./Actuators.vue";
</script>
<template>
  <h2>Dashboard</h2>
  <hr />
  <h3><em>Sensors</em></h3>
  <Sensors class="grid-container" />
  <hr />
  <h3><em>Actuators</em></h3>
  <Actuators class="grid-container" />
</template>
<style scoped>
.grid-container {
  display: grid;
}

@media (min-width: 512px) {
  .grid-container {
    grid-template-columns: 1fr 1fr;
  }
}
</style>