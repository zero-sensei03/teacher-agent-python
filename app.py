import streamlit as st

st.set_page_config(
    page_title="Teacher Assistant Agent",
    page_icon="📚",
    layout="centered",
)

st.title("📚 Teacher Assistant Agent")

st.write(
    "Asisten AI untuk membantu pekerjaan guru SMP/MTs."
)

st.info(
    "Prototipe ini sedang dalam tahap pengembangan. "
    "Fitur utama akan ditentukan dan disesuaikan berdasarkan "
    "kebutuhan yang ditemukan dalam penelitian."
)

st.subheader("Eksplorasi kebutuhan")

st.write(
    "Pilih area pekerjaan yang ingin dieksplorasi. "
    "Pilihan ini masih bersifat sementara dan bukan penetapan "
    "masalah utama penelitian."
)

area_pekerjaan = st.selectbox(
    "Area pekerjaan guru",
    [
        "Pilih area pekerjaan",
        "Penyusunan materi pembelajaran",
        "Pembuatan soal dan pembahasan",
        "Pemeriksaan jawaban dan pengolahan nilai",
        "Administrasi pembelajaran",
    ],
)

if area_pekerjaan != "Pilih area pekerjaan":
    st.write(f"Area yang dipilih: **{area_pekerjaan}**")
    st.caption(
        "Belum ada pemrosesan AI pada tahap ini."
    )
