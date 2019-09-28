<template>
  <div id="preferences">
    <h1>Welcome to SBB Surprise</h1>
    <h1>{{ date }}</h1>
    <input></input>
    <button v-on:click="fetchHello">Click me!</button>
  </div>
</template>

<script>
export default {
  name: 'Preferences',
  data () {
    return {
      date: new Date(),
      budget: "no",
      location: "Zürich HB"
    }
  }
}
</script>

<stlye scoped>

</style>