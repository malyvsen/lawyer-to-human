<template>
  <nav class="sentence-nav">
    <v-layout justify-space-between row>
      <v-flex sm1 class="text-xs-center">
        <v-btn flat icon>
          <v-icon>arrow_back</v-icon>
        </v-btn>
      </v-flex>

      <v-flex class="text-xs-center">
        <v-item-group>
          <v-btn flat icon>
            <v-icon>volume_up</v-icon>
          </v-btn>

          <v-divider vertical></v-divider>

          <v-btn flat icon @click="$emit('decreaseFontSize')">
            <v-icon>remove</v-icon>
          </v-btn>
          <span>Aa</span>
          <v-btn flat icon @click="$emit('increaseFontSize')">
            <v-icon>add</v-icon>
          </v-btn>
        </v-item-group>
      </v-flex>

      <v-flex sm1 class="text-xs-center">
        <v-btn flat icon>
          <v-icon>arrow_forward</v-icon>
        </v-btn>
      </v-flex>
    </v-layout>
  </nav>
</template>

<script>
export default {
  // data: () => ({
  //   quote: "Lorem ipsum"
  // }),
  //   props: ['quote'],
  components: {},
  computed: {},
  methods: {
    changeFont(delta) {
      this.$emit('myEvent')
    }
  }
};
</script>

<style>
.sentence-nav {
  background: #fff;
  position: fixed;
  top: 0;
  width: 100vw;
  padding: 1rem;
  box-shadow: 0 3px 15px rgba(0, 0, 0, 0.2);
  z-index: 1;
}

.sentence-nav .quote {
  font-size: 2rem;
  margin-bottom: 1.5rem;
}

.sentence-nav dt {
  font-size: 1.5em;
  font-weight: normal;
  margin-top: 1.5rem;
}

.sentence-nav .toolbox {
  position: absolute;
  top: 1rem;
  right: 10rem;
}
</style>
