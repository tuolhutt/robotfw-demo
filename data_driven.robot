*** Settings ***
Documentation     Test cases using the data-driven testing.
...
...               Notice that one of these tests fails on purpose to show how
...               failures look like.
Test Template     Calculate
Library           AreaCalculatorLibrary.py

*** Test Cases ***    Expression    Expected
Rectangle             r 1.0 2.0     2.0
                      r 2.5 3.0     7.5

Ellipse               e 1.0 1.0     3.14
                      e 2.0 2.0     12.56

Triangle              t 2.0 2.0     2.0
                      t 2.0 3.5     3.5

Failing               t 1.1 1.1     5.0

Calculation error     [Template]    Calculation should fail
                      asd           Invalid expression.
                      ${EMPTY}      Invalid expression.

*** Keywords ***
Calculate
    [Arguments]    ${expression}    ${expected}
    Push arguments    C${expression}
    Result should be    ${expected}

Calculation should fail
    [Arguments]    ${expression}    ${expected}
    ${error} =    Should cause error    C${expression}
    Should be equal    ${expected}    ${error}    # Using `BuiltIn` keyword
