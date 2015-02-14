# 豆瓣·我读

`dbmc`（Douban Book My Collections）可获取用户的`我读`数据，并生成相应的`Markdown`文件，方便嵌入到个人的静态站点中使用。


## quickstart

- 将项目克隆到本地后，将`config.py`中的`DBID`变量替换成你自己的豆瓣ID。
- `pip install -r requirements.txt` 来安装依赖。
- 使用`python dbmc.py`生成我读的 Markdown 文件，默认在 output 目录下。
- 将生成的文件放到自己的静态站点源码目录中，即可生成个人风格的豆瓣读书主页。例如我的[我读](http://daily.page7.me/posts/2015/02/book/)


## 模板

- 项目使用[Jinja2]()来渲染，模板的路径在`config.py`中设置。也可以自己修改模板。