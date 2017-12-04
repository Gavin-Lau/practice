package main

import "fmt"

func main() {
    queue := make(chan string, 2)
    queue <- "one"
    queue <- "two"
    //如果没有关闭,则下面的for循环回一直阻塞
    close(queue)

    for elem := range queue {
        fmt.Println(elem)
    }
}

