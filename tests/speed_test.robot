*** Settings ***
Resource    resources/speed_test_keywords.robot
Test Teardown   Browser Teardown

*** Variables ***
${BROWSER}      firefox
${URL}      https://www.speedtest.net/

*** Test Cases ***
Perform Speed Test
    [Tags]  XXX
    Open SpeedTest Page     ${BROWSER}  ${URL}
    Accept Cookies
    Start Speed Test
    Check Results   80

