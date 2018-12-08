import React, { Component } from 'react';

class Upload extends React.Component {
	construct() {
		this.state = {uploaded: true};
	}
	render() {
		if (this.uploaded)
			return <p>Uploaded!</p>;
		else
			return <button>Upload</button>;
	}
	upload(file) {
		fetch('localhost:5000', {
			method: 'POST',
			headers: {
				"Content-Type": ""
			},
			body: file
		}).then(
			response => response.json()
		).then(
			success => {
				this.setState((state, props) => {
					return {uploaded: true};
				});
				console.log(success);
			}
		).catch(
			error => console.log(error)
		);
	};
	onClick() {
		const input = document.getElementById('fileinput');
		this.upload(input.files[0]);
	};
};

export default Upload;
