<template>
  <article class="paper-document elevation-3">
    <p>
      <span
        class="sentence"
        v-for="(sentence, index) in document.sentences"
        :key="index"
        v-bind:class="{'important': sentence.important, 'current-sentence': index === sentenceIndex}"
      >
        {{ sentence.text }}
        <!-- <SideTooltip></SideTooltip> -->
      </span>
    </p>
  </article>
</template>

<script>
import SideTooltip from "./SideTooltip.vue";
export default {
  props: ["content", "positions", "document", "sentenceIndex"],
  watch: {
    sentenceIndex: function(newIndex, oldIndex) {
      console.log('WATCH sentenceIndex:', newIndex, oldIndex);
      const sentenceEl = this.$el.querySelector(`.sentence:nth-child(${newIndex+1})`);
      const scroll = sentenceEl.offsetTop - sentenceEl.scrollTop;
      // const scroll = sentenceEl.getBoundingClientRect().top;
      console.log(scroll);
      window.scrollTo(0, scroll);
    }
  },
  components: {
    SideTooltip
  },
  computed: {
    // splitedContent: function() {
    //   const parts = [];
    //   let prevIndex = 0;
    //   for (const position of this.positions) {
    //     parts.push({
    //       text: this.content.slice(prevIndex, position[0]),
    //       isSelection: false
    //     });
    //     parts.push({
    //       text: this.content.slice(position[0], position[1]),
    //       isSelection: true
    //     })
    //     prevIndex = position[1];
    //   }
    //   parts.push({
    //     text: this.content.slice(prevIndex),
    //     isSelection: false
    //   });
    //   return parts;
    // },
    // splitedContent: function() {
    //   const sentences = this.document.sentences;
    // }
  }
};
</script>

<style>
.paper-document {
  position: relative;
  font-size: 1.5em;
  background: #fff;
  max-width: 210mm;
  width: 100%;
  min-height: 80%;
  margin: 4rem auto;
  padding: 3rem;
  margin-bottom: 50vh;

  color: #0007;
}

.paper-document > p {
  text-align: justify;
}

.important {
  position: relative;
}

.side-tooltip {
  transition: opacity 0.5s ease;
  opacity: 0;
}

span.important:hover > div .side-tooltip {
  opacity: 1;
  transition-duration: 0.3s;
}

span.important {
  background: #0001;
}

span.current-sentence {
  background: #ffa;
  color: #000;
}
</style>
