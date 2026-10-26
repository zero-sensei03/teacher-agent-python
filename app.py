import streamlit as st

from src.agent.tasks import get_task_areas
from src.agent.workflow import run_workflow


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
    "Prototipe ini masih dalam tahap pengembangan. "
    "Fitur utama akan disesuaikan berdasarkan hasil penelitian."
)

st.subheader("Eksplorasi kebutuhan")

area_pekerjaan = st.selectbox(
    "Area pekerjaan guru",
    ["Pilih area pekerjaan", *get_task_areas()],
)

instruksi = st.text_area(
    "Instruksi",
    placeholder="Contoh: Buat materi pembelajaran IPA tentang ekosistem.",
    max_chars=5000,
    help="Masukkan instruksi yang ingin diuji.",
)

if st.button("Jalankan workflow", type="primary"):
    if area_pekerjaan == "Pilih area pekerjaan":
        st.warning("Silakan pilih area pekerjaan guru terlebih dahulu.")
    else:
        hasil = run_workflow(instruksi)

        if hasil.success:
            st.success(hasil.message)
        else:
            st.error(hasil.message)

        if hasil.content:
            st.subheader("Hasil")
            st.write(hasil.content)

        if hasil.requires_review and hasil.success:
            st.info(
                "Hasil perlu diperiksa oleh guru sebelum digunakan."
            )

        st.caption(
            "Status: validasi instruksi saja. "
            "Pemrosesan AI belum diimplementasikan."
        )
