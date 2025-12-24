import streamlit as st

st.set_page_config(layout="wide", page_title="Merry Christmas", page_icon="🎄")
# Tạo màu nền Giáng sinh (Ví dụ: Màu đỏ nhung)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #8B0000; /* Màu nền */
        color: white;              /* Màu chữ toàn bộ trang */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("<h1 style='text-align: center;'>🎄 Merry Christmas! 🎅</h1>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([3, 10, 3])

with col1:
    st.image("giangsinh.png", use_container_width=True)
with col2:
    st.write("""Ho ho ho, các bé ngoan yêu quý của ông! 🎅❤️ Ông già Noel đây, với túi quà đầy kèo sáng sủa nhất đêm nay và rạng sáng mai (24-25/12/2025 giờ VN), để các bé vui vẻ mà không lo bẫy nhà cái nha~ 😊⚽

🎁 Algeria vs Sudan:
         
    🦸‍♂️ Algeria win handicap -1 (odds ~2.3) vì Algeria mạnh như siêu anh hùng! ✨

    😘 BTTS No (odds ~1.8), Sudan khó ghi bàn lắm bé ơi! 🌟
         
🎁 Cameroon vs Gabon:
         
    ❄️ BTTS Yes (odds ~2.1) vì cả hai đội hay ghi bàn lắm, như ôm nhau vui vẻ! 🤗
    
    💥 Under 2.5 goals (odds ~1.7) để an toàn, không quá "nóng" đâu ❄️

Ông khuyên các bé bet vui vẻ, có trách nhiệm nha! Nếu thắng, nhớ mua quà cho ông nhé~ 🎁😉 Chúc Giáng sinh ấm áp! ❄️❤️""")

with col3:
    st.image("giangsinh.png", use_container_width=True)

st.snow()