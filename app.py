import streamlit as st
from datetime import datetime

# ページ設定
st.set_page_config(page_title="緒方ツールBOX", layout="centered")

# カスタムCSS
st.markdown("""
    <style>
    .credit { text-align: right; font-size: 14px; color: #666; margin-bottom: -20px; }
    .stButton>button { height: 3.5em; font-size: 18px !important; font-weight: bold !important; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="credit">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title("🌐 緒方ツールBOX")
st.write("使いたいツールを選択してください")
st.markdown("---")

# アプリのリストとURL
# 11行目の左側（奇数番目）にテレビ番組表を追加
apps = [
    # 1行目
    ("🔢 伝送値換算(200-999)(DEC)", "https://200-999-o244vkvrcu7wufxndezrc5.streamlit.app/"),
    ("🌐 IPv4サブネット", "https://lan-ip-6a84chs983d8qrywcfi8ek.streamlit.app/"),
    
    # 2行目
    ("🔢 伝送値換算(990-FD0)(HEX)", "https://990-fd0-br5qdwlqpcg6xgzndxrfxk.streamlit.app/"),
    ("🔍 ポートスキャンツール", "https://traceroute-dh8dbomk7zmwzhngojchrs.streamlit.app/"),
    
    # 3行目
    ("🔢 伝送値換算(3200-FA00)(HEX)クラウドTM", "https://denatus-kouka-aktoharzrfntzg3ujbemx3.streamlit.app/"),
    ("⚡ 消費電力計算", "https://p-e-i-w-ciq65gzsje57g5t2bjibev.streamlit.app/"),
    
    # 4行目
    ("📡 dBm⇄dBμV変換", "https://dbm-dbuv-converter-aeqcnqxhxypoemfnmbecwh.streamlit.app/"),
    ("📏 ケーブル電圧降下計算", "https://denatus-kouka-mkzokbttfxvxryb4x9kxe6.streamlit.app/"),
    
    # 5行目
    ("📡 W ⇄ dBμV 変換", "https://w-db-v-5oemhzumvdhiaf4shewlhp.streamlit.app/"),
    ("📐 面積・坪・畳 換算", "https://m9ebpan3hnocsbchjgnc3c.streamlit.app/"),
    
    # 6行目
    ("📡 W ⇄ dBm 変換", "https://dxzv2ve2tarf3epbjekvk6.streamlit.app/"),
    ("⚖️ 質量・重量計算", "https://cx6vhj5b5eaum7yrtghzkm.streamlit.app/"),
    
    # 7行目
    ("📡 ＶＳＷＲ計算", "https://y2gpx3glcpxabyvquqwsu8.streamlit.app/"),
    ("🎨 カラー抵抗計算", "https://lbocbpi8ohzxyhudcamols.streamlit.app/"),

    # 8行目
    ("📡 無線回線設計シミュレーター", "https://kaisen-8haqu59gckjy2gi4a5jp5p.streamlit.app/"),
    ("⚡ コンデンサー容量・種類判別", "https://kondensa-fnudpeexwnfu7mz4dgziam.streamlit.app/"),

    # 9行目
    ("📡 同軸ケーブルロス計算", "https://sonsitus-8mequgtoz7d3i9znsbje4j.streamlit.app/"),
    ("🔌 オームの法則計算", "https://et2n3e8fbbryhpbmwsbvyc.streamlit.app/"),

    # 10行目
    ("📉 アッテネータ計算", "https://nytsvfneh7k5juuploydur.streamlit.app/"),
    ("🔋 バッテリー持続計算", "https://gzgy6vngtgrgxbafzgczbd.streamlit.app/"),

    # 11行目 (左側に追加)
    ("", ""), # 右側は空欄
    ("📺 テレビ・ラジオ番組表", "https://cw62cfu7zm7iar6znuxzbg.streamlit.app/"), # ※番組表アプリのURLを入れてください
]

# 2列でボタンを配置
cols = st.columns(2)
for i, (name, url) in enumerate(apps):
    with cols[i % 2]:
        if name:
            st.link_button(name, url, use_container_width=True)

st.markdown("---")
st.caption("※ボタンを押すと各アプリのページに移動します。")
