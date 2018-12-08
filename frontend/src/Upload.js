import React, { Component } from 'react';

class Upload extends React.Component {
	constructor(props) {
		super(props);
		this.state = {uploaded: false};
		this.handleClick = this.handleClick.bind(this);
	}
	render() {
		if (this.uploaded)
			return <p>Uploaded!</p>;
		else
			return <button onClick={this.handleClick}>Upload</button>;
	}
	upload(file) {
		fetch('//localhost:5000/', {
			method: 'POST',
			//mode: 'no-cors',
			headers: {
				"Content-Type": "text",
				"Access-Control-Allow-Origin": "*"
			},
			body: file
		}).then(
			response => console.log(response)
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
	handleClick() {
		const input = document.getElementById('fileinput');
		this.upload(input.files[0]);
	};
};

export default Upload;
