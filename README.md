# 项目简介

本项目是中国科学院大学人工智能学院本科自然语言处理课程的第一次作业。

目标是收集大量的中英文文本，并对这些文本进行处理与分析。通过计算字母和汉字的熵值，观察不同规模文本数据下的熵值变化，分析语言结构的特性。同时，通过构建词汇表，探究词汇量的增长趋势。本项目涉及以下几个主要功能模块：

## 项目结构

```
├── LICENSE
├── README.md  # 项目简介
├── data  # 中英文文本数据
│   ├── cn
│   │   ├── data.json  # 中文数据
│   │   └── tokens.json  # 中文标注数据
│   └── en
│       ├── data.json  # 英文数据
│       └── tokens.json  # 英文标注数据
├── docs  # 文档和报告
│   ├── images  # 数据分析生成的图像
│   └── report.md  # 数据分析报告
├── main.ipynb  # 主实验脚本，包含熵值计算、词汇量统计等
├── utils  # 工具模块
│   ├── cleaning.py  # 文本清理工具
│   ├── distribution.py  # 分布计算工具
│   ├── entropy.py  # 熵值计算工具
│   └── tokenization.py  # 分词工具
└── xinhua-crawler  # 数据爬取模块
    ├── crawler_requests.py  # 基于requests的爬虫
    ├── news_crawler  # 基于Scrapy的新闻爬虫
    ├── utils  # 爬虫工具
```

## 功能模块介绍

### 1. 文本处理与清洗 (`utils/cleaning.py`)

- `clean_cn`：清理中文文本，去除不必要的字符和符号，规范化标点符号。
- `clean_en`：清理英文文本，去除不必要的符号并规范文本格式。

### 2. 分词工具 (`utils/tokenization.py`)

- `tokenize_cn`：对中文文本进行分词，支持去除标点符号等。
- `tokenize_en`：对英文文本进行分词，支持去除标点符号等。
- `split_sentences_cn` 和 `split_sentences_en`：按句号等标点符号进行句子拆分。

### 3. 熵值计算 (`utils/entropy.py`)

- `cal_entropy`：计算给定文本的熵值。
- `entropy_curve`：根据文本数据量绘制熵值变化曲线。

### 4. 数据分布与词汇量统计 (`utils/distribution.py`)

- `pdf_curve`：绘制数据的概率密度分布曲线。
- `vocab_size_curve`：根据文本数据量统计词汇量变化趋势。

### 5. 数据爬取 (`xinhua-crawler`)

- 这是一个Git子仓库，位于`SunnyYYLin/xinhua-crawler`，这样设计是为了便于复用。
- `crawler_requests.py`：使用 `requests` 库的新闻爬虫，用于抓取新华网新闻数据。
- `news_crawler`：基于 `Scrapy` 框架的新闻爬虫，支持多线程抓取。

## 实验内容

`main.ipynb` 文件中包含了实验的主要步骤，包括：

1. 收集并处理中英文文本数据。
2. 计算不同文本规模下的熵值，并与参考文献中的结果进行对比。
3. 分析词汇量的增长趋势。
4. 绘制各类分析图表，展示结果。

## 数据

项目中的数据以 `json` 格式存储，其中包含文本内容及其对应的标注数据。由于数据过大，没有随代码上传，请运行指令爬取：
```bash
cd xinhua-crawler
scrapy crawl news_spider -s OUTPUT_DIR="../data/cn" -a language="cn" -a start_keyword="1" -s CLOSESPIDER_ITEMCOUNT=50000
scrapy crawl news_spider -s OUTPUT_DIR="../data/en" -a language="en" -a start_keyword="a" -s CLOSESPIDER_ITEMCOUNT=100000
```

## 如何运行项目

1. 克隆仓库
    ```bash
    gh repo clone SunnyYYLin/text-entropy
    ```

2. 安装依赖库：
   ```bash
   pip install requests bs4 lxml scrapy matplotlib tqdm jieba regex
   ```

3. 使用 `xinhua-crawler` 目录中的爬虫脚本抓取新闻数据。

4. 运行 `main.ipynb` 以执行主要实验代码。

## 可视化与分析

实验结果会生成各类图表，存储在 `docs/images/` 目录中。您可以查看 `report.md` 以获取详细的分析报告。

## 许可证

本项目遵循 [MIT License](./LICENSE)。