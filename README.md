# beancount-sample

个人使用 Beancount 总结的一份模板。

- [使用 Beancount 记账篇零：Beancount 入门使用](https://blog.einverne.info/post/2021/02/beancount-introduction.html)
- [使用 Beancount 记账篇一：给账户命名](https://blog.einverne.info/post/2021/02/beancount-account-name-template.html)
- [使用 Beancount 记账篇二：各类账单导入](https://blog.einverne.info/post/2021/02/beancount-import-bill.html)
- [使用 Beancount 记账篇三：周期账单](https://blog.einverne.info/post/2022/02/beancount-installment.html)
- [使用 Beancount 记账篇四：证券交易](https://blog.einverne.info/post/2021/02/beancount-stock-market.html)
- [使用 Beancount 记账篇五：使用 Telegram Bot 简化记账](https://blog.einverne.info/post/2021/03/beancount-telegram-bot.html)
- [使用 Beancount 记账篇六：利用 VS Code 插件辅助](https://blog.einverne.info/post/2021/03/beancount-vscode-plugin.html)
- [https://blog.einverne.info/post/2023/11/beancount-fava.html](https://blog.einverne.info/post/2023/11/beancount-fava.html)

## 导入交通银行信用卡账单
install requirements

```
pip install -r requirements.txt
```

and then

```shell
export PYTHONPATH=.
bean-extract config.py datas/comm-2021.01.csv > beans/comm-2021.01.bean
```


## 致谢

- [lidongchao](https://github.com/lidongchao/BeancountSample)
