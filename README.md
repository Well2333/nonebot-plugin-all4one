<div align="center">
    <img width="200" src="https://raw.githubusercontent.com/nonepkg/nonebot-plugin-all4one/master/docs/logo.png" alt="logo"></br>

# Nonebot Plugin All4One

让 [NoneBot2](https://github.com/nonebot/nonebot2) 成为 OneBot 实现！

[![License](https://img.shields.io/github/license/nonepkg/nonebot-plugin-all4one?style=flat-square)](LICENSE)
![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg?style=flat-square)
[![NoneBot Version](https://img.shields.io/badge/nonebot-2.3.0+-red.svg?style=flat-square)](https://v2.nonebot.dev/)
[![OneBot 4A](https://img.shields.io/badge/OneBot-4A-black?style=flat-square)](https://onebot4all.vercel.app/)
[![PyPI Version](https://img.shields.io/pypi/v/nonebot-plugin-all4one.svg?style=flat-square)](https://pypi.python.org/pypi/nonebot-plugin-all4one)
[![codecov](https://codecov.io/gh/nonepkg/plugin-all4one/branch/master/graph/badge.svg?token=BOK429DAHO)](https://codecov.io/gh/nonepkg/plugin-all4one)

</div>

## 安装

- 使用 nb-cli

```sh
nb plugin install nonebot-plugin-all4one
```

- 使用 pdm

```sh
pdm add nonebot-plugin-all4one
```

## 使用

```dotenv
obimpl_connections = [{"type":"websocket_rev","url":"ws://127.0.0.1:8080/onebot/v12/"}] # 其它连接方式的配置同理
middlewares = ["OneBot V11"] # 自定义加载的 Middleware，默认加载全部
block_event = False # 是否中止已转发 Event 的处理流程，默认中止
blocked_plugins = ["echo"] # 在 block_event=False 时生效，可自定义处理流程中要中止的插件
```

## Feature

### OneBot

- [x] HTTP
- [x] HTTP Webhook
- [x] 正向 WebSocket
- [x] 反向 WebSocket

### Middlewares

- [x] [OneBot V11](https://github.com/nonebot/adapter-onebot)
- [x] [Telegram](http://github.com/nonebot/adapter-telegram)
- [ ] [QQ](https://github.com/nonebot/adapter-qq) [@he0119](https://github.com/he0119) 寻求新维护者

## 相关链接

- [nonebot-adapter-onebot](https://github.com/nonebot/adapter-onebot) 复用代码
- [zhamao-robot/go-cqhttp-adapter-plugin](https://github.com/zhamao-robot/go-cqhttp-adapter-plugin) OneBot V11 -> V12 逻辑参考
- [nonebot-plugin-params](https://github.com/iyume/nonebot-plugin-params) 灵感来源
- [felinae98/nonebot-plugin-send-anything-anywhere](https://github.com/felinae98/nonebot-plugin-send-anything-anywhere) 友情推荐
