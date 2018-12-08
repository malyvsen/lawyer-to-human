<template>
  <v-app>
    <v-content>
      <paper-document></paper-document>
       <div v-show="$refs.upload && $refs.upload.dropActive" class="drop-active">
         <h3>Drop files to upload</h3>
       </div>

       <div class="example-btn">
         <file-upload
            class="btn btn-primary v-btn white--text info v-btn--floating v-btn--outline"
            post-action="//localhost:5000/"
            :multiple="true"
            :drop="true"
            :drop-directory="true"
            v-model="files"
            ref="upload"
            v-if="!$refs.upload || !$refs.upload.active">
           <v-icon right dark>list</v-icon>
         </file-upload>
         <v-progress-circular
           :size="50"
           color="primary"
           indeterminate
           v-else>
         </v-progress-circular>
         <v-btn color="blue-grey" type="button" class="btn btn-success white--text"
           :loading="loading3"
           :disabled="loading3"
            v-if="!$refs.upload || !$refs.upload.active" @click.prevent="$refs.upload.active = true">
           Start Upload
           <v-icon right dark>cloud_upload</v-icon>
         </v-btn>
         <v-btn color="error" type="button" class="btn btn-danger"  v-else @click.prevent="$refs.upload.active = false">
           <i class="fa fa-stop" aria-hidden="true"></i>
           Stop Upload
         </v-btn>
       </div>
    </v-content>
  </v-app>
</template>

<script>
import PaperDocument from './components/PaperDocument'
import FileUpload from 'vue-upload-component'

export default {
  name: 'App',
  components: {
    PaperDocument,
    FileUpload
  },
  data () {
    return {
      files: []
    }
  }
}
</script>

<style>
  body {
    background: #fafafa;
  }
</style>
