*** Settings ***
Documentation   First test
#Resource    ./utils/TestRailConnector.py
Library    resources/testrail_lib.py

*** Variables ***
${Name}     Wojtek

*** Test Cases ***
Greetings Tests
    [Documentation]  Mój pierwszy test
    Log     Witaj ${Name}

Get TCs list
    ${list} =   get_tcs_list
    Log     ${list}