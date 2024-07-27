# 基于AHK V2的快捷键方案

> AHK是一个生产力工具，用于优化人机交互。
>
> 以下笔记基于AHK V2。

## 一、增加「伪修饰键」

热键一般由修饰键+其他按键组成，所以越多修饰键就可以组成越多的热键。但是常用的修饰键（比如Ctrl、Shift、Alt、Win）一般已经绑定有特定功能，限制了自由发挥的空间。这时我们可以考虑在不影响正常使用的情况下，将一些按键转换成「伪修饰键」，比如说重音键、大写键，空格键，反斜杠键。代码如下。

```autohotkey
;将以下按键转换成「伪修饰键」的同时保证其正常使用。

`::`            ;保证[重音键]的正常使用。
Space::Space    ;保证[Space]的正常使用。
\::\            ;保证[反斜杠]的正常使用。

CapsLock::      ;保证[CapsLock]的正常使用。
{
    SetCapsLockState(GetKeyState("CapsLock", "T") ? "AlwaysOff" : "AlwaysOn")
}
```

有了新的修饰键后，我们就可以利用新的修饰键加上其他按键构建出平行的热键层（hotkey layer），在新的热键层中自由地定义我们想要的功能。建议优先定义以下功能：

```autohotkey
; 可以选择在「重音键」的热键层定义以下基础功能。
` & r::Reload  ;重载脚本。
` & l::ListVars  ;显示所有脚本变量。
` & k::KeyHistory ;显示按键历史。

; 或者是在「大写键」的热键层进行定义。
CapsLock & r::Reload  ;重载脚本。
CapsLock & l::ListVars  ;显示所有脚本变量。
CapsLock & k::KeyHistory ;显示按键历史。
```

## 二、划分脚本，优化总体结构

1. 根据作用范围，我们可以将热键分为**全局热键**和**局部热键**，保存到不同的子脚本中，通过 `#Include` 语句包含到 `main.ahk` 中。
2. 对于**全局热键**，为不同的修饰键创建对应的子脚本，收纳相关热键。
3. 对于**局部热键**，可以通过 `#HotIf` 语句限定其作用范围。为不同的软件ID创建对应的子脚本，收纳相关热键。
4. 使用专用的脚本，在每次reload时，将所有合适的子脚本include到公共的 `include_all.ahk` 中，方便开发调试。

## 三、版本管理

1. 使用 VS Code + git + GitHub 进行版本管理。
2. 使用插件 `thqby.vscode-autohotkey2-lsp` 辅助开发。

## 四、自用库&开源库

1. 编写自用库：比如`pathlib.ahk`。
2. 引用开源库：比如`FindText.ahk`， `json.ahk`。
