<template>
  <div id="start">
    <div class="navigation">
      <img src="../assets/group-5.svg" id="menu" />
      <span id="title">SBB Surprise</span>
      <img id="logo" src="../assets/path-2881.svg" />
    </div>
    <div class="content">
      <div id="location-selection">
        <span class="title">Start location</span>
        <img id="current-location-icon" src="../assets/location.svg" v-bind:hidden="startLocation != 'Current Location'" />
        <input  id="start-location" v-model="startLocation" type="text" v-on:click="startLocation = ''" />
      </div>
      <div id="departure-selection">
        <span class="title">Departure date and time</span>
        <input id="departure-date" v-model="departureDate" type="date" />
        <span class="separator"> </span>
        <button id="radio-early-departure" class="radio" v-on:click="departureTime='early'" v-bind:class="departureTime == 'early' ? 'radio-checked' : 'radio-unchecked'"></button>
        <span v-on:click="departureTime='early'">Early bird</span>
        <button id="radio-late-departure" class="radio" v-on:click="departureTime='late'" v-bind:class="departureTime == 'late' ? 'radio-checked' : 'radio-unchecked'"></button>
        <span v-on:click="departureTime='late'">Late riser</span>
      </div>
      <div id="return-selection">
        <span class="title">Return time</span>
        <input id="return-date" v-model="departureDate" type="date" disabled />
        <span class="separator"> </span>
        <button id="radio-early-return" class="radio" v-on:click="returnTime='early'" v-bind:class="returnTime == 'early' ? 'radio-checked' : 'radio-unchecked'"></button>
        <span v-on:click="returnTime='early'">Before dinner</span>
        <button id="radio-late-return" class="radio" v-on:click="returnTime='late'" v-bind:class="returnTime == 'late' ? 'radio-checked' : 'radio-unchecked'"></button>
        <span v-on:click="returnTime='late'">After</span>
      </div>
      <div id="budget-selection">
        <span class="title">Budget</span>
        <button class="budget" v-on:click="budget = 'low'" v-bind:class="budget == 'low' ? 'budget-selected' : ''" id="budget-low">$</button>
        <button class="budget" v-on:click="budget = 'med'" v-bind:class="budget == 'med' ? 'budget-selected' : ''" id="budget-med">$$</button>
        <button class="budget" v-on:click="budget = 'hi'" v-bind:class="budget == 'hi' ? 'budget-selected' : ''" id="budget-hi">$$$</button>
      </div>
      <div id="person-selection">
        <span class="title">Travellers</span>
        <div id="person-selection-full">
          <button id="remove-full" v-on:click="personCountFull--" v-bind:disabled="personCountFull == 0"></button>
          <span class="person-count" id="perosn-cout-full">{{ personCountFull }}</span>
          <button id="add-full"  v-on:click="personCountFull++" v-bind:disabled="personCountFull == 9"></button>
          <span class="person-description">adults 1/1</span>
        </div>
        <div id="person-selection-half">
          <button id="remove-half"  v-on:click="personCountHalf--" v-bind:disabled="personCountHalf == 0"></button>
          <span class="person-count" id="perosn-cout-half">{{ personCountHalf }}</span>
          <button id="add-half"  v-on:click="personCountHalf++" v-bind:disabled="personCountHalf == 9"></button>
          <span class="person-description">adults 1/2 <br />& children</span>
        </div>
      </div>
    </div>
    <div class="footer">
      <button id="surprise-me" v-on:click="supriseMe">Surprise me</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Start',
  props: {
    user: Object
  },
  data () {
    return {
      startLocation: "Current Location",
      departureDate: "",
      departureTime: "early",
      returnTime: "late",
      budget: "no",
      personCountFull: 1,
      personCountHalf: 0,
      preferences: []
    }
  },
  methods: {
    supriseMe: function () {
      this.$parent.user.startLocation = this.startLocation;
      this.$parent.user.departureDate = this.departureDate;
      this.$parent.user.departureTime = this.departureTime;
      this.$parent.user.returnTime = this.returnTime;
      this.$parent.user.budget = this.budget;
      this.$parent.user.personCountFull = this.personCountFull;
      this.$parent.user.personCountHalf = this.personCountHalf;
      this.$parent.user.preferences = this.preferences;
      this.$router.push('preferences')
    }
  }
}
</script>

