#!/usr/bin/env python3
import sys

from beancount.core.data import Transaction

sys.path.append("./importers")
from importers.beanmaker import Drcr, Col, Importer

# Col为枚举类型，预定义了每笔交易记录所需要的内容，_config_alipay负责定义枚举内容与csv表头之间的对应关系

_config_alipay = {
    Col.DATE: "交易创建时间",
    Col.PAYEE: "交易对方",
    Col.NARRATION: "商品名称",
    Col.REMARK: "备注",
    Col.AMOUNT: "金额（元）",
    Col.DRCR: "收/支",
    Col.STATUS: "资金状态",
    Col.TXN_TIME: "交易创建时间",
    Col.TXN_DATE: "交易创建时间",
    Col.TYPE: "类型",
}

_config_wechat = {
    Col.DATE: "交易时间",
    Col.PAYEE: "交易对方",
    Col.NARRATION: "商品",
    Col.REMARK: "支付方式",
    Col.AMOUNT: "金额(元)",
    Col.DRCR: "收/支",
    Col.STATUS: "当前状态",
    Col.TXN_TIME: "交易时间",
    Col.TXN_DATE: "交易时间",
    Col.TYPE: "交易类型",
}

# _default_account负责定义默认账户
_default_account_alipay = "Assets:Alipay:Balance"

_default_account_wechat = "Assets:WeChat:Balance"

_default_account_comm = "Liabilities:CreditCard:BOC:CN"

# _currency定义货币单位
_currency = "CNY"

# Debit_or_credit也是枚举类型，预定义了支出和收入两类，_DRCR_dict负责定义这两类与csv中能够表明该状态的文本之间的对应关系
_DRCR_dict = {
    Drcr.DEBIT: "支出",
    Drcr.CREDIT: "收入"
}

common_assets_account = {
    "交通银行|2987": "Liabilities:CreditCard:BOC"
}

# _assets_account负责保存账户信息，key为手工对账时在备注中输入的关键词；
# 关键词中，"DEFAULT"为非必选项，不提供时将以"_default_account_xxx"的属性值作为"DEFAULT"对应的值；
# 多个关键词用竖线分割，只要备注中出现该关键词，就把该交易分类到对应账户下。
_wechat_assets_account = {
    "DEFAULT": "Assets:WeChat:Balance",
    "招行信用卡|0000": "Liabilities:CreditCard:CMB",
    "招商银行": "Assets:DebitCard:CMB",
    "交通信用卡银行|2987": "Liabilities:CreditCard:BOC:CN",
    "中信银行": "Liabilities:CreditCard:CITIC",
    "汇丰银行": "Liabilities:CreditCard:HSBC:CN",
    "支付宝": "Assets:VirtualCard:Alipay",
    "余额宝": "Assets:MoneyFund:Yuebao",
    "零钱|微信": "Assets:WeChat:Balance"
}
_wechat_assets_account.update(common_assets_account)

