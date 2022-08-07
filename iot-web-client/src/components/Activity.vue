<script>
import { useStore } from "@/stores/store";
import VueSpeedometer from "vue-speedometer"

export default {
  components: {
    VueSpeedometer
  },
  setup() {
    const store = useStore();
    return {
      getActivity() {
        return store.activity;
      },
      updateActivity: store.updateActivity
    };
  },
  created() {
    setInterval(this.updateActivity, 5000);
  },
}
</script>

<template>
    <h3>Activity level: {{ this.getActivity() }}</h3>

<vueSpeedometer :minValue="0" :maxValue="100" :value="this.getActivity()"></vueSpeedometer>
</template>

<style scoped>
</style>