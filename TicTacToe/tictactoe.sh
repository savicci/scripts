#!/usr/bin/bash

board=( 1 2 3 4 5 6 7 8 9 )

turn=0

first_player='X'
second_player='O'

is_running=true


print_board () {
    clear
    echo " ${board[0]} | ${board[1]} | ${board[2]} "
    echo "-----------"
    echo " ${board[3]} | ${board[4]} | ${board[5]} "
    echo "-----------"
    echo " ${board[6]} | ${board[7]} | ${board[8]} "
    echo "-----------"
}


take_input () {
    
    if [[ $(($turn % 2)) == 0 ]]
    then
        echo "First player pick position(X): "
        picking=$first_player
    else
        echo "Second player pick position(O): "
        picking=$second_player
    fi

    read position

    space=${board[($position -1)]}

    if [[ ! $space =~ ^[0-9]+$  ]] || [[ ! $position =~ ^-?[0-9]+$ ]]
    then
        echo "Not valid position. Please input values between 1 and 9"
        take_input
    else
        board[($position -1)]=$picking
        ((turn=turn + 1))
    fi

    space=${board[($position -1)]}
}

check_win () {
    # vertical
    check_match 0 1 2
    if [[ $is_running == false ]]; then return; fi

    check_match 3 4 5
    if [[ $is_running == false ]]; then return; fi

    check_match 6 7 8
    if [[ $is_running == false ]]; then return; fi

    # horizontal
    check_match 0 3 6
    if [[ $is_running == false ]]; then return; fi

    check_match 1 4 7
    if [[ $is_running == false ]]; then return; fi

    check_match 2 5 8
    if [[ $is_running == false ]]; then return; fi

    # crossing
    check_match 0 4 8
    if [[ $is_running == false ]]; then return; fi

    check_match 2 4 6
    if [[ $is_running == false ]]; then return; fi
}


check_match () {
    if [[ ${board[$1]} == ${board[$2]} ]] && [[ ${board[$2]} == ${board[$3]} ]]
    then
        is_running=false

        if [[ ${board[$1]} == 'X' ]]
        then
            echo "First player wins"
        else
            echo "Second player wins"
        fi
    fi
}

check_draw () {
    if [[ $turn == 9 ]]
    then
        echo "Its a draw"
        is_running=false
    fi
}


print_board
while $is_running
do
    take_input
    print_board
    check_win
    check_draw
done

