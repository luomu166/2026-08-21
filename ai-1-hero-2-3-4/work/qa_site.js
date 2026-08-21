const { chromium } = require("playwright-core");
const path = require("path");

const CHROME = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe";
const URL = "file:///" + path.resolve("outputs/portfolio-site/index.html").replace(/\\/g, "/");
const OUT = path.resolve("work/qa");

async function main() {
  const context = await chromium.launchPersistentContext(path.resolve("work/qa-profile"), {
    executablePath: CHROME,
    headless: true,
    viewport: { width: 1440, height: 900 },
  });
  const page = context.pages()[0] || (await context.newPage());

  const consoleErrors = [];
  const pageErrors = [];
  page.on("console", (m) => { if (m.type() === "error") consoleErrors.push(m.text()); });
  page.on("pageerror", (e) => pageErrors.push(String(e)));

  await page.goto(URL, { waitUntil: "load" });
  await page.waitForTimeout(2200);

  const report = {};

  // 横向溢出检查（忽略跑马灯与光标）
  report.overflow = await page.evaluate(() => {
    const vw = document.documentElement.clientWidth;
    const offenders = [];
    document.querySelectorAll("*").forEach((el) => {
      if (el.closest(".marquee") || el.closest(".cursor")) return;
      const cs = getComputedStyle(el);
      if (cs.display === "none" || cs.visibility === "hidden") return;
      const r = el.getBoundingClientRect();
      if (r.width === 0) return;
      if (r.right > vw + 2 || r.left < -2) {
        offenders.push(
          el.tagName.toLowerCase() + "." + String(el.className).split(" ")[0] +
          " L" + Math.round(r.left) + " R" + Math.round(r.right)
        );
      }
    });
    return { vw, count: offenders.length, sample: offenders.slice(0, 12) };
  });

  // 图片是否加载成功
  report.images = await page.evaluate(() =>
    Array.from(document.images).map((img) => ({
      src: img.src.split("/").slice(-2).join("/"),
      ok: img.naturalWidth > 0,
      w: img.naturalWidth,
    }))
  );

  // Hero 视频与画布状态
  report.hero = await page.evaluate(() => ({
    videoReadyState: document.getElementById("heroVideo").readyState,
    videoIsReadyClass: document.getElementById("heroVideo").classList.contains("is-ready"),
    canvasVisible: getComputedStyle(document.getElementById("heroCanvas")).opacity !== "0",
    title: document.querySelector(".hero-title").innerText.replace(/\s+/g, " "),
  }));

  // 滚动到底再回顶，触发全部 reveal
  await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
  await page.waitForTimeout(1400);
  report.revealAfterScroll = await page.evaluate(() => {
    const all = document.querySelectorAll(".reveal").length;
    const shown = document.querySelectorAll(".reveal.is-in").length;
    return { all, shown };
  });

  // 计数器
  report.stats = await page.evaluate(() =>
    Array.from(document.querySelectorAll("[data-count]")).map((el) => el.textContent)
  );

  // 截图：桌面各区块
  const shots = [
    ["hero", 0],
    ["about", 900],
    ["works", 2600],
    ["strengths", 4300],
    ["contact", 6200],
  ];
  for (const [name, y] of shots) {
    await page.evaluate((yy) => window.scrollTo(0, yy), y);
    await page.waitForTimeout(900);
    await page.screenshot({ path: path.join(OUT, `desktop-${name}.png`) });
  }

  // 移动端检查
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(URL, { waitUntil: "load" });
  await page.waitForTimeout(1800);

  report.mobile = await page.evaluate(() => {
    const vw = document.documentElement.clientWidth;
    const burger = document.getElementById("navBurger");
    const menu = document.getElementById("mobileMenu");
    const burgerVisible = getComputedStyle(burger).display !== "none";
    const menuClosed = !menu.classList.contains("open");
    return { vw, burgerVisible, menuClosed };
  });

  await page.click("#navBurger");
  await page.waitForTimeout(700);
  report.mobile.menuOpenAfterClick = await page.evaluate(() =>
    document.getElementById("mobileMenu").classList.contains("open")
  );
  await page.screenshot({ path: path.join(OUT, "mobile-menu.png") });
  await page.screenshot({ path: path.join(OUT, "mobile-hero.png") });

  report.consoleErrors = consoleErrors;
  report.pageErrors = pageErrors;

  console.log(JSON.stringify(report, null, 2));
  await context.close();
}

main().catch((e) => { console.error(e); process.exit(1); });
