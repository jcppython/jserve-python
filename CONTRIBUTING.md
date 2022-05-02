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

# TODO.md

```
// upload first time
python3 -m twine upload  dist/*

// upload for update
```

# 参考
- https://packaging.python.org/en/latest/tutorials/packaging-projects/
- https://www.oschina.net/translate/open-sourcing-a-python-project-the-right-way
- https://juejin.cn/post/6966606637612138504
