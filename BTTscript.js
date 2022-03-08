
// I always put my code into a self executing async function, because top level await is not allowed in JavaScript.
(async () => {

// put the shell script into a string (single backticks are great for multiline strings)
let shellScript = '/Users/matbook/.pyenv/versions/3.7.3/bin/python3.7 /Volumes/SHARED/PyLMS/read_product.py'

let shellScriptWrapper = {
    script: shellScript, // mandatory
    launchPath: '/bin/bash', //optional - default is /bin/bash
    parameters: '-c', // optional - default is -c. If you use multiple parameters please separate them by ;; e.g. -c;;date
    environmentVariables: 'Var1=/productstring' //optional e.g. VAR1=/test/;VAR2=/test2/;
};

// this will execute the Apple Script and store the result in the result variable.
let productstring = await runShellScript(shellScriptWrapper);
let product_result = await callBTT('set_string_variable', {variable_name: 'product', to: productCode});
let batch_result = await callBTT('set_string_variable', {variable_name: 'batch', to: batchCode});
let lot_result = await callBTT('set_string_variable', {variable_name: 'lot', to: lotCode});
let coated_result = await callBTT('set_string_variable', {variable_name: 'coated', to: coatedCode});
// do whatever you want with the result

// at the end you always need to call returnToBTT to exit the script / return the value to BTT.
returnToBTT(productstring);

// it is important that this function self-executes ()
})();