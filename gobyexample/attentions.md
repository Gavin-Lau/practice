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
