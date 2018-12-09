<template>
	<div>
		<v-btn flat icon
			v-show="!locked"
			v-on:click="getTTS"
			>
	<v-icon>volume_up</v-icon>
		</v-btn>
		<v-progress-circular
			:size="50"
			color="primary"
			indeterminate
			v-show="locked"
			>
		</v-progress-circular>
	</div>
</template>

<script>
export default {
	data: () => ({
		locked: false,
		src: null}),
	props: ['txt'],
	methods: {
		fetchTTS: function(txt, assign) {
			fetch("//localhost:10080/newaudio", {
				method: "POST",
				mode: "cors",
				headers: {
					"Content-Type": "plaintext",
					"Access-Control-Allow-Origin": "*"
				},
				body: txt
			}).then(
				response => assign(response)
			)/*.then(
				success => {
					//console.log(success);
				}
			).catch(
				error => console.log(error)
			);*/
		},
		playTTS: function(filename) {
			const src = "//localhost:10080/audio/" + filename;
			const audio = new Audio(src);
			audio.play();
		},
		getTTS: function() {
			this.locked = true;
			let txt = "";
			//if (myid == "all")
			//	txt = this.currentDocument.text;
			txt = this.txt;
			if (this.src == null || !this.src)
				this.fetchTTS(txt, function(d) {
					this.src = d.body;
					this.playTTS(this.src);
					this.locked = false;
				});
			else {
				this.playTTS(this.src);
				this.locked = false;
			}
		}
	}
}
</script>
