#!/usr/bin/env python3
"""Build an offline searchable palette gallery and compact SVG swatch reference."""
import html
import json
from pathlib import Path

from ccf_palette import grayscale_hex
from easyplot_palettes import easyplot_palette, easyplot_palette_info, easyplot_palettes

ROOT = Path(__file__).resolve().parents[1]


def sampled(record, n=16):
    if record["selection"] == "native":
        n = max(int(k) for k in record["native_sizes"] if int(k) <= n)
    elif record["selection"] == "prefix":
        n = min(n, len(record["colours"]))
    return easyplot_palette(record["id"], n)


def gallery():
    cards = []
    for meta in easyplot_palettes():
        record = easyplot_palette_info(meta["id"])
        colors = sampled(record)
        cards.append({"id": meta["id"], "family": meta["family"], "kind": meta["kind"],
                      "cvd": meta["cvd_status"], "note": meta["cvd_note"],
                      "colors": colors, "gray": [grayscale_hex(x) for x in colors],
                      "stored": len(record["colours"]), "source": record["source"]})
    data = json.dumps(cards, ensure_ascii=False).replace("</", "<\\/")
    return '''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>CCF Conference Colors · Research Workbench Skills</title>
<style>
:root{color-scheme:light;font:15px/1.6 system-ui,-apple-system,sans-serif;color:#222;background:#f7f8fa}*{box-sizing:border-box}
body{margin:0}main{max-width:1220px;margin:auto;padding:44px 32px}h1{font-size:38px;line-height:1.15;letter-spacing:-1.1px;margin:12px 0 16px}h2{font-size:16px;margin:0;font-weight:650}p{max-width:850px;margin:8px 0;color:#505863}.eyebrow{font-size:12px;letter-spacing:2px;font-weight:700;color:#4477aa}.stats{display:flex;gap:24px;flex-wrap:wrap;margin:24px 0}.stats strong{font-size:23px;margin-right:7px;color:#222}.tools{display:flex;flex-wrap:wrap;align-items:end;gap:14px;padding:20px 0;border-top:1px solid #dce0e5;border-bottom:1px solid #dce0e5}.tools label{font-size:12px;font-weight:650}.tools input[type=search],select{display:block;margin-top:4px;padding:10px 12px;border:1px solid #bac2cc;border-radius:5px;background:white;font:inherit;color:#222}.tools input[type=search]{width:280px}.check{padding:10px 0;display:flex;gap:7px;align-items:center}input[type=checkbox]{width:17px;height:17px}.count{padding:18px 0;color:#555e69;font-size:13px}#cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}.card{background:white;padding:19px;border:1px solid #dce0e5;border-radius:8px;min-width:0}.head{display:flex;justify-content:space-between;gap:12px;align-items:center}.copy{border:1px solid #c9cfd6;background:#fff;border-radius:4px;padding:4px 9px;font:inherit;font-size:12px;cursor:pointer}.copy:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #4477aa;outline-offset:2px}.meta{font-size:12px;color:#626b77;margin:4px 0 14px}.swatches{display:flex;height:54px;border:1px solid #e0e2e6;border-radius:4px;overflow:hidden}.swatch{flex:1;min-width:0}.note{font-size:12px;margin-top:10px}.source{font-size:12px;margin-top:8px}a{color:#235c92}.foot{margin-top:30px;padding-top:18px;border-top:1px solid #dce0e5;font-size:12px}.empty{grid-column:1/-1;padding:28px;background:white}code{font-size:12px}@media(max-width:740px){main{padding:26px 18px}h1{font-size:30px}#cards{grid-template-columns:1fr}.tools input[type=search]{width:100%}.tools label:first-child{width:100%}}
</style></head><body><main>
<div class="eyebrow">RESEARCH WORKBENCH SKILLS / COLOR REFERENCE</div>
<h1>CCF Conference Colors</h1>
<p>面向会议论文的配色工具箱：先匹配数据含义，再确定色板。用固定标签保持跨图一致，用实际图形检查可读性。</p>
<p>这里展示色板样本，不代表实验结果或 CCF 官方配色标准。CVD 标记来自上游资料；灰度预览不等于色觉缺陷模拟。</p>
<div class="stats"><span><strong>205</strong>套色板</span><span><strong>6</strong>个来源家族</span><span><strong>0</strong>外部页面依赖</span></div>
<div class="tools"><label>搜索名称、来源或类型<input id="search" type="search" placeholder="例如 tol、viridis、diverging"></label><label>来源<select id="family"><option value="">全部来源</option></select></label><label>数据含义<select id="kind"><option value="">全部类型</option></select></label><label class="check"><input id="gray" type="checkbox">灰度预览</label></div>
<div id="count" class="count" aria-live="polite"></div><div id="cards"></div>
<div class="foot">色板顺序与 HEX 来自 easyplot 固定版本，连续色板最多展示 16 个抽样色。具体类别数的 CVD 注记请查原始记录。<br><a href="../references/palette-guide.md">选择指南</a> · <a href="palettes.json">完整数据</a> · <a href="palette-licenses/NOTICES.md">逐来源许可与署名</a> · <a href="provenance.json">固定来源与记录哈希</a><p>This product includes color specifications and designs developed by Cynthia Brewer (http://colorbrewer.org/).</p></div>
</main><script>
const data=DATA_JSON;
const el=id=>document.getElementById(id);
for(const key of ['family','kind']) for(const value of [...new Set(data.map(x=>x[key]))].sort()){const o=document.createElement('option');o.value=value;o.textContent=value;el(key).append(o)}
const node=(tag,text,cls)=>{const n=document.createElement(tag);if(text!==undefined)n.textContent=text;if(cls)n.className=cls;return n};
function render(){const q=el('search').value.toLowerCase(),gray=el('gray').checked;
const rows=data.filter(x=>(!el('family').value||x.family===el('family').value)&&(!el('kind').value||x.kind===el('kind').value)&&[x.id,x.family,x.kind].join(' ').toLowerCase().includes(q));
el('count').textContent=`显示 ${rows.length} / ${data.length} 套 · ${gray?'等亮度灰度预览':'原始颜色预览'}`;el('cards').replaceChildren();
for(const x of rows){const card=node('article',undefined,'card'),head=node('div',undefined,'head');head.append(node('h2',x.id));const b=node('button','复制 ID','copy');b.type='button';b.addEventListener('click',async()=>{try{await navigator.clipboard.writeText(x.id);b.textContent='已复制'}catch{b.textContent=x.id}});head.append(b);card.append(head,node('div',`${x.family} · ${x.kind} · CVD: ${x.cvd}`,'meta'));
const strip=node('div',undefined,'swatches');strip.setAttribute('role','img');strip.setAttribute('aria-label',`${x.id}: ${(gray?x.gray:x.colors).join(', ')}`);(gray?x.gray:x.colors).forEach((c,i)=>{const s=node('span',undefined,'swatch');s.style.backgroundColor=c;s.title=`${i+1}: ${x.colors[i]}${gray?' → '+c:''}`;strip.append(s)});card.append(strip,node('p',`显示 ${x.colors.length} 色 / 主表 ${x.stored} 色。${x.note}`,'note'));const src=node('div',`${x.source.license} · `,'source');const a=node('a','原始资料');a.href=x.source.url;a.target='_blank';a.rel='noopener noreferrer';src.append(a);card.append(src);el('cards').append(card)}
if(!rows.length)el('cards').append(node('div','没有匹配的色板，请调整筛选条件。','empty'))}
for(const id of ['search','family','kind','gray'])el(id).addEventListener('input',render);render();
</script></body></html>
'''.replace('DATA_JSON', data)


