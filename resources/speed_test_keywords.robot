*** Settings ***
Library     SeleniumLibrary
Library    DateTime
Resource    resources/setups_teardowns.robot

*** Variables ***
${start_button}     css:div.start-button
${empty_download_result}    xpath://span[contains(@data-download-status-value, "NaN")]
${speed_result}     css:span.download-speed
${accept_cookie_button}     id:onetrust-accept-btn-handler

*** Keywords ***
Accept Cookies
    Wait Until Element Is Visible   ${accept_cookie_button}
    Click button   ${accept_cookie_button}
    Wait Until Element Is Not Visible   ${accept_cookie_button}

Open SpeedTest Page     [Arguments]    ${BROWSER}    ${URL}
    Open Browser    ${URL}  ${BROWSER}

Start Speed Test
    Click Element   ${start_button}

Check Results   [Arguments]    ${expected_speed}
    Wait Until Page Does Not Contain Element    ${empty_download_result}    timeout=30
    ${speed}=    Get text    ${speed_result}
    Log     ${speed}
    Should be true  ${speed} > ${expected_speed}
