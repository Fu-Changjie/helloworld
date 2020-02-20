# helloworld
hi～
# 这是什么？——本仓库介绍
这是一个测试、讨论、学习用的仓库，在这里你可以练习生成、上传`patch`与使用`patch`生成`rpm`包的相关操作。
## 文件结构

|文件|描述|
|:--------------:|:-------------:|
|  *.patch   |从原始源码版本升级至当前源码版本所需要的所有补丁（patch）|
|helloworld.tar.gz|原始源码包|
|LICENSE|版权许可证|
|README.md|使用文档|
|helloworld.spec|将当前源码编译为二进制包所需的spec文件|

# 如何操作？
## 运行helloworld-构建rpm包
1. 确保已安装`rpm-build`，`gcc-c++`  
```
dnf install rpm-build
dnf install gcc-c++
```

2. 将`helloworld.tat.gz`和所有`patch`文件放到`/root/rpmbuild/SOURCES`目录下
3. 将`helloworld.spec`放到`/root/rpmbuild/SPECS`目录下
4. 以`root`用户执行  
`rpmbuild -ba /root/rpmbuild/SPECS/helloworld.spec`  
这一步将在`/root/rpmbuild/BUILD`目录下生成源码`src`，其中包含`a.cpp`。  

> 相关选项：`-ba`指`build all`。`-bp`准备，解压与打补丁。  

5. 还会根据spec文件自动生成源码包（`.src.rpm`） 和二进制包。最后会有两个`write to `指明包所在的目录。生成`SPRMS`目录，存储`src.rpm`包；`RPMS`存储`x86_64.rpm`包。  
![writeto](https://img-blog.csdnimg.cn/2020021910151023.png)  

6. 安装二进制包`rpm -ivh /root/rpmbuild/RPMS/x86_64/helloworld-1-0.fc31.x86_64.rpm`   
7. 找到安装目录  
`rpm -ql helloworld-1-0.fc31.x86_64`  
![find](https://img-blog.csdnimg.cn/20200219111257449.png)  
8. 运行  
`/bin/helloworld`  
![run](https://img-blog.csdnimg.cn/20200219111332287.png)  

现在可以运行程序、查看源码。
## 修改源码
注意在修改源码**之前**要先提交一次初始状态。
1. 在`/root/rpmbuild/BUILD`目录下，找到源码那一层，初始化git仓库：  
`git init`    
>如果没有采用`rpmbuild`来构建`rpm`包运行程序，而是通过自己`make`编译，那么需要在初始化`git`仓库之后按照顺序把`patch`依次打到源码上，再提交初始状态。`rpmbuild`会自动完成打`patch`操作。  

2. 将初始状态提交，这样修改之后可以根据这次提交来做`patch`  
```
git add -A
git commit -m "Package init"
``` 
![修改前](https://img-blog.csdnimg.cn/20200219131051373.png)  
**修改源码……**  
3. 注意如果使用`make`，要在修改源码后立即提交，再用`make`进行编译，否则会将编译出来的二进制包全部作为更新来提交。  

## 基于修改后的提交生成新patch
修改源码后，进行提交，根据提交生成`patch`：  
```
git add -A
git commit -m "[对本次修改的简短介绍]"
git format-patch HEAD^
```

> 注：`git format-patch HEAD^` 本义为生成上一个改动至今的`patch`， 若想生成多个改动前至今的`patch`可以使用命令 `git format-patch [commit号]`。  

![修改后](https://img-blog.csdnimg.cn/20200219131254411.png)  
## 修改spec文件中的相关说明
1. `release`版本号`+1`
2. 添加`Patch 000x: patch_name` 
3. 添加`changelog`，格式示例：  

```
%changelog
* Wed Feb 19 2020 fuchangjie <changjie.fu@cs2c.com.cn> - 1.0.0-2
- Add a.cpp to say hello world

* Sat Dec 21 2019 user.name <user.name@example.com> - 1.0.0-1
- Package init
```

**完成！请推送并提交pr**  

## 附：
### 应用patch
由于`tar.gz`内是初始源码，没有应用过任何`patch`，所以运行前需要将其解压后，在解压目录下挨个应用`patch`：  
`git am 0001-add-something.patch`  
如果出现报错：  
`Patch format detection failed`   
则使用`git apply`来应用`patch`
### 贡献流程
1. 已提交更新至个人仓库新分支
2. 点击进入新分支，创建`pull request`，从个人分支到上游仓库
3. 撰写`pull request`的题目，尽量简明扼要表述更新内容
4. 撰写`pull request`的描述，建议包含问题、解决/修改方案、来源等  
>`pull request`要尽量让`reviewer`可以快速了解到你的修改原因、内容、目的。  
推送之前请检查自己的`commit`（提交记录）是否合为一次，因为向上游推送一个含有多个`commit`的`pull request`是不合理的。
