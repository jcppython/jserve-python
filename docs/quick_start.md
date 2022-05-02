# jserve 介绍

1. 包含 http、rpc、scoketio 等多类接口的 server 服务组件
2. 重点解决 web-client 和 server 间双向通信的痛点

# 主要组件

# 数据获取

## 配置数据
> 所有请求无关的数据，都应该放在 configure 内，本质是 dict 对象（可包罗万千）

1. 使用说明: 内置 jserve 已完成 configure.init() 初始化
2. 使用示例:

```
import configure

// 赋值
// 如果确定 ['a'] 存在，可以按以下形式赋值
configure.options['a']['b'] = 'value'

// 否则通过接口赋值
configure.options.add_option('a.b.c', 'value')

// 获取
v = configure.options['a']['b']
```

## 会话信息

请求粒度的信息：和认证/请求环境相关信息（与请求业务逻辑无关）

你不应该直接读写 session 和 cookie ?
你的逻辑中不应该直接使用 sio 和 tornado 组件对象，仅能使用
你的逻辑应该能被不同类型的请求触发，只要有以下组件即可

-configure
-request
-response
-method
-talk

```
''' session 在 socketio 和 http 中是否有区别? '''
session = await sio.get_session(sid, namespace=namespace)
# await sio.save_session(sid, {'username': username}, namespace=namespace)
print(session['username'])
```

# 双向通信（socketio）
> 详见官方文档 [python-socketio]

## server 向 client 发送数据

1. 你任何时候都可以向 client 发送数据，只要双方连接中
2. a message payload of type str, bytes, list, dict or tuple, and the recipient room

```
// 给所有 client 发送
sio.emit('my event', {'data': 'foobar'})

// 给指定 client 发送
sio.emit('my event', {'data': 'foobar'}, room=user_sid)

// server 处理数据后 return 返回确认数据触发 client callback, 注意，它必须是最后一个参数
sio.emit('my event', {'data': 'foobar'}, room=user_sid, callback)
```

## 多路复用（同一物理链路）
> the default namespace is '/'

## 会话 session 使用

1. the contents of the user session are destroyed when the client disconnects
2. user session contents are not preserved when a client reconnects after an unexpected disconnection from the server

```
// 写
await sio.save_session(sid, {'username': username}, namespace=namespace)

// 读
with sio.session(sid, namespace=namespace) as session:
    session['username']

// 异步接口中
async with sio.session(sid, namespace=namespace) as session:
    session['username'] = username
```

## server 间通信
> 目前采用 redis 方案，依赖 aioredis 包

## 使用注意
1. 不同集群直接的 namespace 必须不同

- 路由
```
/socket.io/{your cluster flag}
```

2. 如果采用集群部署，load balancer 必须采用 sticky-session 保证同一会话交互落到同一实例

- [nginx config](https://socket.io/docs/v4/using-multiple-nodes/)

# 参考
- [socket.io]: https://socket.io/
- [python-socketio]: https://python-socketio.readthedocs.io/en/latest/server.html
- [tornado-web]: https://www.tornadoweb.org/en/stable/

