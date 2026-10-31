import streamlit as st
from PIL import Image
import os

# Sayfa Ayarları
st.set_page_config(page_title="Hatice ❤️", page_icon="❤️", layout="centered")

# Sayfa Durumunu Yönetmek İçin
if 'page' not in st.session_state:
    st.session_state.page = 1


# Fotoğraf Yükleme Fonksiyonu
def load_image(path):
    if os.path.exists(path):
        return Image.open(path)
    return None


# ================== 1. SAYFA (GİRİŞ) ==================
if st.session_state.page == 1:
    st.title("🎂 Doğum Günün Kutlu OLSUUNN❤️")
    st.write("küçük bir sürpriz hazırladım ve fotolar nnne alaka bilmiyorum .")

    img = load_image("giris.jpg")
    if img:
        st.image(img)

    if st.button("🎁 bass bakalim"):
        st.session_state.page = 2
        st.rerun()

# ================== 2. SAYFA (WALL-E) ==================
elif st.session_state.page == 2:
    st.title("🤖 WALL-E EVEEE")
    st.write("İLK İZLDİGİMİZ VE HAKKINDA KONUSTUGUMUZ ANİMASYON oldugu icin onlari ayri biz diye seviyorum❤️")

    img = load_image("walle.jpg")
    if img:
        st.image(img)

    if st.button("⭐ letssgooooo"):
        st.session_state.page = 3
        st.rerun()

# ================== 3. SAYFA (DİŞSİZ) ==================
elif st.session_state.page == 3:
    st.title("🐉 Dişsiz ve IŞIĞIN ÖFKESİ YANİ BİZ")
    st.write("benim için cok cok cok özelsin bal petegim İyi kiiiiii varsın❤️")

    img = load_image("dissiz.jpg")
    if img:
        st.image(img)

    if st.button("📸 devam ediyoruz"):
        st.session_state.page = 4
        st.rerun()

# ================== 4. SAYFA (FİNAL 1) ==================
elif st.session_state.page == 4:
    st.title("❤️❤️")
    st.write("Bugün senin günün.\nİyi ki doğdun AŞKIMMMM❤️")

    img = load_image("final1.jpg")
    if img:
        st.image(img)

    if st.button("💌 devams"):
        st.session_state.page = 5
        st.rerun()

# ================== 5. SAYFA (FİNAL 3 - STARDEW) ==================
elif st.session_state.page == 5:
    st.title("STARDEWEEWWWW")
    st.write("twdan rastgele bi gece dmlesip tanıstıgım kızla geldigim son nokta❤️")

    img = load_image("final3.jpeg")
    if img:
        st.image(img)

    if st.button("⭐ finito son1"):
        st.session_state.page = 6
        st.rerun()

# ================== 6. SAYFA (SON) ==================
elif st.session_state.page == 6:
    st.title("SENİ ÇOK SEVİYORUM OMRUMM❤️")
    st.write("artık tum doğum günlerini birlikte kutlamak dileğiyle bebegimm..❤️")

    img = load_image("final2.jpg")
    if img:
        st.image(img)

    if st.button("❤️biitttiii❤️"):
        st.session_state.page = 1
        st.rerun()