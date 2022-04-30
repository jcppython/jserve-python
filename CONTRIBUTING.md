# 开发注意

> 目前项目 test 存在问题

- 我们总是保证 master 分支是可用的，但不一定稳定
- 我们总是保证 stable 分支是可用的，是相对稳定将要发版的
- 你总是应该提交到 develop 分支，我们会在合适的时间合并到 master 分支
- 如果你有一个重大的 feature 需要持续开发，可以创建一个对应的分支

- 管理好你的版本号，不要“过于频繁”的发布。记住：用户不会手工维护他们每个安装模块的不同的版本

# 测试文档

- 我们采用 tox 提供的 “Python的标准化测试”

# TODO.md

```
// upload first time
python3 -m twine upload  dist/*

// upload for update
```

# 参考
- https://packaging.python.org/en/latest/tutorials/packaging-projects/
