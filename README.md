# chatgpt_api

<!DOCTYPE html>
<html>
<head>
	<title>ChatGPT API</title>
	<style>
		body {
			font-family: Arial, sans-serif;
			line-height: 1.5;
			margin: 0;
			padding: 0;
		}

		.container {
			max-width: 800px;
			margin: 0 auto;
			padding: 20px;
		}

		h1, h2, h3 {
			margin-top: 0;
		}

		h1 {
			font-size: 48px;
			font-weight: bold;
			text-align: center;
			margin-bottom: 20px;
		}

		h2 {
			font-size: 36px;
			margin-bottom: 10px;
		}

		h3 {
			font-size: 24px;
			margin-bottom: 10px;
		}

		p {
			margin: 0;
			padding: 0;
			font-size: 16px;
			line-height: 1.5;
			margin-bottom: 10px;
		}

		code {
			font-family: Consolas, monospace;
			font-size: 14px;
			background-color: #eee;
			padding: 5px;
			border-radius: 5px;
			overflow: auto;
			display: inline-block;
		}

		pre {
			font-family: Consolas, monospace;
			font-size: 14px;
			background-color: #eee;
			padding: 10px;
			border-radius: 5px;
			overflow: auto;
		}

		.highlight {
			color: #007bff;
			font-weight: bold;
		}

		.button {
			display: inline-block;
			background-color: #007bff;
			color: #fff;
			padding: 10px 20px;
			border-radius: 5px;
			text-decoration: none;
			font-size: 18px;
			margin-top: 20px;
		}

		.button:hover {
			background-color: #0056b3;
		}
	</style>
</head>
<body>
	<div class="container">
		<h1>ChatGPT API</h1>

		<p>This repository contains a standalone Python script called <code>chat.py</code> that uses OpenAI's GPT-3 language model to generate responses to user input. The script can be run locally on your machine and does not require deployment to a hosting provider.</p>

		<h2>Getting Started</h2>

		<p>To use this script, you will need an OpenAI API key. You can sign up for an API key <a href="https://beta.openai.com/signup/">here</a>. Once you have an API key, you can set it as an environment variable in your terminal or in a configuration file called <code>config.py</code>.</p>

		<p>To set the API key as an environment variable, run the following command in your terminal:</p>

		<pre><code>export OPENAI_API_KEY=<span class="highlight">&lt;your-api-key&gt;</span></code></pre>

		<p>To set the API key in a <code>config.py</code> file, create a new file in the same directory as the <code>chat.py</code> file with the following contents:</p>

		<pre><code>API_KEY = "<span class="highlight">&lt;your-api-key&gt;</span>"</code
