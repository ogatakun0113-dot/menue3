import streamlit as st
from datetime import datetime

# ページ設定
st.set_page_config(page_title="緒方専用・番組ハブ", layout="wide")

# --- サイドバーの設定 ---
with st.sidebar:
    st.header("⚙️ 設定")
    st.write("番組表の日付を切り替えられます。")
    
    # カレンダーを左メニューの一番下に配置（実際にはメニュー構成の上から順になりますが、視覚的に独立させます）
    st.markdown("---")
    selected_date = st.date_input(
        "📅 表示する日付を選択", 
        value=datetime.now(),
        help="カレンダーで選んだ日付の番組表リンクが生成されます"
    )
    
    # 選択された日付を変換
    date_param = selected_date.strftime("%Y%m%d")
    display_date = selected_date.strftime("%Y年%m月%d日")
    
    st.success(f"表示中: {display_date}")
    st.caption(f"パラメータ: {date_param}")

# --- メイン画面 ---
st.markdown('<p style="text-align: right; font-size: 12px; color: #666;">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title("📺 番組表ダイレクトハブ")
st.subheader(f"✨ {display_date} の番組表")

st.markdown("""
<style>
.main-btn { 
    background-color: #005A9C; 
    color: white !important; 
    padding: 20px; 
    border-radius: 12px; 
    text-align: center; 
    text-decoration: none; 
    display: block; 
    font-size: 22px; 
    font-weight: bold;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
.main-btn:hover { background-color: #004a80; text-decoration: none; transform: translateY(-2px); transition: 0.2s; }
</style>
""", unsafe_allow_html=True)

# 1. 地デジ (大阪: ggm_group_id=42)
td_url = f"https://bangumi.org/epg/td?broad_cast_date={date_param}&ggm_group_id=42"
st.markdown(f'<a href="{td_url}" target="_blank" class="main-btn">📡 地デジ（大阪）</a>', unsafe_allow_html=True)

# 2. BS放送
bs_url = f"https://bangumi.org/epg/bs?broad_cast_date={date_param}"
st.markdown(f'<a href="{bs_url}" target="_blank" class="main-btn">🛰️ BS放送</a>', unsafe_allow_html=True)

# 3. CS放送
cs_url = f"https://bangumi.org/epg/cs?broad_cast_date={date_param}"
st.markdown(f'<a href="{cs_url}" target="_blank" class="main-btn">🎬 CS放送</a>', unsafe_allow_html=True)

st.markdown("---")
st.info(f"💡 左メニューのカレンダーで日付を変えると、ボタンのリンク先も自動的に **{display_date}** 用に切り替わります。")
