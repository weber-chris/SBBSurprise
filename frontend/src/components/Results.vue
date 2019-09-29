<template>
  <div id="results">
    <div class="navigation">
        <img src="../assets/path.svg" id="back" v-on:click="$router.push('/')" />
        <span id="title">SBB Surprise</span>
        <img id="logo" src="../assets/path-2881.svg" />
      </div>
  </div>
</template>

<script>
export default {
  name: 'Results',
  data () {
    return {
      results: this.$parent.results
    }
  },
  methods: {
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
  bottom: -75px;
  width: 100%;
  padding: 16px;
}

#next {
  width: 343px;
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

</style>