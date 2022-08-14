# user.py

定义了一个UserStatus类，用于储存User的状态。

采用类全局变量 `users_status` 用于储存所有有状态用户的信息。同时由于这个特性，所有的用户状态信息会在**程序关闭之后**清空且无法恢复。其结构如下

**user_status 内部结构**
|Key|Value|
|:----:|:----|
|user_id|user_status|

其中，内部的 `user_status` 指**单个用户**的用户状态信息，正常情况下应该为一个字典。且一个用户只能存在一个key，所以某一个用户的所有信息都会储存在这个 `user_status` 之中。其中通过一个个kv对储存用户的各种信息。

**user_status 内部结构**

|Key|Value|
|:----:|:----|
|status|setting_anti_ad_config|
|anti_ad_conf_1|'哈希竞猜'|
|some_other_keys|some_value|

其中，`status` 被认为应该是**永远存在的基本量**，用于确定用户目前账户所处的状态以及状态更新的时间。比如正在录入设置，又或是正在进行某些需要保存状态的操作，而下面**所有的其他kv对则是在这种状态下产生的数据**，他们需要被保存起来以进行其他的处理。

**关于调用/写入状态**

如果没有特殊必要，建议统一使用 `get_status` 和 `set_status` 进行处理。前者提供**自动读取特定key**的value_list(包含value和浮点timestamp)，后者支持**自动写入时间**。

<br>
<br>
<br>

---

<br>
<br>
<br>

关于 `status` 和 `acc_status` ，这里分别用于**两种不同的功能**：
- status: 用于**用户本地状态的储存**相关变量的命名
- acc_status: 用于**用户服务器上储存状态**的命名，代表**账号的身份** *（会员，管理员等等）*
