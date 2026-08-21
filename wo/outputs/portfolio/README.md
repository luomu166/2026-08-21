# 我的作品集网站

一个纯 HTML / CSS / JS 的个人作品集网页，无需安装任何东西，双击就能打开。

## 如何预览

直接用浏览器打开 `index.html` 即可。

## 如何改成你自己的内容

打开 `index.html`，按下面的提示替换内容：

| 位置 | 要改什么 |
| --- | --- |
| 顶部导航和首屏 | “你的名字”、首屏下方的自我介绍 |
| 「关于我」 | 头像里的字、两段自我介绍、技能标签 |
| 「我的作品」 | 每张卡片的标题、描述、分类标签，以及 `href="#"` 换成你的作品链接 |
| 「联系我」 | 邮箱、微信、GitHub、小红书等链接 |
| 页脚 | 年份和署名 |

### 背景图

页面的水墨背景是 `ink-bg.svg`（一张 SVG 山景：远山、云雾、墨迹和纸张纹理）。想换成自己的背景图时，直接替换这个文件；或者修改 `style.css` 里 `.bg-ink` 的 `background`，指向你自己的图片地址。

### 怎么把渐变色卡片换成真实图片

目前每张作品卡片的封面是一块渐变色块（见 `style.css` 里的 `.work-thumb-1` 等）。
想换成真实图片时，在 `index.html` 里把对应的封面替换成：

```html
<a href="作品链接" class="work-thumb"><img src="图片路径.jpg" alt="作品名称"></a>
```

然后在 `style.css` 里加一行，让图片填满卡片：

```css
.work-thumb img { width: 100%; height: 100%; object-fit: cover; display: block; }
```

### 怎么新增一个作品卡片

复制任意一段 `<article class="work-card ...">…</article>`，改标题、描述和 `data-category`（`design` / `dev` / `photo`，或者新增自己的分类，并在「筛选按钮」区域加一个对应按钮）。

## 如何发布到网上

两种免费方式：

1. **GitHub Pages**：把整个文件夹推到 GitHub 仓库，在仓库 Settings → Pages 里选择分支和根目录，即可获得一个公网地址。
2. **Netlify Drop**：打开 app.netlify.com/drop，把整个文件夹拖进去，立刻得到一个线上地址。

发布前记得把占位内容全部替换成真实信息。
