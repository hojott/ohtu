*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  julia
    Set Password  julia123
    Set Password Confirmation  julia123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  j
    Set Password  julia123
    Set Password Confirmation  julia123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  julia
    Set Password  j1
    Set Password Confirmation  j1
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Valid Username And Invalid Password
    Set Username  julia
    Set Password  juliajulia
    Set Password Confirmation  juliajulia
    Submit Credentials
    Register Should Fail With Message  Password is invalid

Register With Nonmatching Password And Password Confirmation
    Set Username  julia
    Set Password  julia123
    Set Password Confirmation  julia321
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  User with username kalle already exists

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