<style scoped>
#start {
  width: 100%;
}
.navigation {
  width: 100%;
  background-color: #ea0100;
  padding: 16px;
  height: 16px;
}

#menu {
  float: left;
  width: 20px;
  height: 14px;
  object-fit: contain;
}

#title {
  font-size: 22px;
  font-weight: 300;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: 0.46px;
  text-align: center;
  color: #ffffff;
  position: relative;
  top: -6px;
  left: 100px;
}

#logo {
  width: 32px;
  height: 16px;
  object-fit: contain;
  float: right;
  display: block;
  position: relative;
  right: 32px;
}

.content > div {  
  width: 100%;
  border-bottom: solid 0.5px #b4b4b4;
  padding: 16px;
}

.title {
  width: 211px;
  height: 28px;
  font-size: 12px;
  font-weight: 300;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: 0.25px;
  color: #7a7a7a;
  display: block;
  font-family: 'Source Sans Pro', sans-serif;
}

input[type=text] , input[type=date] {
  font-family: 'Source Sans Pro', sans-serif;
  border: 0px;
  font-size: 16px;
  font-weight: 300;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: 0.33px;
  color: #444444;
}

#start-location {
  font-family: 'Source Sans Pro', sans-serif;
  border: 0px;
  font-size: 16px;
  font-weight: 300;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: 0.33px;
  color: #444444;
  width: 300px;
}

#current-location-icon {
  position: relative;
  top: 5px;
}

input[type=date] {
  width: 130px;
  font: inherit;
}

input[type=date]:disabled {
  background-color: white;
  color: #e5e5e5;
}

.separator {
  width: 2px;
  height: 20px;
  border: solid 0.5px #b4b4b4;
}

.radio {
  width: 14px;
  height: 14px;
  background-color: none;
  border: 0px;
  margin-left: 16px;
}

.radio-checked {
  background: url('../assets/group-3.svg') no-repeat;
}

.radio-unchecked {
  background: url('../assets/oval-copy-3.svg') no-repeat;
}

button.budget {
  width: 83px;
  height: 41px;
  border-radius: 4px;
  border: solid 0.5px #1e1e1e;
  background-color: #f6f6f6;
  color: #1e1e1e;
  margin-right: 8px;
}

button.budget-selected {
  background-color: #1e1e1e;
  color: #ffffff;
}

#add-full, #add-half, #remove-full, #remove-half {
  width: 18px;
  height: 18px;
  background-color: none;
  border: 0px;
}

#add-full, #add-half {
  background: url('../assets/group-6.png') no-repeat;
  margin-left: 8px;
}

#add-full:disabled, #add-half:disabled {
  background: url('../assets/group-7.png') no-repeat;
}

#remove-full, #remove-half {
  background: url('../assets/line-6-copy.png') no-repeat;
  position: relative;
  top: 9px;
  margin-right: 8px;
}

#remove-full:disabled, #remove-half:disabled {
  background: url('../assets/line-6-copy-5.png') no-repeat;
}


#person-selection {
  height: 130px;
}

#person-selection > div {
  width: 100px;
  text-align: center;
  float: left;
  margin-right: 16px;
}

.person-count {
  width: 23px;
  height: 24px;
  font-size: 22px;
  font-weight: 300;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: 0.46px;
  text-align: center;
}
.person-description {
  display: block;
  font-size: 16px;
  font-weight: 300;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: 0.33px;
  text-align: center;
  color: #444444;
  margin: 8px 0px;
}

.footer {
width: 100%;
  border-top: solid 1px #e5e5e5;
  background-color: #f6f6f6;
  position: absolute;
  bottom: -75px;
  width: 100%;
  padding: 16px;
}

#surprise-me {
  width: 304px;
  height: 50px;
  border-radius: 6px;
  border: 0px;
  font-family: 'Source Sans Pro', sans-serif;
  box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.1);
  background-color: #ea0100;
  font-size: 16px;
  font-weight: 300;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: 0.33px;
  text-align: center;
  color: #ffffff;
  margin: 16px 19px;
}

#start {
  overflow: hidden;
}
</style>