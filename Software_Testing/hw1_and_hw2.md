# Homework 1. Describe an error recently encountered.

最近实验室的一个项目中需要使用 Arduino 控制多个电机协同运动，主要是对 [AccelStepper](http://www.airspayce.com/mikem/arduino/AccelStepper/) 库进行包装以及二次开发。目前已经将其开源 [AccelStepperDecorate](https://github.com/MiaoDX/AccelStepperDecorate)（虽然除了我自己以及实验室同学也几乎不会有人使用-.-），其中遇到了一些有趣的问题，正好这次作业需要写一下最近自己遇到的程序错误，现小结一下，因为也没有几个错误，也就不限制数目到 “an error” 了。

因为是硬件（嵌入式）编程并且是与电机相关，所以可能与我们平常遇见的 BUG 有些不同 -- 错误不是通过类似于 `assert**` 的测试找到的，而是发现硬件设备运转不合预期进而再次查看代码得到的。

## Enable Pin

Enable Pin，使能管脚，直观地讲（之前学操作系统时），一个管脚是高电平使能，低电平不使能，但是在实际使用时发现与直觉相反。所以，在定义使能管教之前需要将其指出，具体到代码：

``` cpp
stepper.setPinsInverted(false, false, true); // possibly inverted pin(this is true for rasp board)
stepper.setEnablePin(X_ENABLE_PIN);
```

## setMaxSpeed/setAcceleration under subdivision

电机进行细分时对最大速度、加速度的影响。原本是没有考虑这种影响，在增大电机细分（使得控制更加精准）后发现速度远小于预期，尝试后发现需要在设置 maxspeed 与 acceleration 时考虑细分的影响。具体到代码上，对包装后的电机进行初始化时需要：

``` cpp
// AccelStepperDecorate.cpp
//[...]
this->maxSpeed = maxSpeed * subdivision;
this->acceleration = acceleration * subdivision;
//[...]
```

## `||`

这个错误是最有趣的，是我第一次亲自遇到与或运算的“短路”特性，教科书诚不欺我啊:)。

我需要同时运动多个电机，如果有任何一个电机未完成运转便继续下去，否则便结束。调用 `AccleStepper` 的 `run()` 方法，其返回值是是否完成一步运动（完成返回 true，否则返回 false）。开始时代码关键部分如下：

``` cpp
// MultiStepperDecorate.cpp


// Returns true if any motor is still running to the target position.
boolean MultiStepperDecorate::runAccel()
{
    uint8_t i;
    boolean ret = false;
    for (i = 0; i < _num_steppers; i++)
    {
    ret = ret || _steppers_decorate[i]->run(); 
    }
    return ret;
}
```

结果便是只有第一个电机运动结束，第二个电机才会运行。。。

只需将包含 `||` 的语句调换位置，下面是目前的代码：

``` cpp
// MultiStepperDecorate.cpp


// Returns true if any motor is still running to the target position.
boolean MultiStepperDecorate::runAccel()
{
    uint8_t i;
    boolean ret = false;
    for (i = 0; i < _num_steppers; i++)
    {
    ret = _steppers_decorate[i]->run() || ret; // if there are steppers have not stoped, just keep running, pay ATTENTION TO THE ORDER
    }
    return ret;
}
```

其实，完全可以先进行运转然后再判断，这样会减少错误机会，即：

``` cpp
bool tmp_ret = _steppers_decorate[i]->run()
ret = tmp_ret || ret; 
```


# Homework 2.Below are four faulty programs. Each includes a test case that results in failure. Answer the following questions (in the next slide) about each program.

``` cpp
// program 1
public int findLast (int[] x, int y) {
    //Effects: If x==null throw NullPointerException 
    // else return the index of the last element    
    // in x that equals y. 
    // If no such element exists, return -1
    for (int i=x.length-1; i > 0; i--) 
    { 
        if (x[i] == y) 
        {
            return i; 
        }
     }
    return -1; 
}
// test: x=[2, 3, 5]; y = 2
// Expected = 0
```

``` cpp
// program 2
public static int lastZero (int[] x) {
    //Effects: if x==null throw NullPointerException
    // else return the index of the LAST 0 in x.
    // Return -1 if 0 does not occur in x
    for (int i = 0; i < x.length; i++)
    {
         if (x[i] == 0)
        {
              return i;
         } 
     } return -1;
}


// test: x=[0, 1, 0]
// Expected = 2
```

Questions:
* 1.Identify the fault.
* 2.If possible, identify a test case that does not execute the fault. (Reachability)
* 3.If possible, identify a test case that executes the fault, but does not result in an error state.
* 4.If possible identify a test case that results in an error, but not a failure.


1.Fault 分析：
第一个程序是没有进行完全遍历（`i>0` 会使得 x[0] 无法进行检验）；
第二个程是遍历顺序有误 `for (int i = 0; i < x.length; i++)`，会得到 firstZero 而不是 lastZero。

2.a test case that does not execute the fault, 即保证需程序不会运行到 Falut 的语句，因为程序总是要先进入循环，对于第二个程序无法做到 `does not execute the fault`，对于第一个进入循环后也是会先进行 `i>0` 的判断，所以，无法找到合适的测试用例满足要求。


3.a test case that executes the fault, but does not result in an error state，即运行了 Falut 对应的代码，但没有导致 error state 的出现。

简单的例子可以是，不包含所要求的元素，举例如下：

第一个程序：
``` vi
test:x=[1];y=2
Expected = -1

Got = -1
```

第二个程序：
``` vi
test:x=[1];
Expected = -1

Got = -1
```

4.a test case that results in an error, but not a failure. 即算然是 error 的结果，但与预期相同（与 3 略有不同）：

第一个程序：
``` vi
test:x=[1,2];y=2
Expected = 1

Got = 1
```

第二个程序：
``` vi
test:x=[1,0];
Expected = 1

Got = 1
```


当然，上面的举例并没有涵盖所有可能性，但很有助于对 `fault`,`error` 以及 `failure` 的理解。