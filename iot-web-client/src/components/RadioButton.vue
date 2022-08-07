<template>
  <h1 class="mb-6 pt-6 mx-auto max-w-sm">{{ title }}</h1>
  <div class="mx-auto max-w-sm text-center flex flex-wrap"
    :class="{'flex-col': type == 'col'}"
  >
    <div v-for="(option, index) in options" :key="index"
      class="flex items-center mr-4 mb-4"
    >
      <input :id="'radio'+(index+1)" type="radio" name="radio" class="hidden"
        :value="option.value"
        :checked="choice == option.value" @change="$emit('update:choice', $event.target.value)"
      />
      <label :for="'radio'+(index+1)" class="flex items-center cursor-pointer"
        :class="{'text-blue-600': choice == option.value}"
      >
        <span class="w-4 h-4 inline-block mr-1 rounded-full border border-gray-400"
          :class="{'bg-blue-600': choice == option.value}"
          :style="choice == option.value ? 'box-shadow: 0px 0px 0px 2px white inset;' : ''"
        ></span>
        {{ option.text }}
      </label>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    type: { type: String, default: 'row' },
    title: { type: String, default: '' },
    options: { type: Array, default: true },
    choice: { type: String, required: true }
  },
  emits: ['update:choice']
}
</script>

<style scoped>
input[type="radio"] + label span {
  transition: background .2s, transform .2s;
}

input[type="radio"] + label span:hover,
input[type="radio"] + label:hover span{
  transform: scale(1.2);
}
</style>
