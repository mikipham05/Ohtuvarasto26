*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application

*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Get Title  ==  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Go To Register Page
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Get Text  body  *=  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Go To Register Page
    Set Username  kalle
    Set Password  lyhyt
    Set Password Confirmation  lyhyt
    Click  button >> text=Register
    Get Text  body  *=  Password must be at least 8 characters long

Register With Username That Is Already In Use
    Create User  kalle  kalle123
    Go To Register Page
    Set Username  kalle
    Set Password  toinen123
    Set Password Confirmation  toinen123
    Click  button >> text=Register
    Get Text  body  *=  User with username kalle already exists