# _debit_account负责保存支出账户信息，key为与该账户相关的关键词；
# 关键词中，"DEFAULT"为非必选项，不提供时将以"_default_account_xxx"的属性值作为"DEFAULT"对应的值；
# 多个关键词用竖线分割，只要当交易为“支出”，且交易对方名称和商品名称中出现该关键词，就把该交易分类为对应支出。
_debit_account = {
    "DEFAULT": "Expenses:Food:Other",
    "iCloud|腾讯云|阿里云|Plex": "Expenses:Fun:Subscription",
    "滴滴|司机": "Expenses:Transport:Taxi",
    "天和亿|单车": "Expenses:Transport:Bike",
    "中国铁路": "Expenses:Transport:Railway",
    "张夏": "Expenses:House:WaterElectricity",
    "卡表充值|燃气": "Expenses:House:Gas",
    "友宝|勇这直上|芬达|雪碧|可乐|送水|怡宝|饮料|美年达|博雅铭远科技|售货机": "Expenses:Food:Drinks",
    "迪亚天天": "Expenses:Daily:Commodity",
    "水果": "Expenses:Food:Fruits",
    "买菜|叮咚|美团买菜": "Expenses:Food:Cooking",
    "泰餐": "Expenses:Food:Restaurant",
    "App Store|Steam|会员": "Expenses:Fun:Software",
    "全时|华联|家乐福|超市|红旗|WOWO|百货|伊藤|永旺|全家": "Expenses:Daily:Commodity",
    "汽车票|蒜芽信息科技|优步|火车|动车|空铁无忧网|滴滴|汽车|运输|机场|航空|机票|高铁|出行|车费|打车": "Expenses:Travel",
    "捐赠": "Expenses:PublicWelfare",
    "话费|流量|手机|中国移动": "Expenses:Daily:PhoneCharge",
    "电影|大麦网|演出|淘票票": "Expenses:Fun:Amusement",
    "地铁|轨道交通": "Expenses:Transport:Public",
    "青桔|骑安": "Expenses:Transport:Bike",
    "衣|裤|鞋": "Expenses:Dressup:Clothing",
    "造型|美发|理发": "Expenses:Dressup:Hair",
    "化妆品|面膜|洗面奶": "Expenses:Dressup:Cosmetic",
    "医院|药房": "Expenses:Health:Hospital",
    "酒店|airbnb": "Expenses:Travel:Hotel",
    "机票|高铁|票务|特快|火车票|飞机票": "Expenses:Travel:Fare",
    "借款": "Assets:Receivables",
    "蚂蚁财富": "Assets:MoneyFund:BondFund",
    '亲属卡': "Expenses:Parents:Daily",
    '签证': "Expenses:Travel:Visa",
    "门票": "Expenses:Travel:Ticket",
    "gopro|键盘|电脑|手机|SD卡|相机|MacBook|boox|ipad|apple|oneplus": "Expenses:Digital",
    "快递": "Expenses:Daily",
    '公众号付费|知识助手': "Expenses:Fun:Subscription",
    'PLAYSTATION': "Expenses:Fun:Game",
}

# _credit_account负责保存收入账户信息，key为与该账户相关的关键词
# 关键词中，"DEFAULT"为非必选项，不提供时将以"_default_account_xxx"的属性值作为"DEFAULT"对应的值；
# 多个关键词用竖线分割，只要当交易为“收入”，且交易对方名称和商品名称中出现该关键词，就把该交易分类为对应收入。
_credit_account = {"DEFAULT": "Income:RedPacket", "借款": "Assets:Receivables"}

wechat_config = Importer(
    config=_config_wechat,
    default_account=_default_account_wechat,
    currency=_currency,
    file_name_prefix='微信支付账单',
    skip_lines=0,
    DRCR_dict=_DRCR_dict,
    assets_account=_wechat_assets_account,
    debit_account=_debit_account,
    credit_account=_credit_account
)

_alipay_assets_account = {
    "DEFAULT": "Assets:Alipay:Balance",
    "花呗": "Liabilities:VirtualCard:Huabei",
}
_alipay_assets_account.update(common_assets_account)

alipay_config = Importer(
    config=_config_alipay,
    default_account=_default_account_alipay,
    currency=_currency,
    file_name_prefix='alipay_record',
    skip_lines=0,
    DRCR_dict=_DRCR_dict,
    assets_account=_alipay_assets_account,
    debit_account=_debit_account,
    credit_account=_credit_account
)

_comm_assets_account = {
    "DEFAULT": "Liabilities:CreditCard:BOC:CN"
}
_comm_assets_account.update(common_assets_account)

from beancount.ingest.importers import csv

# 优逸白金信用卡
_config_com = {
    csv.Col.DATE: "记账日期",
    csv.Col.PAYEE: "交易说明",
    csv.Col.NARRATION: "交易说明",
    csv.Col.AMOUNT_DEBIT: "交易金额",
    csv.Col.TXN_DATE: "交易日期",
    csv.Col.LAST4: "卡末四位",
}


def comm_categorizer(txn: Transaction):
    # At this time the txn has only one posting
    try:
        posting1 = txn.postings[0]
    except IndexError:
        return txn

    from importers.beanmaker import mapping_account
    account_name = mapping_account(_debit_account, txn.narration)

    posting2 = posting1._replace(
        account=account_name,
        units=-posting1.units
    )
    # Insert / Append the posting into the transaction
    if posting1.units < posting2.units:
        txn.postings.append(posting2)
    else:
        txn.postings.insert(0, posting2)

    return txn


comm_config = csv.Importer(
    config=_config_com,
    account=_default_account_comm,
    currency=_currency,
    last4_map={"2987": "优逸白"},
    categorizer=comm_categorizer
)

CONFIG = [
    wechat_config,
    alipay_config,
    comm_config,
]
