<template>
  <div id="home">
    <h1>{{ data }}</h1>
    <button v-on:click="fetchHello">Click me!</button>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      data: ""
    }
  },
  methods: {
    fetchHello: function () {
      this.$http.get("/")
        .then((result) => {
        this.data = result.data;
      })
    }
  }
}
</script>

<stlye scoped>

</style>