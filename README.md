# beancount-sample

个人使用 Beancount 总结的一份模板。

- [使用 Beancount 记账篇零：Beancount 入门使用](https://einverne.github.io/post/2021/02/beancount-introduction.html)
- [使用 Beancount 记账篇一：给账户命名](https://einverne.github.io/post/2021/02/beancount-account-name-template.html)
- [使用 Beancount 记账篇二：各类账单导入](https://einverne.github.io/post/2021/02/beancount-import-bill.html)
- [使用 Beancount 记账篇三：周期账单](https://einverne.github.io/post/2022/02/beancount-installment.html)


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
