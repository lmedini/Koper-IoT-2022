<script>
import { ref } from "vue";
import { useStore } from "@/stores/store";
import RadioButton from "./RadioButton.vue";

export default {
  components: {
    RadioButton,
  },
  data() {
    return {
      heater: true,
      cooler: false,
      window: false,
    };
  },
  created() {
    setInterval(this.updateActuators, 1000);
  },
  setup() {
    const store = useStore();

    // DATA
    const type = ref("col"); // row or col
    const title = ref("Functioning actuators:");
    const options = ref([
      { text: "Heater", value: "heat" },
      { text: "Cooler", value: "cool" },
      { text: "Window (optional)", value: "open" },
      { text: "none", value: "none" },
    ]);

    return {
      type,
      title,
      options,
      choice: 'none',
      updateActuators: store.updateActuators
    };
  },
};
</script>

<template>
  <div class="container bg-gray-200 m-auto p-40 min-h-screen">
    <radio-button
      :type="type"
      :title="title"
      :options="options"
      :choice="this.updateActuators()"
    />
  </div>
</template>

<style scoped>
input[type="radio"] + label span {
  transition: background 0.2s, transform 0.2s;
}
input[type="radio"] + label span:hover,
input[type="radio"] + label:hover span {
  transform: scale(1.2);
}
</style>