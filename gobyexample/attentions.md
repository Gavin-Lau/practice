### 详细了解golang的闭包

### golang接口类型interface
+ 一种是代表任意类型的数据结构，一般作为函数参数，类型c++的templete，即空类型的interface
+ 一种是指具有统一方法的一类struct的统称，即非空类型的interface。

### golang interface定义方法为指针时
``` golang
func (u *user) notify() {   
    fmt.Printf("Sending user email to %s“,u.name）
}
```
那么对应的接口调用也使用指针，不然会报
>method has pointer receiverd

错误
``` golang
func main() {
    // Create a value of type User and send a notification.
    u := user{"Bill", "bill@email.com"}
    sendNotification(&u)
    // PASSED THE ADDRESS AND NO MORE ERROR.
}
```
### 通道方向
当使用通道作为函数参数的时候，你可以指定这个通道是不是只是用来作为发送或接收（单向的），这个特性可以提升程序的安全性
>只用来发送的chan声明： chan <- string   
>只用来接收的chan声明： <- chan string

### 使用golang自带通道实现超时处理
```golang
    //功能函数
    go func() {
        time.Sleep(time.Second * 2)
        c1 <- "result 1"
    }()
    //使用select来监控他的结果
    select {
    case res := <-c1: //在超时时间内返回，走该分支
        fmt.Println(res)
    case <-time.After(time.Second * 3) :
        fmt.Println("Ooh, time out...")
    }
```

### 非阻塞通道
我们可以使用带default子句的多路select来实现非阻塞的发送和接收
``` golang
    messages := make(chan string)
    signals := make(chan bool)
    ...
    msg := "hi"
    //执行到select的时候,如果messages channel,内容是满的,则直接走default分支
    select {
    case messages <- msg:
        fmt.Println("sent message", msg)
    default:
        fmt.Println("no message sent")
    }
```
### golang中函数式编程思想，替代c++中面向过程和面向对象思想

### golang 中的channel的一些tips
1. 当我们复制一个channel或用于函数参数传递时，我们只是拷贝一个channel的引用
2. channel的发送和接收都是**<-** 符号，在发送语句中，**<-**分割channel和要发送的值，在接收语句中**<-**运算符写在channel对象之前。
3. channel也是可以close（channel1），关闭之后依然可以从中接受关闭之前已经在channel中的数据，如果channel中没有值了，那么会返回一个0值和非nil的错误类型。
4. range可以用于对channel的迭代，当channel关闭且没有值时，跳出循环。
5. 单向channel：chan<-int, 只发送不接收，<- chan int,只接收不发送

