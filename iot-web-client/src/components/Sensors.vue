<script>
import Temperature from "./Temperature.vue";
import Activity from "./Activity.vue";

export default {
  components: {
    Temperature,
    Activity,
  },
};
</script>

<template>
  <div class="grid-item">
    <Temperature />
  </div>
  <div class="grid-item">
    <Activity />
  </div>
</template>

<style scoped>
.grid-item {
  grid-column: auto;
}
.grid-item1 {
  grid-column-start: 0;
  grid-column-end: 1;
}
.grid-item2 {
  grid-column-start: 1;
  grid-column-end: 2;
}
</style>