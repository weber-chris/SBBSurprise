<template>
  <div id="preferences">
    <div v-bind:hidden="page!=1">
      <div class="navigation">
        <img src="../assets/path.svg" id="back" v-on:click="$router.push('/')" />
        <span id="title">SBB Surprise</span>
        <img id="logo" src="../assets/path-2881.svg" />
      </div>
      <div class="content">
        <span id="prompt">Tell us something about you</span>
        <span id="tip">Tap on the images you like</span>

        <img v-bind:class="preferences.includes(categories[0].name) ? 'selected' : ''" v-bind:src="categories[0].img" v-on:click="preferences.push(categories[0].name)" />
        <img v-bind:class="preferences.includes(categories[1].name) ? 'selected' : ''" v-bind:src="categories[1].img" v-on:click="preferences.push(categories[1].name)" />
        <img v-bind:class="preferences.includes(categories[2].name) ? 'selected' : ''" v-bind:src="categories[2].img" v-on:click="preferences.push(categories[2].name)" />
        <img v-bind:class="preferences.includes(categories[3].name) ? 'selected' : ''" v-bind:src="categories[3].img" v-on:click="preferences.push(categories[3].name)" />
        <img v-bind:class="preferences.includes(categories[4].name) ? 'selected' : ''" v-bind:src="categories[4].img" v-on:click="preferences.push(categories[4].name)" />
        <img v-bind:class="preferences.includes(categories[5].name) ? 'selected' : ''" v-bind:src="categories[5].img" v-on:click="preferences.push(categories[5].name)" />
        

      </div>
      <div class="footer">
        <span id="progress">1/2</span>
        <button id="next" v-on:click="page=2">Next</button>
        <span id="skip" v-on:click="getOffers">Skip this step</span>
      </div>
    </div>
    <div v-bind:hidden="page!=2">
      <div class="navigation">
        <img src="../assets/path.svg" id="back" v-on:click="page=1" />
        <span id="title">SBB Surprise</span>
        <img id="logo" src="../assets/path-2881.svg" />
      </div>
      <div class="content">
        <span id="prompt">Interesting, what about these?</span>
        <span id="tip">Tap on the images you like</span>

        <img v-bind:class="preferences.includes(categories[6].name) ? 'selected' : ''" v-bind:src="categories[6].img" v-on:click="preferences.push(categories[6].name)" />
        <img v-bind:class="preferences.includes(categories[7].name) ? 'selected' : ''" v-bind:src="categories[7].img" v-on:click="preferences.push(categories[7].name)" />
        <img v-bind:class="preferences.includes(categories[8].name) ? 'selected' : ''" v-bind:src="categories[8].img" v-on:click="preferences.push(categories[8].name)" />
        <img v-bind:class="preferences.includes(categories[9].name) ? 'selected' : ''" v-bind:src="categories[9].img" v-on:click="preferences.push(categories[9].name)" />
        <img v-bind:class="preferences.includes(categories[10].name) ? 'selected' : ''" v-bind:src="categories[10].img" v-on:click="preferences.push(categories[10].name)" />
        <img v-bind:class="preferences.includes(categories[11].name) ? 'selected' : ''" v-bind:src="categories[11].img" v-on:click="preferences.push(categories[11].name)" />
        

      </div>
      <div class="footer">
        <span id="progress">2/2</span>
        <button id="next" v-on:click="getOffers">Finish</button>
        <span id="skip" v-on:click="getOffers">Skip this step</span>
      </div>
    </div>
    <div id="loading-screen" v-bind:hidden="page!=3">
      <div class="navigation-transparent">
        <span id="title">SBB Surprise</span>
        <img id="logo" src="../assets/path-2881.svg" />
      </div>
      <div id="prompt-white">
        Let's find your unique trip...
      </div>
      <div id="tip-white">
        This can take a few seconds
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'Preferences',
  props: ['user'],
  loading: false,
  data () {
    return {
      page: 1,
      preferences: [],
      categories: [
        {name: 'SBB_lh_games_fun', img: '/static/Games_and_fun.jpg'},
        {name: 'SBB_lh_adventure_panorama_trips', img: '/static/Adventure_and_panarama_trips.jpg'},
        {name: 'SBB_lh_nature_sights_of_interest', img: '/static/Nature_and_sights_of_interest.jpg'},
        {name: 'SBB_lh_zoo_animal_parks', img: '/static/Zoos_and_animal_parks.jpg'},
        {name: 'SBB_lh_bike_ebike', img: '/static/Bike_and_eBike.jpg'},
        {name: 'SBB_lh_wellness_relaxation', img: '/static/Wellness_and_relaxation.jpg'},
        {name: 'SBB_lh_hiking', img: '/static/Hiking.jpg'},
        {name: 'SBB_lh_art_culture_museums', img: '/static/Art_culture_and_museums.jpg'},
        {name: 'SBB_lh_concerts_musicals_festivals', img: '/static/Concerts_musicals_festivals.jpg'},
        {name: 'SBB_lh_markets_shopping', img: '/static/Markets_shopping_and_culinary_art.jpg'},
        {name: 'SBB_lh_short_trips_in_switzerland', img: '/static/Short_trips_in_Switzerland.jpg'},
        {name: 'SBB_lh_city_trips', img: '/static/CityTrips.jpg'}
      ]
    }
  },
  methods: {
    getOffers: function () {
      this.$parent.user.preferences = this.preferences;
      console.log(this.$parent.user);
      this.loading = true;
      this.page = 3;
      this.$http.post("/", this.$parent.user)
        .then((result) => {
        this.data = result.data;
        console.log(this.data);
        this.$parent.results = this. data;
        this.loading = false;
        this.$router.push('results');
      })
    }
  }
}
</script>

