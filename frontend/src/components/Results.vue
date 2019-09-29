<template>
  <div id="results">
    <div class="navigation">
      <img src="../assets/path.svg" id="back" v-on:click="$router.push('/preferences')" />
      <span id="title">Your Surprise</span>
      <img id="logo" src="../assets/path-2881.svg" />
    </div>
    <div class="content">
      <div class="travel-path">
        <span id="start-departure-location">{{ results[result].start_name }}</span>
        <span id="start-departure-time">{{ results[result].start_time_go }}</span>
        <span id="start-arrival-location" class="surprise">Surprise</span>
        <span id="start-arrival-time">{{ /*results[result].start_time_go +*/ results[result].duration_go}}</span>

        <span id="return-departure-location" class="surprise">Surprise</span>
        <span id="return-departure-time">{{ results[result].start_time_return }}</span>
        <span id="return-arrival-location">{{ results[result].start_name }}</span>
        <span id="return-arrival-time">{{ results[result].start_time_return + results[result].duration_return}}</span>

        <span id="travel-date">{{ results[result].start_time_go }}</span>
      </div>
      <div class="tickets">
        <span id="ticket-count">Number of tickets</span>
        <span id="total-tickets-count" class="large">{{ user.personCountFull + user.personCountHalf}}</span>
        <span id="total-tickets-full" class="annotation">{{ user.personCountFull }} x full price</span>
        <span id="total-tickers-half" class="annotation">{{ user.personCountHalf }} x half price</span>
      </div>
      <div class="price">
        <span id="trip-price-title">Total price</span>
        <span id="price" class="large">Fr. {{ results[result].price_saver/100 }}</span>
        <span id="savings">Fr. {{ (results[result].price_normal - results[result].price_saver)/100 }} saved</span>
      </div>
    </div>
    <div class="footer">
      <button id="buy" v-on:click="buy">Book for Fr. {{ results[result].price_saver / 100 }}</button>
    </div>  
  </div>
</template>

<script>
export default {
  name: 'Results',
  data () {
    return {
      results: this.$parent.results,
      user: this.$parent.user,
      result: 1
    }
  },
  methods: {
    buy: function() {
      console.log(this.results);
    }
  }
}
</script>

<style scoped>

 #results > div {
    overflow: hidden;
  }

.navigation {
  width: 100%;
  background-color: #ea0100;
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
  width: 100px;
  height: 100px;
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

#buy {
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
.content > div {  
  width: 100%;
  border-bottom: solid 0.5px #b4b4b4;
  padding: 16px;
}

.travel-path {
  width: 100%;
  background-color: #000;
  color: #fff;
}

.travel-path span {  
  font-weight: bold;
  font-family: 'Source Sans Pro', sans-serif;
  font-size: 16px;
}

.surprise {
  padding: 4px;
  border-radius: 3px;
  background-color: #ea0100; 
}

#ticket-count, #trip-price-title {
  font-family: 'Source Sans Pro', sans-serif;
  font-size: 16px;
  font-weight: 300;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: 0.33px;
  color: #1e1e1e;
  display:block;
}

.large {
  font-family: 'Source Sans Pro', sans-serif;
  font-size: 22px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: 0.46px;
  color: #1e1e1e;
}

.annotation {
  font-family: 'Source Sans Pro', sans-serif;
  font-size: 12px;
  font-weight: 300;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: 0.25px;
  color: #7a7a7a;
  margin-left: 16px;
}

#savings {
  font-family: 'Source Sans Pro', sans-serif;
  border-radius: 10px;
  border: solid 1px #ea0100;
  font-size: 12px;
  font-weight: normal;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: 0.25px;
  color: #ea0100;
  padding: 2px 8px;
  position: relative;
  top: -2px;
  margin-left: 16px;
}
</style>