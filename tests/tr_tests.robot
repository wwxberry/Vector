*** Settings ***
Documentation   First test
Library    resources/testrail_lib.py


*** Test Cases ***
Get TCs list
    ${list} =   get_tcs_list
    Log     ${list}