def preview():
    rows = [("tol.bright", "METHODS / nominal categories", 7),
            ("tol.muted", "COMPARISONS / nominal categories", 9),
            ("viridis.viridis", "MAGNITUDE / ordered values", 16),
            ("scico.batlow", "MAGNITUDE / ordered values", 16),
            ("scico.vik", "DEVIATION / meaningful center", 16),
            ("cmocean.phase", "PHASE / periodic values", 16)]
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="728" viewBox="0 0 1120 728" role="img" aria-labelledby="title desc">',
             '<title id="title">CCF Conference Colors: six illustrative palette choices</title>',
             '<desc id="desc">Categorical, sequential, diverging and cyclic swatches with equal-luminance grayscale previews. This is a reference, not experimental data or CVD simulation.</desc>',
             '<rect width="1120" height="728" fill="#FAFBFC"/>',
             '<g font-family="Arial, Helvetica, sans-serif" fill="#222222">',
             '<text x="44" y="42" font-size="12" letter-spacing="2" fill="#4477AA">RESEARCH WORKBENCH SKILLS</text>',
             '<text x="44" y="88" font-size="32" font-weight="700">CCF Conference Colors</text>',
             '<text x="44" y="116" font-size="14" fill="#565E69">205 palettes · 6 source families · stable identities across figures</text>',
             '<text x="432" y="155" font-size="11" fill="#565E69">COLOR SAMPLES</text>',
             '<text x="838" y="155" font-size="11" fill="#565E69">GRAYSCALE SCREEN</text>']
    for index, (id, label, n) in enumerate(rows):
        y = 181 + index * 76
        colors = easyplot_palette(id, n)
        parts += [f'<text x="44" y="{y+15}" font-size="16" font-weight="700">{html.escape(id)}</text>',
                  f'<text x="44" y="{y+36}" font-size="11" fill="#565E69">{html.escape(label)}</text>']
        for x, width, values in [(432, 362, colors), (838, 238, [grayscale_hex(c) for c in colors])]:
            for i, c in enumerate(values):
                parts.append(f'<rect x="{x+i*width/n:.3f}" y="{y}" width="{width/n+0.01:.3f}" height="42" fill="{c}"/>')
    parts += ['<path d="M44 657H1076" stroke="#D5DAE1"/>',
              '<text x="44" y="684" font-size="12" fill="#565E69">Use the actual venue template. Add useful labels and non-color cues. No official CCF palette or CVD certification is implied.</text>',
              '<text x="44" y="706" font-size="11" fill="#565E69">Sources: Paul Tol, viridisLite, Fabio Crameri, cmocean. Full terms and all six families: palette-licenses/NOTICES.md.</text>',
              '</g></svg>']
    return '\n'.join(parts)+'\n'


def main():
    (ROOT/'assets/palette-gallery.html').write_text(gallery(), encoding='utf-8')
    (ROOT/'assets/palette-preview.svg').write_text(preview(), encoding='utf-8')
    print('Built offline gallery for 205 palettes and the compact SVG reference.')


if __name__ == '__main__':
    main()
