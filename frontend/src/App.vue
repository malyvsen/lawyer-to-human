<template>
  <v-app>
    <v-content>
      <paper-document v-if="currentDocument.text !== null" :content="currentDocument.text" :positions="processingDataPositions"></paper-document>
      <v-btn color="info" fab large dark
        v-if="currentDocument.tts !== null"
        v-bind:id="currentDocument.tts"
	v-on:click="playTTS">
        <v-icon>hearing</v-icon>
      </v-btn>
       <div v-show="$refs.upload && $refs.upload.dropActive" class="drop-active">
         <h3>Drop files to upload</h3>
       </div>

       <div class="example-btn">
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
          >
         </v-progress-circular>
         <v-btn color="blue-grey" type="button" class="btn btn-success white--text"
           @click.prevent="$refs.upload.active = true">
           Start Upload
           <v-icon right dark>cloud_upload</v-icon>
         </v-btn>
       </div>
    </v-content>
  </v-app>
</template>

<script>
import PaperDocument from "./components/PaperDocument";
import FileUpload from "vue-upload-component";

export default {
  name: "App",
  components: {
    PaperDocument,
    FileUpload
  },
  data() {
    return {
      file: [],
      uploadStatus: null,
      currentDocument: {
        text: null,
        tts: null,
        metadata: [],
        selections: []
      }
    }
  },
  methods: {
    fileUpload: function (newFile, oldFile) {
      if (newFile && oldFile && !newFile.active && oldFile.active) {
        if (newFile.xhr) {
          if (newFile.xhr.status === 200) {
            this.uploadStatus = true
            console.log(newFile.response.metadata)
            this.currentDocument.text = newFile.response.text || '';
            this.currentDocument.tts = newFile.response.tts || '';
            this.currentDocument.metadata = newFile.response.metadata || [];
            this.currentDocument.selections = newFile.response.selections || []
          } else {
            this.uploadStatus = false;
          }
        }
      }
    },
    playTTS: function (event) {
      const src = "//localhost:10080" + event.originalTarget.id;
      const audio = new Audio(src);
      audio.play();
    }
  },
  computed: {
    processingDataPositions: function() {
      const selections = Array.from(this.currentDocument.selections);
      const sortedSelections = selections.sort((a, b) => (a[0] > b[0]));
      return sortedSelections.map(selection => (selection.position));
    }
  }
};
</script>

<style>
body {
  background: #fafafa;
}
</style>
