import { defineStore } from 'pinia'

export const useStore = defineStore({
  id: 'regulationStore',
  state: () => ({
    minT: 20,
    maxT: 22,
    temperature: 0,
    activity: 0
  }),
  getters: {
    sliderValues: (state) => [state.minT, state.maxT]
  },
  actions: {
    updateTemperature() {
      // TODO: send request to the server and update the temperature variable
      console.log("updateTemperature...");
      this.temperature = 15 + Math.random() * Math.floor(25);
    },

    updateActivity() {
      // TODO: send request to the server and update the activity variable
      console.log("updateActivity...");
      this.activity = Math.random() * Math.floor(100);
    },

    userUpdateMinT(minVal) {
      this.minT = minVal;
      if (this.maxT < this.minT)
        this.maxT = this.minT;
      console.log("MinT set to ", this.minT);
    },
    userUpdateMaxT(maxVal) {
      this.maxT = maxVal;
      if (this.minT > this.maxT)
        this.minT = this.maxT;
      console.log("MaxT set to ", this.maxT);
    },
    updateThresholds(val) {
      if (val[0] !== this.minT) {
        this.userUpdateMinT(val[0]);
      }
      if (val[1] !== this.maxT) {
        this.userUpdateMaxT(val[1]);
      }
    },
    updateActuators() {
      let choice;
      if (this.temperature < this.minT) {
        choice = "heat";
      } else {
        if (this.temperature > this.maxT) {
          choice = "cool";
        } else {
          choice = "none";
        }
      }
      // TODO: send request to the server to update the actuators values
      console.log("updateActuators...", choice);
      return choice;
    }
  }
})
