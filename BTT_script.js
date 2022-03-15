(async () => {

	// I always put my code into a self executing async function, because top level await is not allowed in JavaScript.
	// put the shell script into a string (single backticks are great for multiline strings)
	let shellScript = '/Users/matbook/.pyenv/versions/3.7.3/bin/python3.7 /Users/matbook/Desktop/PyLMS/clip_codes.py'

	let shellScriptWrapper = {
		script: shellScript, // mandatory
		launchPath: '/bin/bash', //optional - default is /bin/bash
		parameters: '-c', // optional - default is -c. If you use multiple parameters please separate them by ;; e.g. -c;;date
		environmentVariables: 'VAR1=/result/' //optional e.g. VAR1=/test/;VAR2=/test2/;
	};

	// this will execute the Apple Script and store the result in the result variable.
	let result = await runShellScript(shellScriptWrapper);

	// do whatever you want with the result

	let code_string = await callBTT('set_string_variable', { variable_name: 'code', to: result });


	// at the end you always need to call returnToBTT to exit the script / return the value to BTT.
	returnToBTT(result);

	// it is important that this function self-executes ()
})();