import { defineStore } from 'pinia'

// The base URL for the API.
// Better to use an URL on the same server to avoid CORS issues
const API_SERVER_BASE_URL = "../iot-api/";

export const useStore = defineStore({
  id: 'regulationStore',
  state: () => ({
    minT: 20,
    maxT: 22,
    temperature: 0,
    activity: 0,
    heat: false,
    cool: false,
    choice: 'none'
  }),
  getters: {
    sliderValues: (state) => [state.minT, state.maxT],
    choiceValue: (state) => state.heat?"heat":(state.cool?"cool":"none")
  },
  actions: {
    updateTemperature() {
      // Send request to the server and update the temperature variable
      //this.temperature = 15 + Math.random() * Math.floor(25);
      fetch(API_SERVER_BASE_URL + "temp/0").then(res => res.json()).then((json) => {
        const table = json.temperature_values;
        this.temperature = table[table.length - 1];
      })
    },

    updateActivity() {
      // Send request to the server and update the activity variable
      //this.activity = Math.random() * Math.floor(100);
      fetch(API_SERVER_BASE_URL + "act/0").then(res => res.json()).then((json) => {
        const table = json.activity_values;
        this.activity = table[table.length - 1];
      })

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
    async updateActuators() {
      // Send request to the server to update the actuators values
      let choice, response, json, table;
      response = await fetch(API_SERVER_BASE_URL + "heat/0");
      json = await response.json();
      table = json.heat_values;
      const heatValue = table[table.length - 1];

      response = await fetch(API_SERVER_BASE_URL + "cool/0");
      json = await response.json();
      table = json.cool_values;
      const coolValue = table[table.length - 1];

      if (this.temperature < this.minT) {
        choice = "heat";
        if (heatValue === "False") { // if heater was not already started
          console.log('HEAT');
          // send heating request
          fetch(API_SERVER_BASE_URL + "heat/1", { method: "PUT"});
          if (coolValue === "True") { // if the cooler was also on
            // send not cooling request
            fetch(API_SERVER_BASE_URL + "cool/0", { method: "PUT"});
          }
        }
      } else {
        if (this.temperature > this.maxT) {
          choice = "cool";
          if (coolValue === "False") { // if cooler was not already started
            console.log('COOL');
            // send cooling request
            fetch(API_SERVER_BASE_URL + "cool/1", { method: "PUT"});
            if (heatValue === "True") { // if the heater was also on
              // send not heating request
              fetch(API_SERVER_BASE_URL + "heat/0", { method: "PUT"});
            }
          }
        } else {
          choice = "none";
          // Shut everything off
          if (heatValue === "True") {
            // send not heating request
            fetch(API_SERVER_BASE_URL + "heat/0", { method: "PUT"});
          }
          if (coolValue === "True") {
            // send not cooling request
            fetch(API_SERVER_BASE_URL + "cool/0", { method: "PUT"});
          }
        }
      }
      this.choice = choice;
    }
  }
})
