(async () => {

let input = 'product'

    let shellScript = '/Users/matbook/.pyenv/versions/3.7.3/bin/python3.7 /Users/matbook/Desktop/PyLMS/BTT Scripts/read_codes.py' + ' ' + input

let shellScriptWrapper = {
    script: shellScript, // mandatory
    launchPath: '/bin/bash', //optional - default is /bin/bash
    parameters: '-c', // optional - default is -c. If you use multiple parameters please separate them by ;; e.g. -c;;date
    environmentVariables: '' //optional e.g. VAR1=/test/;VAR2=/test2/;
};

// this will execute the Apple Script and store the result in the result variable.
let result = await runShellScript(shellScriptWrapper);

// do whatever you want with the result

let string = await callBTT('set_string_variable', {variable_name: input, to: result});

returnToBTT(result);
})();