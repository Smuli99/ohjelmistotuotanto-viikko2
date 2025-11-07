*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  hytosama  barfoo123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  hytosama  barfoo123
    Output Should Contain  New user registered
    Input New Command
    Input Credentials  hytosama  foobar123
    Output Should Contain  User with username hytosama already exists

Register With Too Short Username And Valid Password
    Input Credentials  ht  foobar123
    Output Should Contain  Username ht must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  Hytosama  foobar123
    Output Should Contain  Username Hytosama must only contain lowercase letters a to z

Register With Valid Username And Too Short Password
    Input Credentials  hytosama  foobar1
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  hytosama  foobarfoo
    Output Should Contain  Password must contain number or special character
