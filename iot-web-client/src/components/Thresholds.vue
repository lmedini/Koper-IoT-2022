<script>
import { useStore } from '@/stores/store'

import Slider from '@vueform/slider'

let store

export default {
  components: {
    Slider,
  },
  props: ["min", "max"],
  setup() {
    store = useStore()
    return {
        getThresholds() { return store.sliderValues},
        setThresholds(newThresholds) { return store.updateThresholds(newThresholds)}
    }
  },
}

</script>

<template>
    <div>
        <br>
        <br>
        <Slider id="tempSlider" :min="min/1" :max="max/1" :step='-1/1' :value="this.getThresholds()" @change="setThresholds" />
    </div>
</template>
<style src="@vueform/slider/themes/default.css"></style>