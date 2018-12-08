<template>
  <v-app>
    <v-content>
      <PaperDocument></PaperDocument>
    </v-content>
  </v-app>
</template>

<script>
import PaperDocument from './components/PaperDocument'

export default {
  name: 'App',
  components: {
    PaperDocument
  },
  data () {
    return {
      //
    }
  }
}
</script>
