<template>
  <div>
    <b-container>
      <b-table striped hover :items="grades"></b-table>
    </b-container>
  </div>
</template>
<script>
import axios from 'axios'

const endpoint = 'http://localhost:8000/'

export default {
  data() {
    return {
      grades: []
    }
  },
  created() {
    axios.get(endpoint + 'grade/')
      .then(response => {
        this.grades = response.data;
      })
  }
}
</script>
