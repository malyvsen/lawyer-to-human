<template>
  <v-app>
    <v-content>
      <paper-document :content="documentText" :positions="processingDataPositions"></paper-document>
      <div v-show="$refs.upload && $refs.upload.dropActive" class="drop-active">
        <h3>Drop files to upload</h3>
      </div>

      <div class="example-btn">
        <file-upload
          class="btn btn-primary"
          post-action="//localhost:5000/"
          :multiple="true"
          :drop="true"
          :drop-directory="true"
          v-model="files"
          ref="upload"
        >
          <i class="fa fa-plus"></i>
          Select files
        </file-upload>
        <button
          type="button"
          class="btn btn-success"
          v-if="!$refs.upload || !$refs.upload.active"
          @click.prevent="$refs.upload.active = true"
        >
          <i class="fa fa-arrow-up" aria-hidden="true"></i>
          Start Upload
        </button>
        <button
          type="button"
          class="btn btn-danger"
          v-else
          @click.prevent="$refs.upload.active = false"
        >
          <i class="fa fa-stop" aria-hidden="true"></i>
          Stop Upload
        </button>
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
      files: [],
      documentText:
        "Sit voluptatem aliquid error corporis laborum sapiente sint. Labore ipsam doloribus ut aut alias placeat. Atque autem et odio totam labore neque ut. Error soluta iste tenetur quia voluptas debitis dolores.",
      sampleTextProcessingData: {
        text: "The document contents.",
        selections: [
          { type: "underline", position: [4, 14] },
          {
            type: "definition",
            position: [38, 45],
            description: "Definition of term."
          },
          { type: "entity-info", position: [50, 57], description: {} }
        ],
        metadata: [
          { type: "document-type", "document-type-name": "Umowa o prace" },
          { type: "summary", text: "Summary text." }
        ]
      }
    };
  },
  computed: {
    processingDataPositions: function() {
      const sortedSelections = this.sampleTextProcessingData.selections.sort((a, b) => (a[0] > b[0]));
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
