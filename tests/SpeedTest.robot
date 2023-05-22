*** Settings ***
Resource    resources/SpeedTestKeywords.robot
Test Teardown   Browser Teardown

*** Variables ***
${BROWSER}      firefox
${URL}      https://www.speedtest.net/

*** Test Cases ***
Perform Speed Test
    Open SpeedTest Page     ${BROWSER}  ${URL}
    Accept Cookies
    Start Speed Test
    Check Results   80

