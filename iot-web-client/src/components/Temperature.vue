<script>
import { useStore } from "@/stores/store";
import VueThermometer from "vuejs-thermometer/src/components/VueThermometer.vue";

export default {
  components: {
    VueThermometer,
  },
  data() {
    return {
      options: {
        text: {
          color: "black",
          fontSize: 10,
          textAdjustmentY: 2,
          fontFamily: "Arial",
          textEnabled: true,
        },
        thermo: {
          color: "#FF0000",
          backgroundColor: "#fcf9f9",
          frameColor: "black",
          ticks: 10,
          ticksEnabled: true,
          tickColor: "black",
          tickWidth: "1",
        },
        layout: {
          height: 300,
          width: 90,
        },
      },
    };
  },
  setup() {
    const store = useStore();
    return {
      getTemp() {
        return store.temperature;
      },
      updateTemperature: store.updateTemperature
    };
  },
  created() {
    setInterval(this.updateTemperature, 1000);
  },
};

</script>

<template>
  <h3>Temperature: {{ this.getTemp() }}</h3>
  <vue-thermometer :value="this.getTemp()" :min="5" :max="40" />
</template>

<style scoped>
</style>