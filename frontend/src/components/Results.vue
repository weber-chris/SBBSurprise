<template>
  <div id="results">
    <div class="navigation">
      <img src="../assets/path.svg" id="back" v-on:click="$router.push('/preferences')" />
      <span id="title">Your Surprise</span>
      <img id="logo" src="../assets/path-2881.svg" />
    </div>
    <div class="content">
      <div class="travel-path">
        <table>
          <tr>
            <td>
              <span id="start-departure-location">{{ results[result].start_name }}</span>
            </td>
            <td style="text-align: center;">
              <img style="width: 150px;" src="../assets/go.svg" />
            </td>
            <td style="text-align:right">
              <span id="start-arrival-location" class="surprise">Surprise</span>
            </td>
          </tr>
          <tr>
            <td>
              <span id="start-departure-time">~{{ results[result].start_time_go_approx }}</span>
            </td>
            <td>
            </td>
            <td style="text-align:right">
              <span id="start-arrival-time">~{{ results[result].end_time_go_approx }}</span>
            </td>
          </tr>
          <tr style="height: 16px;">
          </tr>
          <tr>
            <td>
              <span id="return-departure-location" class="surprise">Surprise</span>
            </td>
            <td style="text-align: center;">
              <img style="width: 150px;" src="../assets/back.svg" />
            </td>
            <td style="text-align:right">
              <span id="return-arrival-location">{{ results[result].start_name }}</span>
            </td>
          </tr>
          <tr>
            <td>
              <span id="return-departure-time">~{{ results[result].start_time_return_approx }}</span>
            </td>
            <td>
            </td>
            <td style="text-align:right">
              <span id="return-arrival-time">~{{ results[result].end_time_return_approx}}</span>
            </td>
          </tr>
        </table>
        <span id="travel-date">{{ results[result].trip_date }}</span>
      </div>
      <div class="tickets">
        <div id="ticket-count">Number of tickets <img src="../assets/i.svg" /></div>
        <span id="total-tickets-count" class="large">{{ user.personCountFull + user.personCountHalf}}</span>
        <span id="total-tickets-full" class="annotation">{{ user.personCountFull }} x full price</span>
        <span id="total-tickers-half" class="annotation">{{ user.personCountHalf }} x half price</span>
      </div>
      <div class="price">
        <div id="trip-price-title">Total price <img src="../assets/i.svg" /></div>
        <span id="price" class="large">{{ results[result].price_saver }}</span>
        <span id="savings">{{ results[result].saved_perc + ' or ' + results[result].price_rebate }} saved</span>
      </div>
    </div>
    <div class="footer">
      <div id="roll" v-on:click="roll" style="text-align: center">
        <img id="roll-icon" src="../assets/roll.svg" /><br />
        <div id="try-again">Try again</div>
      </div>
      <button id="buy" v-on:click="buy">Book for {{ results[result].price_saver }}</button>
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
    },
    roll: function() {
      this.result++;
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
  width: 260px;
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
  padding: 0px 4px;
  border-radius: 3px;
  background-color: #ea0100; 
}

table {
  border: 0px;
  padding: 0px;
  margin: 0px;
  width: 343px;
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

#travel-date {
  font-family: 'Source Sans Pro', sans-serif;
  font-size: 16px;
  font-weight: 300;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: 0.33px;
  color: #ffffff;
  display: block;
  margin: auto;
  text-align: center;
  width: 100%;
  position: relative;
  right: 16px;
  margin-top: 16px;
}

#roll {
  display: inline-block;
  position: relative;
  top: 16px;
}

#try-again {
  display: inline-block;

  font-family: 'Source Sans Pro', sans-serif;
  font-size: 12px;
  font-weight: 300;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: 0.25px;
  text-align: center;
  color: #1e1e1e;
}
</style>