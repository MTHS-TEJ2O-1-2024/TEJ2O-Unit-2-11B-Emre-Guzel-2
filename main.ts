/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Emre Guzel
 * Created on: Oct 22 2024
 * This program generates ramdom number from 0-99
*/

// seting the screen 
basic.clearScreen()
basic.showIcon(IconNames.Happy)

// seting my varibles 
let num1 = randint (0, 99)
let num2 = randint (0,99)

// Setting the button A and making the that to genreate a number between 0 and 99
input.onButtonPressed(Button.A,function(){
    basic.clearScreen()
    basic.showString("#1:"),+ basic.showNumber(num1)
    basic.showIcon(IconNames.Happy)
})
    // Setting the button A and making the that to genreate a number between 0 and 99
input.onButtonPressed(Button.B, function(){
    basic.clearScreen()
    basic.showString("#2:"), + basic.showNumber(num2)
    basic.showIcon(IconNames.Happy)
})
// Ading a shake functoin 
input.onGesture(Gesture.Shake,function(){
    if(num1 < num2){
        num1
    }
})


