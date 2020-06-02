<template>
  <div>
    <b-container>
      <b-table striped hover :items="users"></b-table>
    </b-container>
  </div>
</template>
<script>
import axios from 'axios'

const endpoint = 'http://localhost:8000/'

export default {
  data() {
    return {
      users: []
    }
  },
  created() {
    axios.get(endpoint + 'grade/')
      .then(response => {
        this.users = response.data;
      })
  }
}
</script>
