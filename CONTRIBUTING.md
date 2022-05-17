# 开发注意

> 目前项目 test 存在问题

- 注意：我们采用主干开发，你总是应该提交到 master 分支，它不总是靠谱可用的
- 我们总是保证 stable 分支是可用的，是相对稳定将要发版的
- 如果你有一个重大的 feature 需要持续开发，可以创建一个对应的分支

- 管理好你的版本号，不要“过于频繁”的发布。记住：用户不会手工维护他们每个安装模块的不同的版本

# 测试文档

- 我们采用 tox 提供的 “Python的标准化测试”

# 项目文档

- 依赖：sphinx
- 命令

```
sphinx-apidoc -F -o docs jserve
cd docs
make html
```

# 上传包

```
// upload first time
python3 -m twine upload  dist/*

// upload for update
```

# todo

- jserve 如何设计能使子包如何更加独立?
    - configure/log/talk 等在 jhttp/jsocketio 中耦合

- configure 是否要侵入到 jhttp、jsocketio 等组件内?
    - 对比：jhttp 等组件定义自己的配置，外层从 configure 剥离出相关配置（这里相当于多了一层显冗余的接偶转化）
    - 有没有更好的办法两者兼得
    - 优点：传参数等方便，复用 configure 通路
    - 缺点：总感觉哪里有耦合

- 不支持 python 3.9+
    - eventlet 0.33.0 and below doesn't support Python3.9+/kqueue (default hub on FreeBSD, Mac OSX, possibly other BSDs).
    - https://github.com/eventlet/eventlet/issues/670


# 参考
- https://packaging.python.org/en/latest/tutorials/packaging-projects/
- https://www.oschina.net/translate/open-sourcing-a-python-project-the-right-way
- https://juejin.cn/post/6966606637612138504
- [setup-vs-requirement]: https://caremad.io/posts/2013/07/setup-vs-requirement/
