# Glad Accountancy：重新設計概念網站

UX CIRCLES 為 Glad Accountancy（Altrincham，香港人創辦的特許會計師行）製作的非官方重新設計概念。
這不是官方網站。官方網站：https://gladacc.co.uk/

- 網址：https://uxcircles.github.io/gladacc/（中文：`/zh/`）
- 所有頁面都設有 `noindex, nofollow`，`robots.txt` 禁止搜尋引擎收錄。

## 頁面

| 英文 | 中文 | 內容 |
| --- | --- | --- |
| `index.html` | `zh/index.html` | 主頁：電車相片、曼徹斯特道路牌、五項服務、旺角霓虹、獅子山、維港到 Altrincham、地圖 |
| `services.html` | `zh/services.html` | 五項服務（原網站五個服務頁合併為一頁） |
| `contact.html` | `zh/contact.html` | 查詢表格（開啟 WhatsApp 或電郵，不儲存資料）、地圖 |
| `privacy.html` | `zh/privacy.html` | 按 UK GDPR 更新的私隱政策草稿（需客戶審閱） |
| `404.html` | | 「此路不通」路牌 |

## 如何修改

所有文字都在 `_build/pages.py`，以 `L(英文, 中文)` 並排寫成。

```bash
python3 _build/pages.py     # 重新產生所有 HTML
python3 _build/fonts.py     # 修改中文字後重新子集化字型
```

修改 CSS 或 JS 後，把 `pages.py` 裡的 `V` 加一（防止手機讀舊檔）。

## 設計概念

- **標誌元素**：香港街道路牌。原網站滿是香港相片（電車、旺角、獅子山、天星小輪），自稱
  「Hongkonger Chartered Accountants」，辦公室在 Manchester Road。所以首頁把地址寫成一塊香港路牌：
  「曼徹斯特道 Manchester Road 197」。五項服務各有一塊路牌（會計道、報告街、稅務徑、薪俸里、評稅坊），
  404 頁是「此路不通」。商標裏的「樂」字印章（Glad＝樂）用作網站圖示、地圖標記及頁尾。
- **首屏類型**：`full-bleed-photo`。香港電車相片滿版，上面放路牌。以往的會計師概念網站
  全是 split-info-card 或 split-arch-photo，這次刻意不同。
- **電車**：香港叮叮與 Altrincham 的 Metrolink 呼應；地圖顯示由 Timperley 電車站步行的路線。
- **字型**：Red Hat Display（標題）、Source Sans 3（內文）、Chiron Hei HK（中文內文）、
  Chiron Sung HK（中文標題）。Chiron 系列按香港字形設計。
- **顏色**：路牌白 `#fbfaf6`、路牌黑 `#161616`、商標啡 `#803400`、香港電車綠 `#1d5c45`。
  前幾個會計師網站用了深藍、米色加金、紅色，這次轉用啡綠。
- **標題**：EN「Hong Kong chartered accountants on Manchester Road」／中「香港人創辦的會計師行，就在曼徹斯特道」。
- **字數**：主頁英文約 210 字，首屏少於 45 字；主頁 7 張圖片（佔頁面約 46%）。

## 資料來源

| 資料 | 來源 |
| --- | --- |
| 服務項目及原文用語（「Genuine business partner for small enterprises」「Honest, quick and responsive」） | gladacc.co.uk 主頁、/accounting、/reporting、/tax-and-vat、/payroll、/self-assessment、/contact-us |
| 「由香港特許會計師創辦」 | gladacc.co.uk 主頁「About Glad Accountancy」 |
| 地址 Office 5, 197 Manchester Road, Altrincham WA14 5NU | 主頁及 /contact-us |
| 電話／WhatsApp 07769 391052、info@gladacc.co.uk | 主頁及 /contact-us |
| 辦公時間 09:00–17:00 | 主頁及 /contact-us（未列明星期幾） |
| Glad Accountancy Limited、公司編號 05728991、Rochdale 註冊辦事處 | /privacy-policy 第 2 節 |
| 座標 | OpenStreetMap（197-201 Manchester Road） |
| Timperley 電車站步行約 17 分鐘（1.3 公里） | routing.openstreetmap.de 步行路線，見 `_build/routes.json` |

## 需要客戶確認

- 辦公時間是星期幾（原網站只顯示「Open today 09:00–17:00」）。
- 屬於哪個會計師公會（ICAEW、ACCA、HKICPA 等）及會員編號；原網站沒有列出。
- 中文名稱：網站只用「Glad Accountancy」，沒有自行加上中文名。
- 五塊服務路牌的街名（會計道等）是設計用的虛構名稱，不是真實地址。
- 私隱政策是草稿，需客戶審閱。

## 圖片來源

| 檔案 | 來源 | 授權 | 是否客戶自己的 |
| --- | --- | --- | --- |
| `hk-tram.webp` | gladacc.co.uk（Tram.jpg） | 客戶網站 | 是 |
| `mong-kok-neon.webp` | gladacc.co.uk（Mong-Kok.jpg） | 客戶網站 | 是 |
| `lion-rock.webp` | gladacc.co.uk（Lion rock.jpg） | 客戶網站 | 是 |
| `star-ferry.webp` | gladacc.co.uk（Harbour.jpg） | 客戶網站 | 是 |
| `glad-logo.png`、`seal.svg`、`favicon.svg` | gladacc.co.uk 商標；印章以 Chiron Sung HK 的「樂」字重繪 | 客戶商標 | 是 |
| `metrolink-altrincham.webp` | DS Pugh，Geograph 8414132（Wikimedia Commons） | CC BY-SA 2.0 | 否 |
| `altrincham-market-house.webp` | Richard Sutcliffe，Geograph 5324781（Wikimedia Commons） | CC BY-SA 2.0 | 否 |

客戶網站的四張香港相片原本來源不明，如客戶沒有使用權，應替換。

## 第三方

- MapLibre GL JS（BSD 授權）`assets/vendor/maplibre/`；地圖圖塊 OpenFreeMap，資料 © OpenStreetMap。
- 字型：Google Fonts（SIL Open Font License），自行託管。
