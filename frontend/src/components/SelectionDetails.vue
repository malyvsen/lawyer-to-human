<template>
  <div class="selection-details">
    <v-layout column>
      <strong>
        <v-icon>book</v-icon>Definitions
      </strong>
      <dl>
        <div v-for="(definition, index) in definitionList" :key="index">
          <dt>{{ definition.word }}</dt>
          <dd>{{ definition.definition }}</dd>
        </div>
      </dl>
    </v-layout>
  </div>
</template>

<script>
export default {
  props: ['definitionList'],
  components: {},
  computed: {}
};
</script>

<style>
.selection-details {
  background: #fff;
  position: fixed;
  bottom: 0;
  width: 100vw;
  padding: 2rem 5rem;
  box-shadow: 0 -3px 15px rgba(0, 0, 0, 0.2);
  z-index: 1;
}

.selection-details strong {
  margin-bottom: 1.5rem;
}

.selection-details strong .v-icon {
  color: rgb(13, 121, 209) !important;
}

.selection-details dt {
  font-size: 1.5em;
  font-weight: normal;
  font-size: 1.5rem;
  display: inline;
  font-weight: bold;
}

.selection-details dt::after {
  content: "–";
  margin: 0 0.5rem;
}

.selection-details dd {
  display: inline;
  font-size: 1.3rem;
  vertical-align: 1px;
}
</style>
