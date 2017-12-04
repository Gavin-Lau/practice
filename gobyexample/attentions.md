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
只用来接收的chan声明： <- chan string

