<template>
  <v-app>
    <SentenceNav
      :sentenceIndex="sentenceIndex"
      :sentenceMaxIndex="sentenceMaxIndex"
      @decreaseFontSize="changeFontSize(-25)" @increaseFontSize="changeFontSize(25)"
      @previousSentence="switchSentence(-1)" @nextSentence="switchSentence(1)"
      v-bind:class="{hidden: !uploadStatus}">
    </SentenceNav>

    <v-content :style="fontSizeStyle" @keyup.left="switchSentence(-1)" @keyup.right="switchSentence(+1)">
      <paper-document
        v-if="currentDocument.text !== null"
        :content="currentDocument.text"
        :positions="processingDataPositions"

        :sentenceIndex="sentenceIndex"
        :document="currentDocument"
      ></paper-document>
      <!-- <v-btn
        color="info"
        fab
        large
        dark
        v-if="currentDocument.tts !== null"
        v-bind:id="currentDocument.tts"
        v-on:click="playTTS"
      >
        <v-icon>hearing</v-icon>
      </v-btn> -->
      <div v-show="$refs.upload && $refs.upload.dropActive" class="drop-active">
        <h3>Drop files to upload</h3>
      </div>

      <SelectionDetails :definitionList="currentDefinitions" v-bind:class="{hidden: !uploadStatus || currentDefinitions.length === 0}"></SelectionDetails>

      <div class="upload-btn text-xs-center" v-if="!uploadStatus">
        <file-upload
          class="btn btn-primary v-btn white--text info v-btn--floating v-btn--outline"
          post-action="//localhost:10080/"
          :drop="true"
          :drop-directory="true"
          v-model="file"
          ref="upload"
          v-show="!$refs.upload || !$refs.upload.active"
          @input-file="fileUpload"
        >
          <v-icon right dark>list</v-icon>
        </file-upload>
        <v-progress-circular
          :size="50"
          color="primary"
          indeterminate
          v-show="$refs.upload && $refs.upload.active"
        ></v-progress-circular>
        <v-btn
          color="blue-grey"
          type="button"
          class="btn btn-success white--text"
          @click.prevent="$refs.upload.active = true"
        >Start Upload
          <v-icon right dark>cloud_upload</v-icon>
        </v-btn>
      </div>
    </v-content>
  </v-app>
</template>

<script>
import PaperDocument from "./components/PaperDocument";
import FileUpload from "vue-upload-component";
import SelectionDetails from "./components/SelectionDetails";
import SentenceNav from "./components/SentenceNav";

export default {
  name: "App",
  components: {
    PaperDocument,
    FileUpload,
    SelectionDetails,
    SentenceNav
  },
  data() {
    return {
      file: [],
      fontSize: 100,
      uploadStatus: null,
      currentDocument: {
        text: null,
        tts: null,
        metadata: [],
        selections: [],
        sentences: [],
        definitions: []
      },
      sentenceIndex: 0,
    };
  },
  methods: {
    fileUpload: function(newFile, oldFile) {
      if (newFile && oldFile && !newFile.active && oldFile.active) {
        if (newFile.xhr) {
          if (newFile.xhr.status === 200) {
            this.uploadStatus = true;
            this.currentDocument.text = newFile.response.text || "";
            this.currentDocument.tts = newFile.response.tts || "";
            this.currentDocument.metadata = newFile.response.metadata || [];
            this.currentDocument.selections = newFile.response.selections || [];
            this.currentDocument.sentences = newFile.response.sentences || [];
            
            this.currentDocument.sentences.map(sentence => {
              console.log('sentence', sentence);
              const snetenceText = sentence.text.replace('\n', '<br>');
              console.log(snetenceText);
              sentence.text = snetenceText;
              return sentence;
            });
            console.log("CURR DOC", this.currentDocument);
          } else {
            this.uploadStatus = false;
          }
        }
      }
    },
    switchSentence: function(step) {
      const newIndex = this.sentenceIndex + step;
      if (newIndex >= 0 && newIndex < this.sentenceMaxIndex) {
        this.sentenceIndex = newIndex;
      }
    },
    changeFontSize: function(delta) {
      const newFontSize = this.fontSize + delta;
      if (newFontSize >= 25 && newFontSize <= 300) {
        this.fontSize = newFontSize;
      }
    },
    playTTS: function(event) {
      const src = "//localhost:10080/audio/" + event.originalTarget.id;
      const audio = new Audio(src);
      audio.play();
    }
  },
  mounted () {
    window.addEventListener('keydown', (e) => {
      if (this.uploadStatus === false) {
        return false;
      }
      
      if (e.code === 'ArrowLeft') {
        this.switchSentence(-1);
      } else if (e.code === 'ArrowRight') {
        this.switchSentence(1);
      }
    });
  },
  computed: {
    processingDataPositions: function() {
      const selections = Array.from(this.currentDocument.selections);
      const sortedSelections = selections.sort((a, b) => a[0] > b[0]);
      return sortedSelections.map(selection => selection.position);
    },
    fontSizeStyle: function() {
      return { fontSize: this.fontSize + "%" };
    },
    sentenceMaxIndex: function() {
      return this.currentDocument.sentences.length;
    },
    currentDefinitions: function() {
      const sentence = this.currentDocument.sentences[this.sentenceIndex];
      if (sentence === undefined) {
        return [];
      }

      return sentence.definitions;
    }
  }
};
</script>

<style>
body {
  background: #fafafa;
  padding-top: 6rem;
}

.theme--light.v-divider {
  height: 1em;
}

.sentence-nav.hidden {
  transform: translateY(-100%);
}

.sentence-nav {
  transform: translateY(0);
  transition: all 0.3s ease;
}

.selection-details.hidden {
  transform: translateY(100%);
}

.selection-details {
  transform: translateY(0);
  transition: all 0.3s ease;
}
</style>