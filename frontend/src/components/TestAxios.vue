<template>
  <div id="TestAxios">
    {{ test }}
    <div v-for="user in users" v-key="user.id">
        <h1>{{user.name}}</h1>
        <p>{{user.email}}</p>
    </div>
    <button v-on:click="fetchUsers">Click me!</button>
  </div>
</template>

<script>
export default {
  name: 'TestAxios',
  data () {
    return {
      test: 'test',
      users: []
    }
  },
  methods: {
    fetchUsers: function () {
      const baseURI = 'https://jsonplaceholder.typicode.com/users'
      this.$http.get(baseURI)
        .then((result) => {
        this.users = result.data
        console.log("ping")
      })
    }
  }
}
</script>