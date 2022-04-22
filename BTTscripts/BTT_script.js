(async () => {

    let input = 'product'

    let shellScript = '/Users/matbook/.pyenv/versions/3.7.3/bin/python3.7 /Users/matbook/PyLMS/BTTscripts/read_codes.py' + ' ' + input

    let shellScriptWrapper = {
        script: shellScript, // mandatory
        launchPath: '/bin/bash', //optional - default is /bin/bash
        parameters: '-c', // optional - default is -c. If you use multiple parameters please separate them by ;; e.g. -c;;date
        environmentVariables: '' //optional e.g. VAR1=/test/;VAR2=/test2/;
    };

    // this will execute the Apple Script and store the result in the result variable.
    let result = await runShellScript(shellScriptWrapper);

    // do whatever you want with the result

    if (input = 'product'){
        let notchbar_uuid = 'BB3F6378-A170-4F35-AE1F-3F2CAF39190F'// product NotchBar
        let touchbar_uuid = '5C5FA28F-EACB-4CC5-8B26-DDB6C2974B63'// product Touchbar
        let previous_result = await callBTT('get_string_variable', { variable_name: input })
    }
    else if (input = 'batch'){
        let notchbar_uuid = 'AAB25018-6B64-44D9-B043-9F302E81D7A3'// batch NotchBar
        let touchbar_uuid = '96594A80-F726-4D67-B6C0-0B14CEE100A7'// batch Touchbar
        let previous_result = await callBTT('get_string_variable', { variable_name: input })
    }
    else if (input = 'lot'){
        let notchbar_uuid = 'C489EAF0-94B1-4671-9312-45FA8A77BA3F'// lot NotchBar
        let touchbar_uuid = 'D9AE7570-94B2-4410-9C34-70046C429865'// lot Touchbar
        let previous_result = await callBTT('get_string_variable', { variable_name: input })
    }
    else if (input = 'coated'){
        let notchbar_uuid = '7B0BE149-703B-41E2-9272-FD9B497E2045'// coated NotchBar
        let touchbar_uuid = 'FA5D8ECE-9C20-4888-8B6B-81978A8E057C'// coated Touchbar
        let previous_result = await callBTT('get_string_variable', { variable_name: input })
    }
    else if (input = 'batcho'){
        let notchbar_uuid = '9092EC10-D06F-4F5D-AACD-9883677799AD'// batcho NotchBar
        let previous_result = await callBTT('get_string_variable', { variable_name: input })
    }

    if (result != previous_result) {
        let string = await callBTT('set_string_variable', { variable_name: input, to: result });
        callBTT('refresh_widget', { uuid: notchbar_uuid });
        callBTT('refresh_widget', { uuid: touchbar_uuid });
    }
    returnToBTT(result);
})();