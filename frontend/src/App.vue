<template>
  <v-app>
    <SentenceNav
      :sentenceIndex="sentenceIndex"
      @decreaseFontSize="changeFontSize(-25)" @increaseFontSize="changeFontSize(25)"
      @previousSentence="switchSentence(-1)" @nextSentence="switchSentence(1)">
    </SentenceNav>

    <v-content :style="fontSizeStyle">
      <paper-document
        v-if="currentDocument.text !== null"
        :content="currentDocument.text"
        :positions="processingDataPositions"
      ></paper-document>
      <v-btn
        color="info"
        fab
        large
        dark
        v-if="currentDocument.tts !== null"
        v-bind:id="currentDocument.tts"
        v-on:click="playTTS"
      >
        <v-icon>hearing</v-icon>
      </v-btn>

      <SelectionDetails></SelectionDetails>

      <v-layout
        align-center
        align-content-center
        justify-center
        column
        >
        <v-flex>
          <file-upload
            class="file-upload"
            post-action="/api/"
            :drop="true"
            :drop-directory="true"
            v-model="file"
            ref="upload"
            v-show="!$refs.upload || !$refs.upload.active"
            @input-file="fileUpload"
          >
            <v-layout align-center justify-center style="height: 100%;" column>
              <v-icon size="5em">
                present_to_all
              </v-icon>
              <span v-if="file.length == 0">
                Przeciągnij tutaj plik albo naciśnij aby go wybrać.
              </span>
              <span v-else>
                Plik wybrany! Naciśnij przycisk poniżej aby przesłać.
              </span>
            </v-layout>
          </file-upload>
          <v-progress-circular
            indeterminate
            size="50"
            color="blue"
            v-show="$refs.upload && $refs.upload.active"
          ></v-progress-circular>
        </v-flex>
        <v-flex>
          <v-btn
            color="blue-grey"
            type="button"
            class="btn btn-success white--text"
            @click.prevent="$refs.upload.active = true"
          >Start Upload
            <v-icon right dark>cloud_upload</v-icon>
          </v-btn>
        </v-flex>
      </v-layout>
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
        selections: []
      },
      sentenceIndex: 0
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
          } else {
            this.uploadStatus = false;
          }
        }
      }
    },
    switchSentence: function(step) {
      const newIndex = this.sentenceIndex + step;
      if (newIndex >= 0 && newIndex < 30) { // TODO: prawdziwa długość dokumentu
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
  computed: {
    processingDataPositions: function() {
      const selections = Array.from(this.currentDocument.selections);
      const sortedSelections = selections.sort((a, b) => a[0] > b[0]);
      return sortedSelections.map(selection => selection.position);
    },
    fontSizeStyle: function() {
      return { fontSize: this.fontSize + "%" };
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

.file-upload {
  margin-top: 30px;
  width: 200px;
  height: 200px;
}
</style>
