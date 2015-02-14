## 在读

{% for item in readings: %}[![{{ item.book.title }}]({{ item.book.images.medium }})]({{ item.book.alt }}) {% endfor %}

---

## 读过

{% for item in reads: %}[![{{ item.book.title }}]({{ item.book.images.medium }})]({{ item.book.alt }}) {% endfor %}

---

## 想读

{% for item in wishes: %}[![{{ item.book.title }}]({{ item.book.images.medium }})]({{ item.book.alt }}) {% endfor %}

本页通过[dbmc](https://github.com/whilgeek/dbmc)自动生成
