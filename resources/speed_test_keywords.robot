*** Settings ***
Library     SeleniumLibrary
Library    DateTime
Resource    resources/SetupsTeardowns.robot

*** Variables ***
${start_button}     css:div.start-button
${empty_download_result}    xpath://span[contains(@data-download-status-value, "NaN")]
${speed_result}     css:span.download-speed

*** Keywords ***
Accept Cookies
    ${timestamp}     get current date
    add cookie  OptanonAlertBoxClosed   ${timestamp}

Open SpeedTest Page     [Arguments]    ${BROWSER}    ${URL}
    Open Browser    ${URL}  ${BROWSER}

Start Speed Test
    Click Element   ${start_button}

Check Results   [Arguments]    ${expected_speed}
    Wait Until Page Does Not Contain Element    ${empty_download_result}    timeout=30
    ${speed}=    Get text    ${speed_result}
    Log     ${speed}
    Should be true  ${speed} > ${expected_speed}