<style scoped>

.navigation {
  width: 100%;
  background-color: #ea0100;
  padding: 16px;
  height: 16px;
}

.navigation-transparent {
  width: 100%;
  padding: 16px;
  height: 16px;
}

#back {
  float: left;
  width: 13px;
  height: 22px;
  object-fit: contain;
  position: relative;
  top: -2px;
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

#prompt {
  width: 211px;
  height: 60px;
  font-family: 'Source Sans Pro', sans-serif;
  font-size: 22px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: 1.36;
  letter-spacing: 0.46px;
  text-align: center;
  color: #000000;
  display: block;
  margin: auto;
  margin-top: 32px;
}

#prompt-white {
  width: 211px;
  height: 60px;
  font-family: 'Source Sans Pro', sans-serif;
  font-size: 22px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: 1.36;
  letter-spacing: 0.46px;
  text-align: center;
  color: #fff;
  display: block;
  margin: auto;
  margin-top: 64px;
}

#tip-white {
    font-size: 12px;
  font-weight: 300;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: 0.25px;
  color: #fff;
  display: block;
  font-family: 'Source Sans Pro', sans-serif;
  margin: auto;
  text-align: center;
  margin-top: 8px;
}

#tip, #progress, #skip {
  font-size: 12px;
  font-weight: 300;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: 0.25px;
  color: #7a7a7a;
  display: block;
  font-family: 'Source Sans Pro', sans-serif;
  margin: auto;
  text-align: center;
  margin-top: 8px;
}

#skip {
  font-size: 16px;
}


.content > img {
  width: 130px;
  height: 100px;
  margin-left: 32px;
  margin-top: 32px;
  border: solid 2px #fff;
}

img.selected {
  border-radius: 4px;
  border: solid 2px #ea0100;
}

.footer {
width: 100%;
  border-top: solid 1px #e5e5e5;
  background-color: #f6f6f6;
  position: absolute;
  bottom: 0px;
  width: 100%;
  padding: 16px;
}

#next {
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

#loading-screen {
  width: 100vw;
  height: 100vh;
  background-image: url('../assets/claudio-schwarz-purzlbaum-xnHSJ_6y2Io-unsplash.jpg');
  background-size: 375px 812px;
  -webkit-filter: sepia(50%) hue-rotate(0deg) saturate(70%);
  filter: sepia(50%) hue-rotate(0deg) saturate(70%);
  overflow: hidden;
  }

  #preferences > div {
    overflow: hidden;
  }

  .footer > span {
    position: relative;
    right: 16px;
  }

</style>