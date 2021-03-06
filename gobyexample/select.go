package main

import (
    "time"
    "fmt"
)

func main() {
    c1 := make(chan string)
    c2 := make(chan string)

    go func() {
        time.Sleep(time.Second)
        c1 <- "one"
    }()

    go func() {
        time.Sleep(time.Second * 2)
        c2 <- "two"
    }()

    for i := 0 ; i < 3; i++ {
        select {
        case msg1 := <-c1 :
            fmt.Println("Recievd:", msg1)
        case msg2 := <-c2 :
            fmt.Println("Recievd:", msg2)
        }
    }

}


