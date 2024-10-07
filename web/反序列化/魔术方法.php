<?php
class student{
    // 定义私有属性$name，初始值为123
    private $name=123;
    // 定义公有属性$number
    public $number;

    // 构造函数，初始化$number为123
    public function __construct(){
        $this->number = 123;
    }
    // 析构函数，输出"destruct"
    public function __destruct(){
        echo "\ndestruct";
    }
    // 唤醒函数，输出"wakeup"
    public function __wakeup(){
        echo "\nwakeup";
    }
    // 将对象转换为字符串，返回$name的值
    public function __toString(){
        return $this->name;
    }
    // 获取属性$name的值，输出"get"
    public function __get($name){
        echo "\nget";  
    }
    // 设置属性$name的值，输出"set"
    public function __set($name,$value){
        echo "\nset";
    }

    // 调用不存在的方法，输出"call"
    public function __call($name,$args){
        echo "\ncall";
    }
    // 调用对象，输出"invoke"
    public function __invoke(){
        echo "\ninvoke";
    }
    // 序列化对象，输出"sleep"
    public function __sleep(){
        echo "\nsleep";
    } 
    // 唤醒对象，输出"wakeup"
    public function __wakeup(){
        echo "\nwakeup"; 
    }
    // 判断属性$name是否存在，输出"isset"
    public function __isset($name){
        echo "\nisset";
    }
    // 删除属性$name，输出"unset"
    public function __unset($name){
        echo "\nunset";
    }

    // 输出"hello"
    public function hello(){
        echo "\nhello";
    }
}
// 创建对象$xiaoming
$xiaoming = new student();
// $xiaoming->name='xiaoming';
// $xiaoming->hello();
// 将对象$xiaoming序列化，并使用urlencode进行编码
echo urlencode(serialize($xiaoming));

// $a = unserialize('O:7:"student":2:{s:4:"name";s:8:"xiaoming";s:6:"number";i:123;}');
$a = unserialize(urldecode('O%3A7%3A%22student%22%3A2%3A%7Bs%3A13%3A%22%00student%00name%22%3Bi%3A123%3Bs%3A6%3A%22number%22%3BN%3B%7D'));
// echo $a->name;
echo $a->hello();
?>