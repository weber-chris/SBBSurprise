<template>
  <div id="Home">
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
      const baseURI = 'http://localhost:5000'
      this.$http.get(baseURI)
        .then((result) => {
        this.data = result.data;
      })
    }
  }
}
</script>

<stlye scoped>

</style>