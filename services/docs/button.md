# Botton.py

## 基本功能

用于生成Telegram的`InlineKeyboardBotton`格式的变量。（这里的`Botton`是指附着在**消息框下方**的按钮，而不是在输入框底下的按钮）

<br>
<br>
<br>

## 运行逻辑

本文件提供基本的`gen_markup`函数，由`function`内各个模块自行调用，然后生成满足需求的各种`InlineKeyboardDotton`

<br>
<br>
<br>

## 格式规范

**1.callback_data**

字典。

键值规范

|Key|Necessary|Value|
|:----|:----:|:----|
|botton|Required|(str) 按钮类型。用于记录最基本的按钮分类。如`help_gethelp`。<br>注意，如果按钮跟某些function有关，请尽量使用`function`_`botton`的格式，如：`setting_adblock`|
|time|Optional|(int) 时间。记录按钮生成的时间，如果有需要，也可以是其他时间，一般用于具有时效性的按钮|

<br>
<br>
<br>

---

